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

::inputcell:`Model Folder`:       path of the MESSAGE model to be connected to the SPLAT interface
::inputcell:`Main Region`:        name of the MESSAGE model to be connected to the SPLAT interface
::inputcell:`Region Active?`:     list of sub-regions (countries) to be loaded into memory
::inputcell:`Scenarios to Load`:      list of currently specified scenarios in the main region, and to specify the scenarios to be loaded into memory
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


.. _demandsheets:

Demand sheets
--------------

.. _demand:

Demand
++++++

Displays all demand series in the model, including total "Sent Out" (i.e. Secondary, or before transmission & distribution) demand and Final demand by sector

.. _peakdemand:

PeakDemand
++++++++++

Displays Peak Demand series in MW in the model, including total "Sent Out" (i.e. Secondary, or before transmission & distribution) demand and Final demand by sector

.. _fuelprices:

FuelPrices
----------

Displays fuel prices used in the model

.. _technologysheets:

Technology sheets
------------------

.. _generictech:

GenericTech
+++++++++++

Displays generic technology parameters that are constant over the model horizon

.. _generictechcosts:

GenericTechCosts
++++++++++++++++

Displays generic technology cost parameters that are either constant or change over the model horizon (e.g. CAPEX, FOM, VOM)

.. _specifictec:

SpecificTech
+++++++++++++

Displays site-specific technology parameters that are constant over the model horizon

.. _specifictechhydrodams:

SpecificTechHydroDams
+++++++++++++++++++++

Displays site-specific technology parameters that are specific to hydro plants with storage (dams)

.. _specifictechcosts:

SpecificTechCosts
++++++++++++++++++

Displays site-specific technology cost parameters that are either constant or change over the model horizon (e.g. CAPEX, FOM, VOM)

.. _specificcapacitylimits:

SpecificCapacityLimits
+++++++++++++++++++++++

Displays site-specific technology capacity limits that are either constant or change over the model horizon

.. _batterystorage:

BatteryStorage
++++++++++++++

Displays Battery Storage Parameters

.. _pvzones:

PVZones
++++++++

Displays PV Zones Data

.. _windzones:

WindZones
++++++++++

Displays Wind Zones Data

.. _offshorewindzones:

OffshoreWindZones
+++++++++++++++++

Displays OffshoreWind Zones Data

.. _csp6hrzones:

CSP6hrZones
++++++++++++

Displays CSP 6hr Zones Data

.. _csp12hrzones:

CSP12hrZones
++++++++++++

Displays CSP 12hr Zones Data

.. _interconnectors:

Interconnectors
+++++++++++++++

Displays regional interconnector parameters

.. _transmission:

Transmission
++++++++++++

Displays transmission network parameters by country

.. _distribution:

Distribution
++++++++++++

Displays distribution network parameters by country and sector

.. _reportgen_annual:

ReportGen-Annual
-----------------

Generate Annual Results File

.. _reportgen_profiles:

ReportGen-Profiles
-------------------

Generate Sub-Annual (Profiles) Results File

.. _timeslices:

TimeSlices
___________

Displays timeslice definitions (load regions) used in model

RenameTechFacility: This sheet is used to change the technology name of selected technologies. Note that new Technology names should not be longer than 40 characters.

DeleteTechFacility: This sheet is used to delete selected technologies from the linked MESSAGE model

Constraints List (work in Progress)

TechConstraintCoeffs (work in Progress)

EForms


Years

Scenarios (Work in progress – Use MESSAGE interface for now)

QueryDemand

QueryTech

Load Calibration (still in development)

DemandProj
