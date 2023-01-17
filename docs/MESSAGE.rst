.. role:: inputcell
    :class: inputcell
.. role:: interfacecell
    :class: interfacecell
.. role:: button
    :class: button

MESSAGE 
=====================
The current version of the MESSAGE software consists of the following components:

* A user-interface for building a model.

* Databases.

* A matrix generation program called "mxg".

* An optimization program called "opts".

* A program for the post processing of the solution for extraction of results called "cap".

The following figure shows the flow of control and information between these components in execution of the MESSAGE program.

.. image:: /images/message_components.PNG

The first part of this section describes the various databases used in MESSAGE. And the second part describes the significance of modelling files created by various programs while using MESSAGE.

.. _Databases_in_MESSAGE:

Databases in MESSAGE
------------------------
MESSAGE creates each model in a separate case study and accordingly one database file for each model.

.. csv-table:: Databases in MESSAGE
    :header-rows: 1
    :file: csv_file/message_databases.csv

The interrelationship of the databased in the MESSAGE program is depicted in the figure below:

.. image:: /images/message_databases.PNG

