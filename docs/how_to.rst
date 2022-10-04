.. role:: inputcell
    :class: inputcell
.. role:: interfacecell
    :class: interfacecell
.. role:: button
    :class: button

How-To Guides
=============

.. _install_solver:

Installing an Alternative (Faster) Free Solver
----------------------------------------------

The MESSAGE software comes by default with a free solver called GLPK. This solver is adequate for working with small models, however, when a larger model is to be used (e.g. many timeslices, many technologies and subregions), this solver becomes inadequate requiring a long time to complete a "RUN".

There is an alternative free solver that can be used with MESSAGE called the CBC (Coil-or Branch and Cut solver [link:https://github.com/coin-or/Cbc]) that is more powerful and can solve larger problems at comparable speeds to some of the commercial solvers such as CPLEX.

However, to execute runs with this solver one must use the SPLAT Excel Interface to initiate runs (see Tutorial C - Using the SPLAT Excel Interface) and one has to add the solver to the user's existing MESSAGE installation. This guide gives a brief description on how to do this installation.

1. Download the cbc.rar archive file from Sharepoint and put it in the MESSAGE installation folder called:
``C:\Programs\MESSAGE_INT\message_bin``

.. image:: how_to_1.PNG

2. Use a 3rd party software such as Winrar to extract the files from ``cbc.rar`` into the ``C:\Programs\MESSAGE_INT\message_bin`` folder (use "extract here")
Some of the files may already exist in the folder, you can accept to overwrite those files with the ones from the ``cbc.rar`` archive.


.. _using_message:

Restoring and opening a model using the MESSAGE interface
----------------------------------------------------------


1. From the most recent folder that is being used in the training programme Sharepoint: Link to Sharepoint

Save the ZIP file that starts with ``\MAINa_...`` into a known location of the computer

2. After installation of MESSAGE, open the program and two windows will open; the blue one is the user interface for Windows OS and the black one is the command window for MESSAGE.

.. important::

    You will use the blue windows but always leave the black window open:

.. image:: how_to_using_message_1.PNG

.. image:: how_to_using_message_2.PNG

3. Select :button:`Cases` > :button:`Restore`

.. image:: how_to_using_message_3.PNG

4. Select the ZIP file ``MAINa_...`` located in the place you previously saved

.. image:: how_to_using_message_4.PNG

5. Select :button:`Cases` > :button:`Open`

.. image:: how_to_using_message_5.PNG

.. image:: how_to_using_message_6.PNG

6. Select "Africa" and your country code (Please see Table).

.. image:: how_to_using_message_7.PNG

.. image:: how_to_using_message_8.PNG

For example, suppose your country is Cameroon, then you choose the code CMa, then the following window will appear with Case Study : CMa.

.. image:: how_to_using_message_9.PNG

7. You have now the Country model of your choice, which you can edit or work with.

If you click :button:`Edit` and then click :button:`application db`, you get the following screen which you can use to view most of your model's input data.

.. image:: how_to_using_message_10.PNG
