D�finition des r�gions
======================

V�RIFIER:

Des r�gions peuvent �tre ajout�es � un mod�le MESSAGE-SPLAT multir�gion existant comme suit�:

1. Copier le dossier Blank Regions

2. Renommez les fichiers (utilisez le code VBA dans ``Regions`` Module appel�: ``Rename_Files()``

3. Modifiez les fichiers�:

- C:\Programs\MESSAGE_INT\models\ACEC_V2\MAINa\Regid

- Recharger global dans l&#39;interface SPLAT

4. Rename Technologies (utilisez le code VBA dans le module ``Regions`` appel�: ``DeleteandrenameTechs()`` suivi du code VBA dans le module ``writeadb`` appel� ``WriteAllScenarios()``

5. Renommer la description du pays (en haut)

6. Rechercher et remplacer les produits �chang�s, ainsi que l&#39;�lectricit� secondaire

7. Ajoutez le nom de r�gion to C:\Programs\MESSAGE_INT\models\ACEC_V2\MAINa\data\MAINa.gen fichier

8. ajouter le fichier XXa.dir to C:\Programs\MESSAGE_INT\models\mms_fils\

9. Edit C:\Programs\MESSAGE_INT\models\mms_fils\glob.reg et ajoutez le chemin

10. Edit C:\Programs\MESSAGE_INT\models\mms_fils\mms.pro et ajoutez le chemin

-*.cin,-*.adb,-*.ldb,-*.mps,-*.chn,-*.lbu,-*.tab,-*.sol,-*.mst,-*.rar, -*.ggi,-*.sdb,-*.toc,-*.txt,-*.bat,-*.itl,-*.nbd
