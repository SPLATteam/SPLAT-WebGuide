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
Modèle pour les alternatives de stratégie de système énergétique et leurs impacts environnementaux généraux (MESSAGE)
a été conçu pour développer un modèle d'optimisation d'un système énergétique pour la planification à moyen et long terme, l'analyse de la politique énergétique et le développement de scénarios.
MESSAGE formule le modèle de programmation linéaire dynamique avec une option d'entiers mixtes.
(Les contraintes non linéaires ou la fonction objectif non linéaire ne peuvent être définies que pour un problème spécifique.)
MESSAGE résout le modèle d'optimisation en deux étapes :

1. Génération de matrice.

2. Optimisation du modèle à l'aide de la matrice générée.

La version actuelle du logiciel MESSAGE comprend les composants suivants :

* Une interface utilisateur pour construire un modèle.

* Bases de données.

* Un programme de génération de matrice appelé "mxg".

* Un programme d'optimisation appelé "opts".

* Un programme de post-traitement de la solution d'extraction des résultats appelé "cap".

La figure suivante montre le flux de contrôle et d'informations entre ces composants lors de l'exécution du programme MESSAGE.

.. image:: /images/message_components.PNG

La première partie de cette section décrit les différentes bases de données utilisées dans MESSAGE. Et la deuxième partie décrit l'importance des fichiers de modélisation créés par divers programmes lors de l'utilisation de MESSAGE.

.. _Databases_in_MESSAGE :

Bases de données dans MESSAGE
------------------------
MESSAGE crée chaque modèle dans une étude de cas distincte et, par conséquent, un fichier de base de données pour chaque modèle. Les types de bases de données utilisées dans MESSAGE sont donnés dans le tableau ci-dessous :

.. csv-table :: Bases de données dans MESSAGE
    :lignes d'en-tête : 1
    :file: csv_file/message_databases.csv
    :width: 5, 5, 20

L'interrelation des bases de données utilisées dans le programme MESSAGE est illustrée dans la figure ci-dessous :

.. image:: /images/message_databases.PNG

Signification des différents fichiers de modèle MESSAGE
------------------------------------------------
Cette section décrit les différents types de fichiers qui sont présents ou créés dans les sous-dossiers tels que ``data``, ``int`` et ``res`` dans le dossier ``models/Region`` lors de l'exécution du MESSAGE.

.. note::
  * ``Région`` pourrait faire référence à un acronyme pour un pays, par exemple, ``ZAa`` pour l'Afrique du Sud ou ``MAINa`` pour l'ensemble du continent.
  
  * ``CaseName`` fait référence à un scénario.
  
  * ``MXG`` est un programme de génération de matrice et ``CAP`` est utilisé pour le post-traitement de la solution et pour l'extraction des résultats dans l'application MESSAGE GUI.

Types de fichiers dans le dossier de données
+++++++++++++++++++++++++++++++
.. table-csv ::
    :class: full-largeur
    :lignes d'en-tête : 1
    :file: csv_file/message_data.csv

Types de fichiers dans le dossier intm (intérimaire)
+++++++++++++++++++++++++++++++
.. table-csv ::
    :class: full-largeur
    :lignes d'en-tête : 1
    :file: csv_file/message_intm.csv

Types de fichiers dans le dossier res
+++++++++++++++++++++++++++++++
.. table-csv ::
    :class: full-largeur
    :lignes d'en-tête : 1
    :file: csv_file/message_res.csv

.. _splat_message_workflow :

Flux de travail SPLAT MESSAGE
------------------------

Le diagramme de workflow SPLAT MESSAGE se présente comme suit :

.. image:: /images/splat_message_workflow.PNG

