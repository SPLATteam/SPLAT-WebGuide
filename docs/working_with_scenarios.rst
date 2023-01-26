.. role:: button
    :class: button

Working with Scenarios
=======================

.. note::
    The SPLAT excel interface is limited in doing scenario management directly. Please add and delete scenarios directly through MESSAGE.

.. _add_scenario:

Add a scenario
--------------
Scenarios need to be added via the MESSAGE interface. It is recommended that the user makes a copy of an existing scenario through the MESSAGE interface and load it into the SPLAT interface. Refer to :ref:`message_copy_scenario`.

.. _select_scenario:

Select a scenario
-----------------
To select a specific scenario in SPLAT, the respective scenario needs to be activated (Put "1" in Scenario to Reload column for the respective scenario in the Scenario table) in the Main sheet.
Then the Reload Global needs to be activated to load model data for model specified for given subregion and scenario specified in the table.
The data needs to be defined in the input sheets and constraints sheets to match the narratives and assumptions of the specific scenario.

.. note::
    When a input or constraints sheet is refreshed for a scenario (except adb) and a data field is empty, it implies that the scenario assumes the same value as defined in the adb scenario.
    To  define a new value for the data field, the data needs to be entered and :button:`Update model data` needs to be pressed to update the model data for the given scenario.

.. _define_fullintegration_scenario:

Defining FullIntegration scenario
---------------------------------
A Full Integration scenario considers integration in both country and regional level in the model. As opposed to other scenarios, the generic interconnectors come online in this scenario.
Therefore, the overnight costs of generic interconnectors ($/kW) need to be "well defined" in the ``Interconnectors`` sheet in the case of FullIntegration scenario.


