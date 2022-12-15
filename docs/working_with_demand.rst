.. role:: inputcell
    :class: inputcell
.. role:: interfacecell
    :class: interfacecell
.. role:: button
    :class: button

Working with Demand
====================

.. important::
    The interface must be linked to the model before executing any of the steps in this section.
    See :ref:`link_interface`.

This section describes how to view, change and add demand using the SPLAT interface.

.. view_demand:

Viewing demand input
---------------------

1. In the ``Demand`` tab, enter the scenario to be queried in the cell ``Choose Scenario``

2. Click on :button:`Refresh Sheet`. The yearly demand in the scenario will be shown in the same sheet. Only data for the country(s) loaded (in the ``Main`` sheet) will be displayed.

3. In the ``PeakDemand`` tab, repeat steps 1 and 2 to retrieve the peak demand for the selected scenario.

.. note::
	Most SPLAT models only have Sent out demand. However, some models have also demand at industrial, urban , rural levels. The user will see demand data categorised into these said multiple demand levels. If the model is using just the send-out demand, user can simply ignore the data on other demand levels. These demand levels exist as an indication that a user always have the option to model these demand if he/she so wishes. 

.. note::
	Peak demand is not a direct input in SPLAT model. This sheet is populated by macro codes which multiply the peak of a normalised load curve with the region's annual electricity demand (Watt Hours).
	
	
.. change_demand:

Changing demand input
----------------------

1. In the ``Demand`` tab, click on :button:`Refresh Sheet` to get the data saved in the model.

2. Make changes to the demand series in the sheet.

3. Click on :button:`Update Sheet` to update the model with the new data.

.. image:: /images/demand_update.PNG



