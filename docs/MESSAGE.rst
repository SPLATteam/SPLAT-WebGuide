.. role:: inputcell
    :class: inputcell
.. role:: interfacecell
    :class: interfacecell
.. role:: button
    :class: button

MESSAGE 
=====================

.. _Databases_in_MESSAGE:

Databases in MESSAGE
------------------------

.. list-table:: The extensions of MESSAGE files indicate the type of data they contain.
    :widths: 10 10 50
    :header-rows: 1
    :stub-columns: 1

    * - Extension
      - Full form
      - Significance
    * - adb
      - Application database
      - adb file is created and maintained for each case study. It contains information on default scenario created by MESSAGE.
    * - ldb
      - Local database 	
      - ldb file is created and maintained for each (alternative) scenario in a case study. It is a copy of adb file. It is created for each alternative scenario, which user can modify as per their scenario narratives. When input sheets (parameters) are updated in SPLAT for alternative scenario, the corresponding ldb files also get updated.
    * - tdb
      - Technology database
tdb file is created and maintained independent of any case study
    * - upd
      - Update database
      - upd file is created and maintained to update values in the adb and/or a set of scenarios in a case study across the board.
