.. role:: inputcell
    :class: inputcell
.. role:: interfacecell
    :class: interfacecell
.. role:: button
    :class: button

Defining Time
==================

.. important::
    The interface must be linked to the model before executing any of the steps in this section.
    See :ref:`link_interface`.

The ``Timeslices (Load Regions)`` sheet allows the user to see what load regions are in the model. It also allows user to select the timezone to run the model with. To make changes to the load region definition requires the demand and profile data to be provided in a specified folder as per specifications outlined later in this document.

Note that currently the interface does not support multiple day types (e.g. weekday vs weekends), although this will be added in future versions of the interface.

The user can review the load regions definition by clicking on the :button:`Show TS in memory` button.

.. _time_zones:

Defining time zones and granularity
-------------------------------------------------

1. Add local time zone information to regid_AllRegions.tit (relative to UTC).

2. In the ``Timeslices (Load Regions)`` sheet, select one of the predefined configurations and the time zone of the model

.. note::

    There are 4 pre-defined Load Region configurations in the interface:

    - Large model: 30 time-slices/load regions (3 seasons each with 10 blocks)

    - Small model: 10 time-slices/load regions (3 season, 2 with 3 blocks, 1 with 4 blocks)

    - Small model V2: 10 time-slices/load regions (1 season with 10 blocks)

    - Very small model: 3 time-slices/load regions (1 season with 3 blocks)

3. Update the timeslice definitions in the model by clicking the :button:`Update files` button. This will:

    -	Update the timeslice definitions in the adb, ldb and ldr files

    -	Shift the capacity factor time series and the demand time series from the regions' local time zones to the model time zone selected.

    -	Update the RE profiles and Demand profiles which are stored in 8760 data series in separate csv files. The csv files for demand and RE profiles are stored in each of the country/sub-region’s data folder.

.. note::
    Required: Macros-> tools -> References (Microsoft Active X …..)
