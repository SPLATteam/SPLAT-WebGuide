.. role:: inputcell
    :class: inputcell
.. role:: interfacecell
    :class: interfacecell
.. role:: button
    :class: button

Description of Sheets
=====================

.. _main:

Main
-----

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
--------------

This section contains the list of parameters (along with parameter code, their unit and definitions) present in each input sheet in the SPLAT interface.

.. note::
    1. The parameter values refer to the value of the parameter fand the given country fand the given scenario and fand the given year(s).
    2. If there is no year mentioned in the input sheet, then the value is constant for all years.
    3. If the input sheets contain placeholders only fand specific years, then the values of the parameter fand the years in between are linearly interpolated.
    4. Costs are provided in terms of base year values (2019 as of now).

.. _demand_sheet:

Demand
+++++++++++++++++++
    
.. csv-table::
    :file: csv_file/demand_sheet.csv
    :header-rows: 1
    :widths: 20 10 50

.. _peakdemand_sheet:

PeakDemand
+++++++++++
.. csv-table::
    :file: csv_file/peakdemand_sheet.csv
    :header-rows: 1
    :widths: 20 10 50

.. _t&d_sheet:

Transmission and Distribution
++++++++++++++++++++++++++++++

.. csv-table::
    :file: csv_file/t&d_sheet.csv
    :header-rows: 1
    :widths: 20 10 50

.. note:: 
    For distribution, values need to be entered for urban, rural, industry and commerce distribution types.

.. _fuelprices_sheet:

FuelPrices
+++++++++++++++++++
.. csv-table:: 
    :file: csv_file/fuelprices_sheet.csv
    :header-rows: 1
    :widths: 20 10 50

.. _tech_sheet:

GenericTech and SpecificTech
+++++++++++++++++++

The ``GenericTech`` sheet displays generic technology parameters that are constant over the model horizon

The ``SpecificTech`` sheet is used to review and update site specific power generation technology parameters that don’t vary from year to year.
The ``SpecificTech`` sheet has an extra button: :button:`Add missing Tech`, which allows the user to add new site specific technology to the MESSAGE model that is linked. Currently this technology makes the addition by copying the technology parameters of a generic technology of the same technology type as specified by the first 6 characters in the technology name. A new technology will be automatically added to all active scenarios. A MESSAGE technology code is created automatically based on the input and output commodities (as specified by the associated generic technology) and the already existing technologies having the same inputs and outputs.
Once a new technology is added, its parameters must be updated using the :button:`Update Model Data` button.

.. csv-table:: 
    :file: csv_file/tech_sheet.csv
    :header-rows: 1
    :widths: 20 20 10 50

.. note:: 
    1. The profiles/load curves are calculated by SPLAT based on the hourly values (8760) present in *.tit file in data folder. They are stored in the adb, ldb and ldr files. The reason for not having them in the spreadsheet is that they vary depending on the load region/timeslice definition (e.g. large model/small model) and are would be very difficult to manage effectively in a spreadsheet.

    2. ** Parameters relevant to ``SpecificTech`` sheet only.

.. _techcosts_sheet:

GenericTechCosts and SpecificTechCosts
+++++++++++++++++++

These sheets display the cost parameters that are either constant or change over the model horizon.

.. csv-table:: 
    :file: csv_file/techcosts_sheet.csv
    :header-rows: 1
    :widths: 20 10 50

.. _specifictechhydrodams_sheet:

SpecificTechHydroDams
+++++++++++++++++++

This sheet displays site-specific technology parameters that are specific to hydro plants with storage (dams).
The ``SpecificTechHydroDams`` sheet manipulates the hydro dams in the model.
The :button:`Refresh Sheet` button extracts the technologies that belong to the `TechSetL2`: `Large Hydro Dams`.
And the :button:`Create River Tech+Storage Constraint` button adds a technology and a storage constraint for each dam.
The :button:`Update Model Data` updates the user input data.

.. csv-table:: 
    :file: csv_file/specifictechhydrodams_sheet.csv
    :header-rows: 1
    :widths: 20 20 10 50

.. _battery&pumpstorage_sheet:

Battery&PumpStorage
+++++++++++++++++++

.. csv-table:: 
    :file: csv_file/battery&pumpstorage_sheet.csv
    :header-rows: 1
    :widths: 20 20 10 50

.. _interconnectors_sheet:

Interconnectors
+++++++++++++++++++

.. csv-table:: 
    :file: csv_file/interconnectors_sheet.csv
    :header-rows: 1
    :widths: 20 20 10 50

.. _caplimits_sheet:

SpecificCapacityLimits and InterconnectorsCapLimits
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :file: csv_file/caplimits_sheet.csv
    :header-rows: 1
    :widths: 20 10 50

.. _vrezones_sheet:

PVZones, WindZones, OffshoreWindZones, CSP6hrZones and CSP12hrZones
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
.. ++++++

.. Displays all demand series in the model, including total "Sent Out" (i.e. Secondary, or before transmission & distribution) demand and Final demand by sector

.. .. _peakdemand:

.. PeakDemand
.. ++++++++++

.. Displays Peak Demand series in MW in the model, including total "Sent Out" (i.e. Secondary, or before transmission & distribution) demand and Final demand by sector

.. .. _fuelprices:

.. FuelPrices
.. ----------

.. Displays fuel prices used in the model

.. .. _technologysheets:

.. Technology sheets
.. ------------------

.. .. _generictech:

.. GenericTech
.. +++++++++++

.. Displays generic technology parameters that are constant over the model horizon

.. .. _generictechcosts:

.. GenericTechCosts
.. ++++++++++++++++

.. Displays generic technology cost parameters that are either constant or change over the model horizon (e.g. CAPEX, FOM, VOM)

.. .. _specifictec:

.. SpecificTech
.. +++++++++++++

.. Displays site-specific technology parameters that are constant over the model horizon


.. The ``SpecificTech`` sheet is used to review and update Site specific power generation technology parameters that don’t vary from year to year.

.. The SpecificTech sheet has an extra button: :button:`Add missing Tech`, which allows the user to add new site specific technology to the MESSAGE model that is linked. Currently this technology makes the addition by copying the technology parameters of a generic technology of the same technology type as specified by the first 6 characters in the technology name. A new technology will be automatically added to all active scenarios. A MESSAGE technology code is created automatically based on the input and output commodities (as specified by the associated generic technology) and the already existing technologies having the same inputs and outputs.

.. Once a new technology is added, its parameters must be updated using the :button:`Update Model Data` button.



.. .. _specifictechhydrodams:

.. SpecificTechHydroDams
.. +++++++++++++++++++++

.. Displays site-specific technology parameters that are specific to hydro plants with storage (dams)

.. The ``SpecificTechHydroDams`` sheet manipulates the hydro dams in the model.

.. :button:`Refresh Sheet` button extracts the technologies that belong to the `TechSetL2`: `Large Hydro Dams`.

.. :button:`Create River Tech+Storage Constraint` button adds a technology and a storage constraint for each dam.

.. :button:`Update Model Data` updates the user input data.


.. .. _specifictechcosts:

.. SpecificTechCosts
.. ++++++++++++++++++

.. Displays site-specific technology cost parameters that are either constant or change over the model horizon (e.g. CAPEX, FOM, VOM)

.. .. _specificcapacitylimits:

.. SpecificCapacityLimits
.. +++++++++++++++++++++++

.. Displays site-specific technology capacity limits that are either constant or change over the model horizon

.. .. _batterystorage:

.. BatteryStorage
.. ++++++++++++++

.. Displays Battery Storage Parameters

.. .. _pvzones:

.. PVZones
.. ++++++++

.. Displays PV Zones Data

.. .. _windzones:

.. WindZones
.. ++++++++++

.. Displays Wind Zones Data

.. .. _offshorewindzones:

.. OffshoreWindZones
.. +++++++++++++++++

.. Displays OffshoreWind Zones Data

.. .. _csp6hrzones:

.. CSP6hrZones
.. ++++++++++++

.. Displays CSP 6hr Zones Data

.. .. _csp12hrzones:

.. CSP12hrZones
.. ++++++++++++

.. Displays CSP 12hr Zones Data

.. .. _interconnectors:

.. Interconnectors
.. +++++++++++++++

.. Displays regional interconnector parameters

.. .. _transmission:

.. Transmission
.. ++++++++++++

.. Displays transmission network parameters by country

.. .. _distribution:

.. Distribution
.. ++++++++++++

.. Displays distribution network parameters by country and sector

.. _constraint_sheets:

Constraint Sheets
-----------------

This section describes the different constraints (including their equations and parameters) present in different Constraint sheets in SPLAT.

.. _rmconstraint_sheet:

Reserve Margin Constraint
+++++++++++++++++++++++++

Reserve margin (RM) is the margin of firm capacity required above peak demand. It ranges usually between 10 to 25% of peak capacity.
The constraint equation used in this sheet is as follows:

:math:`$\sum (Capacity_PP \times RM_LHS) > 0$`

The transmission technology is also used to calculate peak demand, and their RM coefficient is considered negative because of their nature of transmitting rather than generating activity.

.. csv-table::
    :file: csv_file/rmconstraint_sheet.csv
    :header-rows: 1
    :widths: 20 20 10 50

.. _reportgen_annual:

ReportGen-Annual
-----------------

This sheet allows to run the model and get results in annual resolution.
The steps are described in :ref:`run_model`.

.. _reportgen_profiles:

ReportGen-Profiles
-------------------

This sheet allows to generate Sub-Annual (Profiles) results file. The steps are described in :ref:`extract_results`.

.. _timeslices:

TimeSlices
-----------

Displays timeslice definitions (load regions) used in model
