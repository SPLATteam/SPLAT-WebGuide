.. role:: inputcell
    :class: inputcell
.. role:: interfacecell
    :class: interfacecell
.. role:: button
    :class: button


Working with Technologies
====================================

.. important::
    The interface must be linked to the model before executing any of the steps in this section.
    See :ref:`link_interface`.

A technology in the model is a power-producing unit or a combination of such units or a transmission line with specific parameters such as, maximum capacity, capacity factor, CAPEX, FOM, fuel cost etc.

A technology can be site specific (a specific plant or transmission line with known parameters) or generic (a technology with generalised parameters).
Technologies in SPLAT are classified into four main types:

**1. Existing technologies:** The technologies which are already in place as of the reference year.

**2. Committed technologies:** The technologies which are currently under construction, or whose implementation has been approved. The deployment of these technologies may be considered guaranteed in the model results.

**3. Candidate technologies:** The technologies which may or may not be commissioned in the long term and thus are part of the optimisation process. The characteristics of these projects (size, location, technology, etc.) must be consistent with existing infrastructure, price trends and energy resource potential. 
The model will select them if they show a net benefit to the modelled power system, which implies that building, operating and maintaining them should minimise the total cost of power system expansion.

The SPLAT Africa model used in the Continental Power System Master Plan (CMP) project makes used of energy model "supply regions" (MSR). 
MSR comprises of pre-loaded georeferenced solar PV, solar CSP, wind onshore and offshore supply options designed by IRENA through a systematic geospatial analysis explained in this `paper <https://www.nature.com/articles/s41597-022-01786-5>`_.
These variable renewable energy technologies are also considered as candidate technologies.

**4. Generic technologies:** These technologies are not site specific. They have generalised parameters. Similar to candidate technologies, these technologies are also part of the optimisation process. The model would select these technologies if they show a net benefit to the modelled power system.

The generic technologies are normally set up in a way that they don't come online in reference scenaerios. One of the main motivations to have generic technologies in the model is to make the model tech-agnostic, which in turn increases acceptance among stakeholders.

The Technology tabs are listed at :ref:`technologysheets`

This section describes how to view, add and change technologies using the SPLAT Excel Interface.


.. _view_tech_inputs:

Viewing technology inputs
-----------------------------------

1. In any of the :ref:`technologysheets` (except the tabs containing information of specific zones), enter the scenario to be queried in the cell ``Choose Scenario``

2. Click on :button:`Refresh Sheet`. The technologies and their parameters in the scenario will be shown in the same sheet. Only data for the country(s) loaded (in the ``Main`` sheet) will be displayed.

3. Refer to :ref:`renewable_tech` for steps to retrieve the information of renewable zones (Solar PV, Solar CSP, Onshore Wind, Offshore Wind).

.. _add_tech:

Adding a technology
-------------------------

1. Refresh the sheet :ref:`SpecificTech` for the scenario selected.

2. Add new specific tech name and parameters in the table. Ensure the that technology code is unique and not repeated.

3. Click on :button:`Add New Techs`. A technology is added with parameters from the underlying generic tech.

4. Refresh sheet to see the new technology added. Refresh other sheets before modifying relevant parameters.

.. note::
	Battery and pump storage technologies need to be defined separately in :ref:`Battery&PumpStorage` sheet in SPLAT interface.

.. _rename_tech:

Renaming a technology 
-----------------------------

1. Enter the old and new technology names in :ref:`RenameTechFacility` and click on :button:`Rename Techs in List`. 

2. To confirm that the technology has been renamed, refresh the relevant tabs (``GenericTech`` or ``SpecificTech``) to see the updated names. Multiple technologies can be renamed.

.. image:: /images/technology_rename.PNG

.. _delete_tech:

Deleting a technology
------------------------------

1. Enter the technology names in :ref:`DeleteTechFacility` and click on :button:`Delete Techs in List`. 

2. To confirm that the technology has been deleted, refresh the relevant tabs (``GenericTech`` or ``SpecificTech``) to see the update. Multiple technologies can be deleted.

.. image:: /images/technology_delete.PNG

.. _change_tech:

Changing a technology 
------------------------------

1. In any of the :ref:`technologysheets` (except the tabs containing information of specific zones), click on :button:`Refresh Sheet` to get the data saved in the model for the scenario chosen.

2. Make changes to the technologies in the sheet.

3. Click on :button:`Update Model Data` to update the model with the new data.

.. .. _fuel:

.. Fuel price
.. ---------------

.. 1. In the tab :ref:`fuelprices`, click on :button:`Refresh Sheet` to get the data saved in the model for the scenario and countries chosen.

.. 2. Make changes to the fuel prices in the sheet.

.. 3. Click on :button:`Update Model Data` to update the model with the new data.

.. .. note::
..     1. The fuel price is specified in $/GJ. It is currently not possible to add new fuel supply technologies via the SPLAT interface, this is left for future development (as well as the possibility of specifying limits, which would be needed if one wanted to model a supply curve for a particular fuel).
..     2. If a user specifies values both in the Constant column, as well as under milestone year columns, only the constant value will be used to update the MESSAGE model and the other values will be ignored.

.. .. _tech_cost:

.. Technology costs
.. -----------------------

.. 1. In the tab :ref:`generictechcosts` and :ref:`specifictechcosts`, click on :button:`Refresh Sheet` to get the cost data saved in the model for the scenario and countries chosen.

.. 2. Make changes to the costs (Overnight Cost-$/kW, Fixed O&M Cost-$/kW, Variable O&M Cost-$/MWh) in the sheet.

.. 3. Click on :button:`Update Model Data` to update the model with the new data.

.. .. note::
..     If a user specifies values both in the Constant column, as well as under milestone year columns, only the constant value will be used to update the MESSAGE model and the other values will be ignored.

.. .. _tech_capacity:

.. Capacity Limit
.. ---------------------

.. 1. In the tab :ref:`specificcapacitylimits`, click on :button:`Refresh Sheet` to get the capacity limits saved in the model for the scenario and countries chosen.

.. 2. Make changes to the capacity limits in the sheet.

.. 3. Click on :button:`Update Model Data` to update the model with the new data.

.. .. note::
..     1. There are no capacity limits for generic technologies.
..     2. If a user specifies values both in the Constant column, as well as under milestone year columns, only the constant value will be used to update the MESSAGE model and the other values will be ignored.

.. _renewable_tech:

Defining variable renewable energy technologies
-----------------------------------------------------------------

.. _solar_wind:

Solar PV, CSP, onshore and offshore Wind
+++++++++++++++++++++++++++++++++++++++++++++++++

VRE technologies can be defined in two ways - either as generic technologies or site-specific technologies. Below is an example for adding offshore wind, first as a generic technology, then as zones.

1.	In the :ref:`GenericTech` tab, add technology "XXWDLCO00" (XX being country ID, for e.g. DZ) with tech description "Offshore generic tech". Use add new tech button. The macro will update the underlying files and reload at the end.

2.	Go to :ref:`RenameTechFacility` sheet. Change the newly added offshore techs to appropriate generic tech name i.e. XXWDOC00. The macro will update the underlying files and reload at the end.

3.	Go to :ref:`OffshoreWindZones` sheet. Add new techs in each country. Click on :button:`Add New Techs`. The macro will update the underlying files and reload at the end.

4.	Locate the .tit file of the model and open as excel, it will ask you about delimit parameter. Select comma. The generic wind offshore and newly added offshore zones will have same profiles. Now, got to :ref:`OffshoreWindZones` sheet. Give address to the file that contains the profiles, in the section MSR data file. This will update the zone profiles in .tit file. Currently, the wind offshore generic tech has same profile as wind generic. But remember, wind onshore generic tech has been ousted from model by setting first year=2050

5.	The updated profiles in the .tit file needs to be inserted in model files. Go to :ref:`TimeSlices` sheet, press :button:`Update Files`.

.. _hydro_dam:

Hydro Dam
++++++++++++++

SPLAT characterizes the dam-based hydropower plants by accounting river and dam specific resource conditions. Their dispatch is optimized while synergizing with other renewable supply options (i.e. the solar photovoltaic, wind, concentrated solar power and run of river based hydropower) that are given fixed and exogenously determined generation profiles. 

The dam hydropower plants are represented as a combination of three elements: river, dam and a generator. The river and the generator are inserted as ‘technology’ while the dam is inserted as a ‘storage’ (for details, see MESSAGE manual). As explained ahead, the SPLAT naming convention requires these three elements to carry a common name but different prefixes. 

The river technology is characterized with the exogenously determined maximum monthly inflow assumption in MW units and a normalized monthly flow profile. Similarly, the dam storage is characterized with a maximum volume in MWyr units. These assumptions are mainly derived from 'IRENA’s AfREP Hydropower database <https://www.irena.org/publications/2021/Dec/African-Renewable-Electricity-Profiles-Hydropower>'. In rare cases, when refinements are necessary, the SPLAT user has the ability to modify these characteristics. However, in normal use case, the user is required to just review/revise the generator side characteristics only (see :ref:`tech_sheet`).

The ``SpecificTechHydroDams`` sheet manipulates the hydro dams in the model.

1. Click on :button:`Refresh Sheet` button to extract the technologies that belong to the `TechSetL2`: `Large Hydro Dams`.

2. :button:`Create River Tech+Storage Constraint` button adds a technology and a storage constraint for each dam.

A new dummy technology for each hydro station with Dam is added to model the river inflows to the dam. The naming convention of the dummy technology is XXRIDM_rivername, for example CMRIDM_LAGDO (using LAGDO as an example).  The output is set to the existing dummy elc energy form.

A new storage constraint is added, example D_LAGDO with short name DXXX. The storage constraint is linked to CMRIDM_LAGDO with +1 coefficient, so each MWyr flow from CMRIDM_LAGDO increases the storage content by 1 MWyr.

The storage constraint is linked to CMHYDM_LAGDO with -1 coefficient (meaning that each MWyr flow from CMHYDM_LAGDO decreases the storage content by 1 MWyr). It would be possible in theory to do cascade modelling by linking the output of upstream plants to storage constraints downstream (rather than a river technology). The coefficients would have to be scaled by the relative "Energy per unit volume (MJ/m3)" of the upstream and downstream plants. This functionality will need a revisit as a new development task if there is a pressing need for it.

The user has to specify 2 parameters, whose values can be calculated in the right-most table and copy pasted.

3. Once this is done the user can click on :button:`Update Model Data`:

The capacity is set to max flow (in MW, m3/s max flow scaled by design flow). The capacity is specified as a capacity limit on the River Technology (bdi) .

The storage constraint max volume is set to Max volume in MWyr as per table.

The user then has to add a time series in the csv file under the tech CMRIDM_LAGDO and :button:`Update Timeslices` in the ``Timeslice`` sheet. The values in the csv file must be monthly average flow divided by "max flow" that was used to set the "River Capacity", using the same max flow value regardless of the scenario.
If the user wants to simulate different rainfall scenarios without a full time series, they could use plant factor to scale up or down the profile in the ``SpecificTech`` sheet. It is currently not possible to specify a different seasonal profile by scenario, but this feature is on the todo list for the near future.

.. _batteries:

Batteries and Pump Storage
++++++++++++++++++++++++++++++++++++

Batteries and pump storage technologies can be added and modified in the same way through the SPLAT excel interface.

1. In ``Battery&PumpStorage`` sheet: create the technology with techname convention: xxELSTyyyy for a battery or xxELSTPSyyyy for pump storage, where xx is country code, and yyyy is site description. (For example, ZAELSTPSDrakensberg)

2. :button:`Reload Global`

3. In the same ``Battery&PumpStorage`` sheet click :button:`Refresh` and then specify storage hours and cycle efficiency

4. In the ``TechSpecific`` sheets specify the other usual parameters hc, bdi, inv etc....

.. .. _csp:

.. Concentrated Solar Power (CSP)
.. ++++++++++++++++++++++++++++++++++++++++++

.. Refer to steps in :ref:`solar_wind`. (Improvements upcoming)

.. .. _transmission_distribution:

.. Transmission and Distribution
.. ---------------------------------------

.. The :ref:`transmission` and :ref:`distribution` sheets are used to review or modify transmission and distribution technologies parameters as per the definitions in the ``TechnologySets`` sheet (see section below).

.. .. note::
..     1. If the user wants to model with "sent-out" demand (see :ref:`demand`), transmission efficiency must be set to 100%, and investment costs set to a small value. In the default configuration there is no distribution technology specified for "Sent-out" electricity.

..     2. If a user specifies values both in the Constant column, as well as under milestone year columns, only the constant value will be used to update the MESSAGE model and the other values will be ignored.

.. .. _interconnection:

.. Interconnection
.. -----------------------

.. The :ref:`interconnectors` sheet is used to review and update cross-border interconnector parameters.

.. At a minimum the two interconnecting countries (which must be active) must be specified to view the interconnections between them. 

.. _tech_naming:

Technology naming in the SPLAT model
--------------------------------------------------

The naming convention of various technologies including technology set levels 1 and 2, and generic technologies are given in the table below.
The "??" in the technology code in the front refers to the two-letter country code (alpha-2). And the * provides further information about the technology.

The naming of technology set level 1 follow the following conventions in the SPLAT model:

.. csv-table:: 
    :file: csv_file/level1sets_sheet.csv
    :header-rows: 1

The naming of technology set level 2 follow the following conventions in the SPLAT model:

.. csv-table:: 
    :file: csv_file/level2sets_sheet.csv
    :header-rows: 1

The naming convention of generic technologies is given in the table below:

.. csv-table:: 
    :file: csv_file/generictechcodes_sheet.csv
    :header-rows: 1

.. _country_code:

Country Code in the SPLAT model
-------------------------------------------

The two-letter or three-letter country codes used in the SPLAT model are based on `ISO 3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1>`_ standard.