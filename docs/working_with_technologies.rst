.. role:: inputcell
    :class: inputcell
.. role:: interfacecell
    :class: interfacecell
.. role:: button
    :class: button


Working with Technologies
==========================

.. important::
    The interface must be linked to the model before executing any of the steps in this section.
    See :ref:`link_interface`.

A technology in the model is a power-producing unit or a combination of such units or a transmission line with specific parameters such as, maximum capacity, capacity factor, CAPEX, FOM, fuel cost etc.

A technology can be site specific (a specific plant or transmission line with known parameters) or generic (a technology with generalised parameters).

The Technology tabs are listed at :ref:`technologysheets`

This section describes how to view, add and change technologies using the SPLAT Excel Interface.

.. _view_tech_inputs:

Viewing technology inputs
-------------------------

1. In any of the :ref:`technologysheets` (except the tabs containing information of specific zones), enter the scenario to be queried in the cell ``Choose Scenario``

2. Click on :button:`Refresh Sheet`. The technologies and their parameters in the scenario will be shown in the same sheet. Only data for the country(s) loaded (in the ``Main`` sheet) will be displayed.

3. Refer to :ref:`renewable_tech` for steps to retrieve the information of renewable zones (Solar PV, Solar CSP, Onshore Wind, Offshore Wind).

.. _add_tech:

Adding a technology
-------------------

to fill

.. _rename_tech:

Renaming a technology 
---------------------

1. Enter the old and new technology names in :ref:`RenameTechFacility` and click on :button:`Rename Techs in List`. 

2. To confirm that the technology has been renamed, refresh the relevant tabs (``GenericTech`` or ``SpecificTech``) to see the updated names. Multiple technologies can be renamed.

..image:: technology_rename.PNG

.. _delete_tech:

Deleting a technology
----------------------

1. Enter the technology names in :ref:`DeleteTechFacility` and click on :button:`Delete Techs in List`. 

2. To confirm that the technology has been deleted, refresh the relevant tabs (``GenericTech`` or ``SpecificTech``) to see the update. Multiple technologies can be deleted.

..image:: technology_delete.PNG

.. _change_tech:

Changing a technology 
----------------------

1. In any of the :ref:`technologysheets` (except the tabs containing information of specific zones), click on :button:`Refresh Sheet` to get the data saved in the model for the scenario chosen.

2. Make changes to the technologies in the sheet.

3. Click on :button:`Update Model Data` to update the model with the new data.

.. _fuel:

Fuel price
-----------

1. In the tab :ref:`fuelprices`, click on :button:`Refresh Sheet` to get the data saved in the model for the scenario and countries chosen.

2. Make changes to the fuel prices in the sheet.

3. Click on :button:`Update Model Data` to update the model with the new data.

.. note::
    1. The fuel price is specified in $/GJ. It is currently not possible to add new fuel supply technologies via the SPLAT interface, this is left for future development (as well as the possibility of specifying limits, which would be needed if one wanted to model a supply curve for a particular fuel).
    2. If a user specifies values both in the Constant column, as well as under milestone year columns, only the constant value will be used to update the MESSAGE model and the other values will be ignored.

.. _tech_cost:

Technology costs
-----------------

1. In the tab :ref:`generictechcosts` and :ref:`specifictechcosts`, click on :button:`Refresh Sheet` to get the cost data saved in the model for the scenario and countries chosen.

2. Make changes to the costs (Overnight Cost-$/kW, Fixed O&M Cost-$/kW, Variable O&M Cost-$/MWh) in the sheet.

3. Click on :button:`Update Model Data` to update the model with the new data.

.. note::
    If a user specifies values both in the Constant column, as well as under milestone year columns, only the constant value will be used to update the MESSAGE model and the other values will be ignored.

.. _tech_capacity:

Capacity Limit
---------------

1. In the tab :ref:`specificcapacitylimits`, click on :button:`Refresh Sheet` to get the capacity limits saved in the model for the scenario and countries chosen.

2. Make changes to the capacity limits in the sheet.

3. Click on :button:`Update Model Data` to update the model with the new data.

.. note::
    If a user specifies values both in the Constant column, as well as under milestone year columns, only the constant value will be used to update the MESSAGE model and the other values will be ignored.

.. _renewable_tech:

Renewable and storage technologies
----------------------------------

.. _solar_wind:

Solar PV, onshore and offshore Wind
+++++++++++++++++++++++++++++++++++

VRE technologies can be defined in two ways - either as generic technologies or site-specific technologies.

.. _hydro_dam:

Hydro Dam
++++++++++

The ``SpecificTechHydroDams`` sheet manipulates the hydro dams in the model.

:button:`Refresh Sheet` button extracts the technologies that belong to the `TechSetL2`: `Large Hydro Dams`.

:button:`Create River Tech+Storage Constraint` button adds a technology and a storage constraint for each dam.

A new dummy technology for each hydro station with Dam is added to model the river inflows to the dam. The naming convention of the dummy technology is XXRIDM_rivername, for example CMRIDM_LAGDO (using LAGDO as an example).  The output is set to the existing dummy elc energy form.

A new storage constraint is added, example D_LAGDO with short name DXXX. The storage constraint is linked to CMRIDM_LAGDO with +1 coefficient, so each MWyr flow from CMRIDM_LAGDO increases the storage content by 1 MWyr.

The storage constraint is linked to CMHYDM_LAGDO with -1 coefficient (meaning that each MWyr flow from CMHYDM_LAGDO decreases the storage content by 1 MWyr). It would be possible in theory to do cascade modelling by linking the output of upstream plants to storage constraints downstream (rather than a river technology). The coefficients would have to be scaled by the relative "Energy per unit volume (MJ/m3)" of the upstream and downstream plants. This functionality will need a revisit as a new development task if there is a pressing need for it.

The user has to specify 2 parameters, whose values can be calculated in the right-most table and copy pasted.

Once this is done the user can click on :button:`Update Model Data`:

The capacity is set to max flow (in MW, m3/s max flow scaled by design flow). The capacity is specified as a capacity limit on the River Technology (bdi) .

The storage constraint max volume is set to Max volume in MWyr as per table.

The user then has to add a time series in the csv file under the tech CMRIDM_LAGDO and :button:`Update Timeslices` in the ``Timeslice`` sheet. The values in the csv file must be monthly average flow divided by "max flow" that was used to set the "River Capacity", using the same max flow value regardless of the scenario.
If the user wants to simulate different rainfall scenarios without a full time series, they could use plant factor to scale up or down the profile in the ``SpecificTech`` sheet. It is currently not possible to specify a different seasonal profile by scenario, but this feature is on the todo list for the near future.


.. _batteries:

Batteries
++++++++++

To Fill

.. _csp:

Concentrated Solar Power (CSP)
++++++++++++++++++++++++++++++

To Fill

.. _transmission_distribution:

Transmission and Distribution
-----------------------------

The `` ref:`transmission` `` and `` ref:`distribution` ``sheets are used to review or modify transmission and distribution technologies parameters as per the definitions in the ``TechnologySets`` sheet (see section below).

.. note::
    1. If the user wants to model with "sent-out" demand (see ref:`demand`), transmission efficiency must be set to 100%, and investment costs set to a small value. In the default configuration there is no distribution technology specified for "Sent-out" electricity.

    2. If a user specifies values both in the Constant column, as well as under milestone year columns, only the constant value will be used to update the MESSAGE model and the other values will be ignored.

.. _interconnection:

Interconnection
-----------------

The `` ref:`interconnectors` `` sheet is used to review and update cross-border interconnector parameters. 

At a minimum the two interconnecting countries (which must be active) must be specified to view the interconnections between them. 
