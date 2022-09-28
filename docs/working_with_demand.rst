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

The ``QueryDemand`` sheets allows the user to review parameters relating to demand.

1. In the sheet, specify what to extract:

    - Scenarios

    - Countries

    - Demand parameters

        - ``FinalEnergyDemand`` (MWyr): as specified in the model and also in GWh.

        - ``FinalPowerDemand`` (MW): calculated using the final energy demand and the load profiles for each of the demands.

        - ``SecondaryEnergyDemand`` (MWyr and GWh): calculated using the final energy demand, the distribution losses and the transmission losses.

        - ``SecondaryPowerDemand`` (MW): calculated using the secondary energy demand and the load profiles.

    - Year

2. Click the :button:`Refresh Query` button. The data is extracted in long format on the same sheet. The user can then review individual entries in the table using filters or a pivot table.

A Pivot Table was created for the user in a sheet called ``Pivot_Demand``, with some predefined views that can be modified as needed. It is also possible for the user to make multiple ‘Pivot tables’ from the same data dump or have multiple ‘Query sheets’ which query specific parameters. A new Query Sheet can be created by simply making a copy of an existing Query Sheet.


.. change_demand:

Changing demand input
----------------------
to add
