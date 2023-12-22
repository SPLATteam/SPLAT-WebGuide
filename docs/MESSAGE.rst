.. role:: inputcell
    :class: inputcell
.. role:: interfacecell
    :class: interfacecell
.. role:: button
    :class: button
.. role:: tight-table
    :class: tight-table

MESSAGE 
=============================
**Model for Energy System Strategy Alternatives and their General Environmental Impacts (MESSAGE)**
has been desgined to develop an optimization model of an energy system for medium to long term planning, energy policy analysis and scenario development.
MESSAGE formulates the dynamic linear programming model with a mixed integer option. 
(Nonlinear constraints or nonlinear objective function can only be defined for specific problem.)

.. _objective_function:

Objective function in MESSAGE
-----------------------------

The objective function in MESSAGE contains the sum of all discounted costs, i.e. all kinds of costs that can be accounted for.
All costs related to operation (i.e. resource use, operation costs, costs of demand elasticities) are discounted from the middle of the current period to the base year to get the present value.

.. note::
    Discounting makes the costs occurring in differnt periods comparable; the discount rate defines the weights different periods get in the optimization.
    In principle, it should be equal to the long-term real interest rate, i.e. excluding inflation or any other opportunity costs.
    A high discount rate gives more weight or importance to present expenditures than to future ones, while a low discount rate reduces these differences and thus favours technologies that have high investment costs but low operation costs.

MESSAGE solves the optimization model in the following two steps:

1. Generation of matrix.

2. Optimization of model using the generated matrix.

The model generates minimal total discounted system costs, including investment, operation and maintenance, fuel and any other user-defined costs, while meeting various system requirements (e.g. sufficient supply to match demand at a given time or sufficient resources and capacity to achieve the desired production) and user-defined constraints (e.g. reserve margin, speed of technology deployment, emission limits, policy targets).

.. _components:

Components in MESSAGE
--------------------------------

The current version of the MESSAGE software (V5) consists of the following components:

* A user-interface for building a model.

* Databases.

* A matrix generation program called "mxg".

* An optimization program called "opt".

* A program for the post processing of the solution for extraction of results called "cap".

The following figure shows the flow of control and information between these components in execution of the MESSAGE program.

.. image:: /images/message_components.PNG

The first part of this section describes the various databases used in MESSAGE. And the second part describes the significance of modelling files created by various programs while using MESSAGE.

.. _Databases_in_MESSAGE:

Databases in MESSAGE
--------------------------------
MESSAGE creates each model in a separate case study and accordingly one database file for each model. The types of databases used in MESSAGE are given in the table below:

.. csv-table::
    :class: full-width
    :header-rows: 1
    :file: csv_file/message_databases.csv  
    :widths: 10 20 50
   
The interrelationship of the databases used in the MESSAGE program is depicted in the figure below:

.. image:: /images/message_databases.PNG

Significance of various MESSAGE model files
-----------------------------------------------------------
This section describes the various file types which are present or created within the sub-folders such as ``data``, ``int``, and ``res`` inside the ``models/Region`` folder while running the MESSAGE.

.. note::
  * ``Region`` could refer to an acronym for a country e.g., ``ZAa`` for SouthAfrica or ``MAINa`` for the entire continent.
  
  * ``CaseName`` refers to a scenario.
  
  * ``MXG`` is a matrix generation program and ``CAP`` is used for post processing of the solution and for extraction of results within MESSAGE GUI application.

File types inside data folder
+++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :class: full-width
    :header-rows: 1
    :file: csv_file/message_data.csv

File types inside intm (interim) folder
+++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :class: full-width
    :header-rows: 1
    :file: csv_file/message_intm.csv

File types inside res folder
+++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :class: full-width
    :header-rows: 1
    :file: csv_file/message_res.csv

.. _splat_message_workflow:

SPLAT MESSAGE workflow
-------------------------------

The SPLAT MESSAGE workflow diagram looks as follows:

.. image:: /images/splat_message_workflow.PNG

