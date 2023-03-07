Defining Regions
=======================

TOCHECK:

Regions can be added to an existing multi-region MESSAGE-SPLAT model as follows:

1. Copy Blank Regions folder

2. Rename files (use VBA code in ``Regions`` Module called: ``Rename_Files()``

3. Edit files:

-	C:\Programs\MESSAGE_INT\models\ACEC_V2\MAINa\Regid

-	Reload global in SPLAT interface

4. Rename Technologies (use VBA code in ``Regions`` Module called: ``DeleteandrenameTechs()`` followed by VBA code in module ``writeadb`` called ``WriteAllScenarios()``

5. Rename Country description (at the top)

6. Search and replace traded commodity, as well as Secondary Electricity

7. Add region name to C:\Programs\MESSAGE_INT\models\ACEC_V2\MAINa\data\MAINa.gen file

8.  add XXa.dir file to C:\Programs\MESSAGE_INT\models\mms_fils\

9. Edit C:\Programs\MESSAGE_INT\models\mms_fils\glob.reg and add path

10. Edit C:\Programs\MESSAGE_INT\models\mms_fils\mms.pro and add path

-*.cin,-*.adb,-*.ldb,-*.mps,-*.chn,-*.lbu,-*.tab,-*.sol,-*.mst,-*.rar,-*.ggi,-*.sdb,-*.toc,-*.txt,-*.bat,-*.itl,-*.nbd
