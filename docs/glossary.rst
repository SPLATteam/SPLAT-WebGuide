.. role:: inputcell
    :class: inputcell
.. role:: interfacecell
    :class: interfacecell
.. role:: button
    :class: button

Description of Sheets
=============================

.. _main:

Main
-------

Set the model path, reload model data to memory, and select active countries for querying

:inputcell:`Model Folder`       path of the MESSAGE model to be connected to the SPLAT interface

:inputcell:`Main Region`        name of the MESSAGE model to be connected to the SPLAT interface

:inputcell:`Region Active?`     list of sub-regions (countries) to be loaded into memory

:inputcell:`Scenarios to Load`      list of currently specified scenarios in the main region, and to specify the scenarios to be loaded into memory

:interfacecell:`Country Name`       country codes in the MESSAGE model

:interfacecell:`Description`        country names expanded

:interfacecell:`Power Pool`         the powerpool a country belongs to

:interfacecell:`TimeSlices/Load Regions`        number of time slices modelled per year

:interfacecell:`# Demands`      number of demand components

:interfacecell:`# Technologies`     number of technologies in country

:interfacecell:`# Constraints`      number of constraints in country

:interfacecell:`Scenarios`      name of scenarios

:interfacecell:`Discount Rate`      discount rate of technologies

:button:`Reload Global`     import model data stored in adb and ldb files into memory, perform various calculations.

:button:`Refresh all Sheets`        refresh data sheets (yellow sheets) for reloaded subregions and scenarios

:button:`Save all Scenario Files using SPLAT formatting`        save all model (adb and ldb) files using excel-SPLAT formatting for selected subregions (use this after making a change with MESSAGE interface)
If this button is pressed the MAINa ldb files will also be updated if MAINa is selected, to exclude interconnectors for subregions that are not selected below.

.. _input_sheets:

Input Sheets
------------------

This section contains the list of parameters (along with parameter code, their unit and definitions) present in each input sheet in the SPLAT interface.

.. note::
    1. The parameter values refer to the value of the parameter for the given country for the given scenario for the given year(s).
    2. Time series data can sometimes be inserted for small number of years and SPLAT will interpolate it linearly for missing years.
    3. All costs must be given in common base year (e.g. CMP model adopted 2019 base year.)
    
.. _demand_sheet:

Demand
+++++++++++++++++++++++++
    
.. csv-table::
    :file: csv_file/demand_sheet.csv
    :header-rows: 1
    :widths: 20 10 50

.. _peakdemand_sheet:

PeakDemand
+++++++++++++++
.. csv-table::
    :file: csv_file/peakdemand_sheet.csv
    :header-rows: 1
    :widths: 20 10 50

.. _t&d_sheet:

Transmission and Distribution
++++++++++++++++++++++++++++++++++++++++++

The :ref:`transmission` and :ref:`distribution` sheets are used to review or modify transmission and distribution technologies parameters as per the definitions in the ``TechnologySets`` sheet (see section below).

.. note::
    1. If the user wants to model with "sent-out" demand (see :ref:`demand`), transmission efficiency must be set to 100%, and investment costs set to a small value. In the default configuration there is no distribution technology specified for "Sent-out" electricity.

    2. If a user specifies values both in the Constant column, as well as under milestone year columns, only the constant value will be used to update the MESSAGE model and the other values will be ignored.

.. csv-table::
    :file: csv_file/t&d_sheet.csv
    :header-rows: 1
    :widths: 20 10 50

.. note:: 
    For distribution, values need to be entered for urban, rural, industry and commerce distribution types.

.. _fuelprices_sheet:

FuelPrices
+++++++++++++++++++++++++
.. csv-table:: 
    :file: csv_file/fuelprices_sheet.csv
    :header-rows: 1
    :widths: 20 10 50

.. _tech_sheet:

GenericTech and SpecificTech
+++++++++++++++++++++++++

The ``GenericTech`` sheet displays generic technology parameters.

The ``SpecificTech`` sheet is used to review and update site specific power generation technology parameters that are constant over time.
The ``SpecificTech`` sheet has an extra button: :button:`Add missing Tech`, which allows the user to add new site specific technology to the MESSAGE model that is linked. 
Currently this action makes the addition by copying the technology parameters of a generic technology of the same technology type as specified by the first 6 characters in the technology name. A new technology will be automatically added to all active scenarios. A MESSAGE technology code is created automatically based on the input and output commodities (as specified by the associated generic technology) and the already existing technologies having the same inputs and outputs.
Once a new technology is added, its parameters must be updated using the :button:`Update Model Data` button.

.. csv-table:: 
    :file: csv_file/tech_sheet.csv
    :header-rows: 1
    :widths: 20 20 10 50
    :class: longtable

.. note:: 
    1. The profiles/load curves are calculated by SPLAT based on the hourly values (8760) present in *.tit file in data folder. They are stored in the adb, ldb and ldr files. The reason for not having them in the spreadsheet is that they vary depending on the load region/timeslice definition (e.g. large model/small model) and are would be very difficult to manage effectively in a spreadsheet.

    2. ** Parameters relevant to ``SpecificTech`` sheet only.

.. _techcosts_sheet:

GenericTechCosts and SpecificTechCosts
+++++++++++++++++++++++++

These sheets display the cost parameters that are either constant or change over the model horizon.

.. csv-table:: 
    :file: csv_file/techcosts_sheet.csv
    :header-rows: 1
    :widths: 20 10 50

.. _specifictechhydrodams_sheet:

SpecificTechHydroDams
+++++++++++++++++++++++++

The approach to define hydro dam technologies in SPLAT is given in :ref:`hydro_dam` section. The parameters used to define them are given below:

.. csv-table:: 
    :file: csv_file/specifictechhydrodams_sheet.csv
    :header-rows: 1
    :widths: 20 20 10 50

.. _battery&pumpstorage_sheet:

Battery&PumpStorage
+++++++++++++++++++++++++

The approach to define battery and pump storage technologies in SPLAT is given in :ref:`batteries` section. The parameters used to define them are given below:

.. csv-table:: 
    :file: csv_file/battery&pumpstorage_sheet.csv
    :header-rows: 1
    :widths: 20 20 10 50

.. _interconnectors_sheet:

Interconnectors
+++++++++++++++++++++++++

The :ref:`interconnectors` sheet is used to review and update cross-border interconnector parameters. At a minimum the two interconnecting countries (which must be active) must be specified to view the interconnections between them. 

.. csv-table:: 
    :file: csv_file/interconnectors_sheet.csv
    :header-rows: 1
    :widths: 20 20 10 50

.. _caplimits_sheet:

SpecificCapacityLimits and InterconnectorsCapLimits
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :file: csv_file/caplimits_sheet.csv
    :header-rows: 1
    :widths: 20 10 50

.. _vrezones_sheet:

PVZones, WindZones, OffshoreWindZones, CSP6hrZones and CSP12hrZones
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The approach to define VRE technologies (solar PV, CSP, onshore and offshore wind) is given in :ref:`solar_wind` section.
The parameters needed to define VRE zones are stated in the table below:

.. csv-table:: 
    :file: csv_file/vrezones_sheet.csv
    :header-rows: 1
    :widths: 20 20 10 50

.. note::
    1. Latitute and Longitude data can be stored in the adb files together with the rest of the model input data. It is not used by SPLAT or MESSAGE for anything, but it can be used by results viewers for display on maps (e.g. in Tableau). 

    2. For offset investment and multiplier investment parameters, one has to remember to use the pull down option "Reset Investment" in cell F6, when generic costs are updated for whatever reason, or before an update was made in raw MSR data, before re-applying the "Offset Investment".

    3. The multiplier investment (according to turbine class) parameter is in ``WindZones`` sheet only. This categorization doesn't apply to offshore as it is assumed all offshore wind turbines are of the same class.

.. .. _demand:

.. Demand
.. ++++++++

.. Displays all demand series in the model, including total "Sent Out" (i.e. Secondary, or before transmission & distribution) demand and Final demand by sector

.. .. _peakdemand:

.. PeakDemand
.. ++++++++++++++

.. Displays Peak Demand series in MW in the model, including total "Sent Out" (i.e. Secondary, or before transmission & distribution) demand and Final demand by sector

.. .. _fuelprices:

.. FuelPrices
.. --------------

.. Displays fuel prices used in the model

.. .. _technologysheets:

.. Technology sheets
.. ------------------------

.. .. _generictech:

.. GenericTech
.. +++++++++++++++

.. Displays generic technology parameters that are constant over the model horizon

.. .. _generictechcosts:

.. GenericTechCosts
.. ++++++++++++++++++++++

.. Displays generic technology cost parameters that are either constant or change over the model horizon (e.g. CAPEX, FOM, VOM)

.. .. _specifictec:

.. SpecificTech
.. +++++++++++++++++

.. Displays site-specific technology parameters that are constant over the model horizon


.. The ``SpecificTech`` sheet is used to review and update Site specific power generation technology parameters that don’t vary from year to year.

.. The SpecificTech sheet has an extra button: :button:`Add missing Tech`, which allows the user to add new site specific technology to the MESSAGE model that is linked. Currently this technology makes the addition by copying the technology parameters of a generic technology of the same technology type as specified by the first 6 characters in the technology name. A new technology will be automatically added to all active scenarios. A MESSAGE technology code is created automatically based on the input and output commodities (as specified by the associated generic technology) and the already existing technologies having the same inputs and outputs.

.. Once a new technology is added, its parameters must be updated using the :button:`Update Model Data` button.



.. .. _specifictechhydrodams:

.. SpecificTechHydroDams
.. +++++++++++++++++++++++++++++

.. Displays site-specific technology parameters that are specific to hydro plants with storage (dams)

.. The ``SpecificTechHydroDams`` sheet manipulates the hydro dams in the model.

.. :button:`Refresh Sheet` button extracts the technologies that belong to the `TechSetL2`: `Large Hydro Dams`.

.. :button:`Create River Tech+Storage Constraint` button adds a technology and a storage constraint for each dam.

.. :button:`Update Model Data` updates the user input data.


.. .. _specifictechcosts:

.. SpecificTechCosts
.. ++++++++++++++++++++++++

.. Displays site-specific technology cost parameters that are either constant or change over the model horizon (e.g. CAPEX, FOM, VOM)

.. .. _specificcapacitylimits:

.. SpecificCapacityLimits
.. +++++++++++++++++++++++++++++++

.. Displays site-specific technology capacity limits that are either constant or change over the model horizon

.. .. _batterystorage:

.. BatteryStorage
.. ++++++++++++++++++

.. Displays Battery Storage Parameters

.. .. _pvzones:

.. PVZones
.. ++++++++++

.. Displays PV Zones Data

.. .. _windzones:

.. WindZones
.. ++++++++++++++

.. Displays Wind Zones Data

.. .. _offshorewindzones:

.. OffshoreWindZones
.. +++++++++++++++++++++++

.. Displays OffshoreWind Zones Data

.. .. _csp6hrzones:

.. CSP6hrZones
.. ++++++++++++++++

.. Displays CSP 6hr Zones Data

.. .. _csp12hrzones:

.. CSP12hrZones
.. ++++++++++++++++

.. Displays CSP 12hr Zones Data

.. .. _interconnectors:

.. Interconnectors
.. +++++++++++++++++++++

.. Displays regional interconnector parameters

.. .. _transmission:

.. Transmission
.. ++++++++++++++++

.. Displays transmission network parameters by country

.. .. _distribution:

.. Distribution
.. ++++++++++++++++

.. Displays distribution network parameters by country and sector

.. _constraint_sheets:

Constraint Sheets
-----------------------

Constraints are linear mathematical equations applicable across several technologies (power plants, storage, transmission, etc. 
These are user-defined relations to guide a model based on scenario narratives.
In MESSAGE, a constraint is defined as a sum-product of a coefficient and variable with user-defined upper or lower limits as shown below: 

.. image:: /images/constraint_form.PNG

This section describes the different constraints (including their equations and parameters) present in different Constraint sheets in SPLAT.

.. _constraintlist_sheet:

ConstraintList
++++++++++++++++++

This sheet contains the list of all the constraints in the model which are defined in the following sheets.

.. _buildlimconstraint_sheet:

PVAnnualBuildLim and WindAnnualBuildLim
+++++++++++++++++++++++++++++++++++++++++++++++++++++

These two sheets are used to set annual build limits for solar PV and wind onshore respectively.
The equation(s) used in the sheet is as given below:

.. https://quicklatex.com/
.. https://www.overleaf.com/learn/latex/Integrals%2C_sums_and_limits
:math:`\sum\limits_{PV}New\, Capacity\, in\, year\, t_{PV} <=  PVBR\, in\, year\, t`

:math:`\sum\limits_{Wind}New\, Capacity\, in\, year\, t_{Wind} <=  WindBR\, in\, year\, t`

The equation suggests that the new installed capacity of solar PV or wind for year t should be below the build rates defined in this sheet. 

The parameters used in this sheet are as follows:

.. csv-table::
    :file: csv_file/buildlimconstraint_sheet.csv
    :header-rows: 1
    :widths: 20 20 10 50

.. note::
    The target (% of peak demand), Min and Max values are set as design decision/suggestion. These values could be made larger or smaller. 
    One can also make country specific coefficients by overwriting the formulas for upper limits.

.. _rmconstraint_sheet:

ReserveMarginConstraint
+++++++++++++++++++++++++++++++

In a power system, generation must always equal consumption.
When the balance is disrupted, it can lead to outages and complete black outs.
There are many events that might disturb the balance (many of them are stochastic/predictable with probability) such as planned maintenance, unplaneed stops, changes/variations in demand, and changes in supply.
Therefore, reserves are needed in the system to make sure that power demand is always met.

Based on the response (reaction time), reserved can be classified as:

i. Primary reserves: part of operational (running) or fast to activate capacity available to immediately (in seconds) for cover for disturbances.

ii. Secondary reserve: can be operating or cold (not operating) capacity to be activated in minutes (after initial disturbance and activation of primary reserve, secondary reserve is activated, and units are redispatched so to re-activate primary reserve capabilities.)

iii. Tertiary reserve: these are usually back-up units that can be activated in minutes/hours to allow reactivation of secondary reserve capabilities.

In MESSAGE framework, all information about current and future power system is assumed to be known (with 100% certainty), i.e., not stochastic, therefore, production pattern decisions always have to deterministic.
When modelling long term development of a power system, an analyst should make sure that the future capacity is sufficient to cover demand during critical periods (usually during peak hours) and to cover other operational needs (e.g., maintenance).

.. note::
    1. There's a lot of stochastic behavior in a real system that cannot be captured in the same way within the model.
    2. It is possible to run analysis with various demand and supply availability patterns and model extreme operational conditions.

Reserve margin is the margin of firm capacity that is required above peak demand/load. It ranges usually between 10% to 25% of peak load.
For e.g., if a region has 12 GW of firm capacity and 10 GW of peak demand, the reserve margin would be 20%.

Reserve Margin (RM) = (Firm Capacity - Peak Demand) / Peak Demand

The representation of system reserve in MESSAGE modelling framework is as shown below:

.. image:: /images/system_reserve_in_message.PNG

The constraint equation used in the ``ReserveMarginConstraint`` sheet is as follows:

:math:`\sum\limits_{PP}(CapacityCredit_{PP} \times Capacity_{PP}) - \dfrac{1+RM}{1-LS} \cdot Capacity_{Ptnd} \geq 0`

where,

PP refers to all applicable power plants.

CapacityCredit_PP and Capacity_PP refer to capacity credit and installed capacity of power plant.

RM = Reserve Margin

Capacity_Pt&d = Size (MW) of transmission and distribution grid used as proxy of peak demand

LS = Transmission Losses

"ConCap_RM" stands for Coefficient applicable on Capacity (MW) and associated to Reserve Margin constraint.

.. csv-table::
    :file: csv_file/rmconstraint_sheet.csv
    :header-rows: 1
    :widths: 20 20 10 50

.. note::
    Unlike build rate constraint, SPLAT requires the user to insert reserve margin constraint as a non time-series constraint i.e., a constant upper or lower limit applied on all years in modelling horizon.
    
.. _localreconstraint_sheet:

LocalREConstraint
+++++++++++++++++++++++

Different countries or regions can have target of achieving certain minimum share RE in the the total power generation by certain year.
In the ``LocalREConstraint`` sheet, the minimum "target" share of RE (more specifically VRE) technologies in the total power generation is set as a constraint in the model for different years.
The equation representing this constraint can be represented below:

vres_gen >= target_vres_share * total_gen

vres_gen - target_vres_share * total_gen >= 0

vres_gen - target_vres_share * (vres_gen + other_gen) >= 0

vres_gen - target_vres_share * vres_gen - target_vres_share * other_gen >=0

(1 - target_vres_share) * vres_gen - target_vres_share * other_gen >= 0

where,

vres_gen = generation from VRE technology

vres_share = share of VRE in total generation (total_gen) which is set as the minimum target share by a country or region

other_gen = generation from non-VRE technologies

"ConAct_RE" refers to the coefficient of Activity/Generation (GWh) of a power plant technology.

.. csv-table::
    :file: csv_file/localreconstraint_sheet.csv
    :header-rows: 1
    :widths: 20 20 10 50


.. _co2constraint_sheet:

CO2Constraint:
++++++++++++++++++

The CO2 emissions constraints are set in more ambitious scenarios.
In this sheet, the reduction target for CO2 emissions for different years is set relative to a specific reference scenario.
This in turn sets the upper limit on the CO2 emissions from power generation from different technologies.
The constraint equation used in the model is as shown below:

:math:`\sum\limits_{PP}CO2_{PP, t} <= MaxCO2_t`

where,

LHS represents the sum of CO2 emissions from power sector in year t.

RHS represents the maximum limit of CO2 emissions from power sector in same year t.

.. csv-table::
    :file: csv_file/co2constraint_sheet.csv
    :header-rows: 1
    :widths: 20 10 50


.. _reportgen_annual:

ReportGen-Annual
-----------------------

This sheet allows to run the model and get results in annual resolution.
The steps are described in :ref:`run_model`.

.. _reportgen_profiles:

ReportGen-Profiles
-------------------------

This sheet allows to generate Sub-Annual (Profiles) results file. The steps are described in :ref:`extract_results`.

.. _timeslices:

TimeSlices
---------------

Displays timeslice definitions (load regions) used in model
