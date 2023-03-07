.. role:: inputcell
    :class: inputcell
.. role:: interfacecell
    :class: interfacecell
.. role:: button
    :class: button

Working with Demand
============================

.. important::
    The interface must be linked to the model before executing any of the steps in this section.
    See :ref:`link_interface`.

This section describes how to view, change and add demand using the SPLAT interface.

.. view_demand:

Viewing demand input
-----------------------------

1. In the ``Demand`` tab, enter the scenario to be queried in the cell ``Choose Scenario``

2. Click on :button:`Refresh Sheet`. The annual demand in the scenario (adb or ldb file) will be shown in the same sheet. Only data for the country(s) loaded (in the ``Main`` sheet) will be displayed.

3. In the ``PeakDemand`` tab, repeat steps 1 and 2 to retrieve the peak demand for the selected scenario.

.. note::
    Provision was made to either work with "sent-out" demand or sectoral demand such as industrial, urban and rural. The user will see demand data categorised into these said multiple demand levels. If the model is using just the send-out demand, user must set the data on other demand levels to zero, and vice versa otherwise demand will be double counted. Also note that the raw data is stored in the adb and ldb files in MWyr. The MWyr values are converted by SPLAT to GWh by default. 
	
.. note::
	Peak demand is not a direct input in SPLAT model. The Peak demand is estimated based on the annual energy values and the corresponding profile parameterization stored in the Application Database (adb) file. 
	
.. change_demand:

Changing demand input
------------------------------

1. In the ``Demand`` tab, click on :button:`Refresh Sheet` to get the data saved in the model.

2. Make changes to the demand series in the sheet.

3. Click on :button:`Update Sheet` to update the model with the new data.

.. image:: /images/demand_update.PNG



