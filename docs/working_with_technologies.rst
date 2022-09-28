.. role:: inputcell
    :class: inputcell
.. role:: interfacecell
    :class: interfacecell
.. role:: button
    :class: button


Working with Technologies
==========================

A technology in the model is a power-producing unit or a combination of such units with specific parameters such as, maximum capacity, capacity factor, CAPEX, FOM, fuel cost etc.

This section describes how to view, add and change technologies using the SPLAT Excel Interface.

.. note::
    The interface must be linked to the model before executing any of the steps in this section.
    See :ref:`link_interface`.

.. _view_tech_inputs:

Viewing technology inputs
-------------------------

In the ``QueryTechInput`` sheet,

.. _add_tech:

Adding a technology
-------------------

.. _change_tech:

Changing and renaming a technology
----------------------------------

.. _delete_tech:

Deleting a technology
----------------------

.. _renewable_tech:

Renewable and storage technologies
----------------------------------

.. _solar_wind:

Solar PV, onshore and offshore Wind
+++++++++++++++++++++++++++++++++++

.. _hydro_dam:

Hydro Dam
++++++++++

The sheet manipulates the hydro dams in the model.

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

.. _csp:

Concentrated Solar Power (CSP)
++++++++++++++++++++++++++++++



