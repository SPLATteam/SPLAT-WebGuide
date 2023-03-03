.. role:: inputcell
:class: inputcell
.. role:: interfacecell
:class: interfacecell
.. role:: button
:class: button
.. role:: tight-tableau
:class: tight-tableau

MESSAGE
=====================
Mod�le pour les alternatives de strat�gie de syst�me �nerg�tique et leurs impacts environnementaux g�n�raux (MESSAGE)
a �t� con�u pour d�velopper un mod�le d&#39;optimisation d&#39;un syst�me �nerg�tique pour la planification � moyen et long terme, l&#39;analyse de la politique �nerg�tique et le d�veloppement de sc�narios.
MESSAGE formule le mod�le de programmation lin�aire dynamique avec une option d&#39;entiers mixtes.
(Les contraintes non lin�aires ou la fonction objectif non lin�aire ne peuvent �tre d�finies que pour un probl�me sp�cifique.)
MESSAGE r�sout le mod�le d&#39;optimisation en deux �tapes�:

1. G�n�ration de matrice.

2. Optimisation du mod�le � l&#39;aide de la matrice g�n�r�e.

La version actuelle du logiciel MESSAGE comprend les composants suivants�:

* Une interface utilisateur pour construire un mod�le.

* Bases de donn�es.

* Un programme de g�n�ration de matrice appel� &quot;mxg&quot;.

* Un programme d&#39;optimisation appel� &quot;opts&quot;.

* Un programme de post-traitement de la solution d&#39;extraction des r�sultats appel� &quot;cap&quot;.

La figure suivante montre le flux de contr�le et d&#39;informations entre ces composants lors de l&#39;ex�cution du programme MESSAGE.

.. image:: /images/message_components.PNG

La premi�re partie de cette section d�crit les diff�rentes bases de donn�es utilis�es dans MESSAGE. Et la deuxi�me partie d�crit l&#39;importance des fichiers de mod�lisation cr��s par divers programmes lors de l&#39;utilisation de MESSAGE.

.. _Databases_in_MESSAGE�:

Bases de donn�es dans MESSAGE
---------------------------------
MESSAGE cr�e chaque mod�le dans une �tude de cas distincte et, par cons�quent, un fichier de base de donn�es pour chaque mod�le. Les types de bases de donn�es utilis�es dans MESSAGE sont donn�s dans le tableau ci-dessous :

.. csv-table :: Bases de donn�es dans MESSAGE
:lignes d&#39;en-t�te�: 1
:file: csv_file/message_databases.csv
:width: 5, 5, 20

L&#39;interrelation des bases de donn�es utilis�es dans le programme MESSAGE est illustr�e dans la figure ci-dessous�:

.. image:: /images/message_databases.PNG

Signification des diff�rents fichiers de mod�le MESSAGE
--------------------------------------------------------------
Cette section d�crit les diff�rents types de fichiers qui sont pr�sents ou cr��s dans les sous-dossiers tels que ``data``, ``int`` et ``res`` dans le dossier ``models/Region`` lors de l&#39;ex�cution du MESSAGE.

.. note::
* ``R�gion`` pourrait faire r�f�rence � un acronyme pour un pays, par exemple, ``ZAa`` pour l&#39;Afrique du Sud ou ``MAINa`` pour l&#39;ensemble du continent.

* ``CaseName`` fait r�f�rence � un sc�nario.

* ``MXG`` est un programme de g�n�ration de matrice et ``CAP`` est utilis� pour le post-traitement de la solution et pour l&#39;extraction des r�sultats dans l&#39;application MESSAGE GUI.

Types de fichiers dans le dossier de donn�es
+++++++++++++++++++++++++++++++++++++++++++++++
.. table-csv ::
:class: full-largeur
:lignes d&#39;en-t�te�: 1
:file: csv_file/message_data.csv

Types de fichiers dans le dossier intm (int�rimaire)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. table-csv ::
:class: full-largeur
:lignes d&#39;en-t�te�: 1
:file: csv_file/message_intm.csv

Types de fichiers dans le dossier res
++++++++++++++++++++++++++++++++++++++
.. table-csv ::
:class: full-largeur
:lignes d&#39;en-t�te�: 1
:file: csv_file/message_res.csv

.. _splat_message_workflow�:

Flux de travail SPLAT MESSAGE
---------------------------------

Le diagramme de workflow SPLAT MESSAGE se pr�sente comme suit�:

.. image:: /images/splat_message_workflow.PNG

