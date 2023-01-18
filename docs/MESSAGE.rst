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
MESSAGE creates each model in a separate case study and accordingly one database file for each model. The types of databases used in MESSAGE are given in the table below:

.. csv-table:: Databases in MESSAGE
        :header-rows: 1
        :file: csv_file/message_databases.csv
        :width: 20 30 50

        
The interrelationship of the databases used in the MESSAGE program is depicted in the figure below:

.. image:: /images/message_databases.PNG

Significance of various MESSAGE model files
-------------------------------------------
This section describes the various file types which are present or created within the sub-folders such as ``data``, ``int``, and ``res`` inside the ``models/Region`` folder while running the MESSAGE.

.. note::
  * ``Region`` could refer to an acronym for a country e.g., ``ZAa`` for SouthAfrica or ``MAINa`` for the entire continent.
  
  * ``CaseName`` refers to a scenario.
  
  * ``MXG`` is a matrix generation program and ``CAP`` is used for post processing of the solution and for extraction of results within MESSAGE GUI application.

File types inside data folder
+++++++++++++++++++++++++++++
.. csv-table::
    :header-rows: 1
    :file: csv_file/message_data.csv

File types inside intm (interim) folder
+++++++++++++++++++++++++++++
.. csv-table::
    :header-rows: 1
    :file: csv_file/message_intm.csv

File types inside res folder
+++++++++++++++++++++++++++++
.. csv-table::
    :header-rows: 1
    :file: csv_file/message_res.csv

  

