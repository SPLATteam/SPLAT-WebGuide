.. role:: inputcell
    :class: inputcell
.. role:: interfacecell
    :class: interfacecell
.. role:: button
    :class: button
.. role:: tight-table
    :class: tight-table

MESSAGE 
=====================
Model for Energy System Strategy Alternatives and their General Environmental Impacts (MESSAGE)
has been desgined to develop an optimization model of an energy system for medium to long term planning, energy policy analysis and scenario development.
MESSAGE formulates the dynamic linear programming model with a mixed integer option. 
(Nonlinear constraints or nonlinear objective function can only be defined for specific problem.)
MESSAGE solves the optimization model in the following two steps:

1. Generation of matrix.

2. Optimization of model using the generated matrix.

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
+-----------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Acronyms  | Full form             | Significance                                                                                                                                                                                                                                                                                                                                    |
+===========+=======================+=================================================================================================================================================================================================================================================================================================================================================+
| adb       | Application database  | adb file is created and maintained for each case study. It contains information on default scenario created by MESSAGE. For a new case study, it is appropriate to work on its adb rather than creating a scenario and working on an ldb.                                                                                                       |
| ldb       | Local database        | ldb file is created and maintained for each (alternative) scenario in a case study. It is a copy of adb file. It is created for each alternative scenario, which user can modify as per their scenario narratives. When input sheets (parameters) are updated in SPLAT for alternative scenario, the corresponding ldb files also get updated.  |
| tdb       | Technology database   | tdb file is created and maintained independent of any case study                                                                                                                                                                                                                                                                                |
| upd       | Update database       | upd file is created and maintained to update values in the adb and/or a set of scenarios in a case study across the board.                                                                                                                                                                                                                      |
+-----------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
.. .. csv-table:: Databases in MESSAGE
..     :header-rows: 1
..     :file: csv_file/message_databases.csv     
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

  

