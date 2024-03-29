# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SPLAT Interface'
copyright = '2023, IRENA'
author = 'Yunshu Li, Himalaya Bir Shrestha'

release = '0.1'
version = '0.1.0'

#formats = ["epub", "pdf"]

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/splat_interface.css',
]

html_style = 'css/splat_interface.css'


# -- Options for EPUB output
epub_show_urls = 'footnote'

locale_dirs = ['locale']
