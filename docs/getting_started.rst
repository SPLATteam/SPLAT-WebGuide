.. only:: html

Getting Started
===============

.. _prerequisites:

Pre-requisites
--------------
Before using the SPLAT interface, ensure that you have the following software installed

-	Microsoft Excel
-	MESSAGE

The MESSAGE software comes with a free solver called GLPK. If a different solver is needed, it will have to be installed separately. Refer to :ref:`using_message` for using alternative solvers.

.. _conventions:

Conventions
----------------

:inputcell: `User Input Cell`

Cells formatted as above (dark font with orange background) are user input cells, where the user is allowed and expected to enter data.

:interfacecell: `Reserved for Interface`

Cells formatted as above (dark font with pale grey background) are cells that are reserved for interface. These cells are populated by macros in the workbook or are calculated cells.

The tabs are organised according to the following conventions:

-	Index sheet: lists all the sheets in the workbook
-	Main sheet: where users set the model path, and select countries in the model
-	Yellow tabs: for reviewing and updating basic model inputs
-	Red tabs: for running a model and extracting results
-	Grey tabs: utilities available for more advanced users

.. _first_steps:

First Steps
--------------
This documentation uses a simple model [to link] for demonstration. You can use an existing MESSAGE model for most of the examples in this documentation.

.. _opening_file:

Opening the file
++++++++++++++++
Open the Excel file that starts with *SPLAT_Interface_...*. When you open the file, you must click *Enable Content* (as shown below) for the file to function.

.. image:: getting_started_opening_file.PNG

.. _checking_decimal:

Checking system's decimal symbol
++++++++++++++++++++++++++++++++++
The "decimal separator" of your system must be set to '.' (point) in order for the SPLAT Excel interface to function properly. If it is otherwise, e.g. ',' (comma), please go to Control Panel > Region > Additional settings, and change decimal symbol to '.'.

The comma separator is often the default in French windows environments and would have to be changed in order to be able to use the interface.

