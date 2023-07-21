.. role:: inputcell
    :class: inputcell
.. role:: interfacecell
    :class: interfacecell
.. role:: button
    :class: button


Getting Started
=====================
This section seeks to guide the reader through a number of basic steps.

.. _prerequisites:

Pre-requisites
------------------
Before using the SPLAT interface, ensure that you have the following software installed and files downloaded:

.. note::
	If you are already issued the SPLAT learning kit, the following software (except Microsoft Excel) can be accessed in the software folder. If the kit has not been issued to you yet, please fill in the `request form <https://forms.office.com/Pages/ResponsePage.aspx?id=sOvdzLvS0ESYSo5CpcBis8X-QNFmuJNIrZ3pyvqZdPxURVJMTUw0Mzg1SkFHOTFFV0lXTFhLN1NEVS4u>`_ , or contact the IRENA person you are in touch with.


-	Microsoft Excel (64 bit version, to check :ref:`checking_bits`)
-	IAEA MESSAGE tool
-  	A model
-   	SPLAT excel interface
-	(recommended) CBC solver

The MESSAGE software comes with a free solver called GLPK. If a different solver is needed, it will have to be installed separately. We recommend using the CBC solver for use with the SPLAT interface. Refer to :ref:`install_solver` for using alternative solvers like cbc. 

.. _conventions:

Conventions
----------------------
:inputcell:`User Input Cell`

Cells formatted as above (dark font with orange background) are user input cells, where the user is allowed and expected to enter data.

:interfacecell:`Reserved for Interface`

Cells formatted as above (dark font with pale grey background) are cells that are reserved for interface. These cells are populated by macros in the workbook or are calculated cells.

The tabs are organised according to the following conventions:

-	``Index`` sheet: lists all the sheets in the workbook
-	``Main`` sheet: where users set the model path, and select countries in the model
-	Yellow tabs: for reviewing and updating basic model inputs
-	Red tabs: for running a model and extracting results
-	Grey tabs: utilities available for more advanced users

.. _first_steps:

First Steps
------------------
This documentation uses a simple model for demonstration. You can use an existing MESSAGE model for most of the examples in this documentation.

.. _checking_bits:

Checking Excel version
+++++++++++++++++++++++++++++++

The SPLAT Excel interface requires the 64-bit default version of Excel for its main functions. You can check your version of Excel by clicking the :button:`File` menu > :button:`Account` > :button:`About Excel`. If you have the older 32-bit Excel, it is recommended to uninstall and re-install your Microsoft Office software with 64-bit selected, or to use a computer with 64-bit software already installed.

.. image:: /images/getting_started_opening_file_2.PNG

.. _restoring_model:

Restore model in MESSAGE
++++++++++++++++++++++++++++++++

In order to run the model using the SPLAT excel interface, you may have to restore the model in MESSAGE once. Refer to the how-to guide on :ref:`using_message` for instructions on using MESSAGE.

.. _opening_file:

Opening the file
++++++++++++++++++++++
Open the Excel file that starts with *SPLAT_Interface_...*.

When you open the file, you must click :button:`Enable Content` (as shown below) for the file to function.

.. image:: /images/getting_started_opening_file.PNG

Also, macros must be enabled. Refer to link to `enable macros <https://support.microsoft.com/en-gb/office/enable-or-disable-macros-in-microsoft-365-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6>`_

.. _checking_decimal:

Checking system's decimal symbol
++++++++++++++++++++++++++++++++++++++++++++++
The decimal separator of your system must be set to '.' (point) in order for the SPLAT Excel interface to function properly. If it is otherwise, e.g. ',' (comma), please go to ``Control Panel`` > ``Region`` > ``Additional settings``, and change decimal symbol to '.'.

.. note::
    The comma separator is often the default in French windows environments and would have to be changed in order to be able to use the interface. Refer to :ref:`change_decimal_seperator`.

.. _link_interface:

Linking the interface to your model file
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

1. In the ``Main`` tab of the file, make sure the fields :inputcell:`Model Folder` and :inputcell:`Main Region` are set correctly as shown below, to reflect the location of the restored MESSAGE model folder on your computer.

2. In the ``Subregions`` section of the ``Main`` tab, choose which country / countries you want to activate, by placing a "1" next to it the orange column, and a "0" next to any other countries.

3. Click the :button:`Reload Global` button at the top of the page (this connects the MESSAGE model files with this Excel workbook). The model files are read and loaded into memory in Excel.

4. You will see a pop-up window which says "2 Countries data loaded in memory" (as shown below); press :button:`OK`.

.. image:: /images/getting_started_linking_interface_1.PNG

.. image:: /images/getting_started_linking_interface_2.PNG

.. _view_input:

Viewing model input
++++++++++++++++++++++++++++++

The SPLAT Excel interface allows a user to see the input data stored in SPLAT-MESSAGE models.

1. In any of the yellow tabs, choose the scenario from the dropdown list in cell C3.

2. Click on :button:`Refresh Sheet`, the data stored in the model will show in the table.

This process works the same way for all the yellow tabs (``Demand``, ``Transmission``, ``Distribution``, etc.) of the SPLAT Excel Interface. You can also refresh all sheets in these tabs by clicking the :button:`Refresh all Sheets` in the ``Main`` tab.

.. image:: /images/getting_started_viewing_input.PNG


.. caution::
	If you have emptied the cells under the table header, pressing the 'Refresh sheet' will cause an error. This occurs because the underlying macro code is unable to identify the start cell to start pasting the requisite model data. If you come across this error, click 'end' > Reload global > write some simple single alphabet in the cell right under the first cell of table header > refresh sheet. 


.. note::
    Keep in mind that the "adb" (Application Database) scenario contains all of the basic data in the model. Choosing another scenario will show only the data that is **different** in that scenario. So, if you choose a scenario and the data is blank, then it means it has the same data as the "adb".


.. _run_model:

Running the model
++++++++++++++++++++++++

**After** linking your model to the interface file in the ``Main`` tab, you can run your SPLAT model using the ``ReportGen-Annual`` tab.

1.	Select the correct scenario and country combination that you want to run.
To run the model for entire continent, select all the countries and "MAINa" in Subregions/Countries.

2.  Select the preferred option (with or without interconnections between subregions) under ``Run Options (Subregions)``. 
For a single county model, select :inputcell:`Separate Subregions`. 
For a multi-country model, :inputcell:`Separate Subregions` or :inputcell:`Interconnected` can be selected depending on the scenario narrative for interconnection between countries.
In this example we select :inputcell:`Interconnected`` option.

3.	Select the correct option under the "Run" categories. The categories correspond to the same options in the MESSAGE "Run" menu:
	:inputcell:`Mxg` = Matrix Generator;
	:inputcell:`Opt` = Optimisation;
	:inputcell:`Cap` = Calculator program (Cap) file creation;
	:inputcell:`All` = perform all of the above.
	There are three different options provided in the interface for CPLEX, CBC and GUROBI depending on which solver you have pre-installed. If you are a new user, please install and use CBC (:ref:`install_solver`).

4.	Press the :button:`Run` button. You should see the black MESSAGE window appear and begin to run.

.. image:: /images/getting_started_running_model.PNG

.. _extract_results:

Extracting the results
++++++++++++++++++++++++++++++

Use the ReportGen tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The ``ReportGen-Annual`` tab is also where you can pull in the results of the model that you just ran.

1.	Select the scenario(s), country(s), variable(s) and year(s) combination that you want to view the results of. Please ensure that your desired scenario has been loaded in the excel memory. If it does not appear in the dropdown list, please go again to 'Main' tab and mark the desired scenario '1' and press 'Reload Global' button.

2.  Select the output format and enter output path (if applicable) under ``Results Destination`` section.

3.	Click on :button:`Get Results` (red circle in picture below). If :inputcell:`on this sheet` is selected, you should see raw results appear on the sheet when the process is finished. If :inputcell:`csv` is selected, then the results will be written to a csv file at the specified location. If the location doesn't exist then there will be an error message. The csv option is more convenient when working with large set of results, and they can be linked to other pivot tables in Excel or other software such as PowerBi or Tableau.

.. image:: /images/getting_started_extract_results_1.PNG

Update the results charts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can find the yearly result charts in the red sheets: ``Capacity``, ``Output``, ``New Capacity``, ``CO2``, and ``Costs``.

.. important::

    Please be sure to check that the correct scenario and country are chosen at the top of the table.

Right-click anywhere in the table on the worksheet, and select :button:`Refresh` from the options. These charts need to be updated **every time** you pull in new results.

.. image:: /images/getting_started_extract_results_2.PNG
