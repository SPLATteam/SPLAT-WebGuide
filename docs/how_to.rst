How-To Guides
=============

.. _install_solver:

Installing an Alternative (Faster) Free Solver
----------------------------------------------

The MESSAGE software comes by default with a free solver called GLPK. This solver is adequate for working with small models, however, when a larger model is to be used (e.g. many timeslices, many technologies and subregions), this solver becomes inadequate requiring a long time to complete a "RUN".

There is an alternative free solver that can be used with MESSAGE called the CBC (Coil-or Branch and Cut solver [link:https://github.com/coin-or/Cbc]) that is more powerful and can solve larger problems at comparable speeds to some of the commercial solvers such as CPLEX.

However, to execute runs with this solver one must use the SPLAT Excel Interface to initiate runs (see Tutorial C - Using the SPLAT Excel Interface) and one has to add the solver to the user's existing MESSAGE installation. This guide gives a brief description on how to do this installation.


.. _using_message:

Restoring and opening a model using the MESSAGE interface
----------------------------------------------------------

Step 1

From the most recent folder that is being used in the training programme Sharepoint: Link to Sharepoint

Save the ZIP file that starts with "\MAINa_..." into a known location of the computer

