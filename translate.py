# Developed for IRENA by Yunshu Li, March 2023

import six
from google.cloud import translate_v2 as translate
import glob
import os
import pandas as pd
import re

def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text,
                                        target_language=target,
                                        source_language="en",
                                        format_ ="text")

#    print(u"Text: {}".format(result["input"]))
#    print(u"Translation: {}".format(result["translatedText"]))
#    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
    return result


def read_text(file):
    with open(file) as f:
        lines = f.readlines()
    return lines


def replacer(regex):
    # modified from https://stackoverflow.com/a/54619385
    # temporarily replace variables of format "%(example_name)s" with "__n__" to
    #  protect them during translate()

    VAR, REPL = re.compile(r'{}'.format(regex)), re.compile(r'__0(\d+)__')
    return VAR, REPL


def protect_text(str, varlist, VAR):
    def replace(matchobj):
        varlist.append(matchobj.group())
        return "__0%d__" % (len(varlist) - 1)

    txt_protected = VAR.sub(replace, str)
    return txt_protected, varlist


def restore_text(str, varlist, REPL):
    def restore(matchobj):
        return varlist.pop(0)
    txt_restored = REPL.sub(restore, str)
    return txt_restored


def get_rst_files(folder):
    path = "{}/*.rst".format(folder)
    files = glob.glob(path)
    return files

def split(list_a, chunk_size):

    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i + chunk_size]

translate_client = translate.Client()

files = get_rst_files("docs")
path_translated = "translated"
isExist = os.path.exists(path_translated)
if not isExist:
   # Create a new directory because it does not exist
   os.makedirs(path_translated)

re_protect = pd.read_csv("protected_strings.csv") #read protected strings csv and get regex
regex = '|'.join(list(re_protect.regex)) #form regex
VAR, REPL = replacer(regex)

for f in files:
    print("Processing {}".format(f))
    lines = read_text(f)

    varlist = []
    lines_repl = []
    for l in lines:
        l_repl, varlist = protect_text(l, varlist, VAR)     #Replace protected strings with __n__
        lines_repl.append(l_repl)

    l_n = len(lines_repl)
    chunk_size = 50 #only translate 50 lines at a time
    if l_n <= 50:
        lines_lst = [lines_repl]
    else:
        lines_lst = split(lines_repl, chunk_size)
    dict_translated = []
    for i in lines_lst:
        dict_translated.extend(translate_text("fr", i))
    df = pd.DataFrame.from_dict(dict_translated)
    lines_trans = list(df['translatedText'])
    lines_rest = []
    for l in lines_trans:
        l_rest = restore_text(l, varlist, REPL)    #Replace back __n__ with strings
        lines_rest.append(l_rest)

    f_name = os.path.basename(f)
    path_out = "{}/{}".format(path_translated, f_name)
    with open(path_out, 'w+', encoding='utf-8') as f_rst:
        for l in lines_rest:
            f_rst.write(l)
    df['orig'] = lines
    df['final'] = lines_rest
    df.to_csv("{}_table.csv".format(path_out))

