.. role:: inputcell
    :class: inputcell
.. role:: interfacecell
    :class: interfacecell
.. role:: button
    :class: button

Travailler avec la demande
====================

.. important::
    L'interface doit être liée au modèle avant d'exécuter l'une des étapes de cette section.
    Voir :ref:`link_interface`.

Cette section décrit comment afficher, modifier et ajouter une demande à l'aide de l'interface SPLAT.

.. view_demand :

Affichage de la saisie de la demande
---------------------

1. Dans l'onglet ``Demande``, entrez le scénario à interroger dans la cellule ``Choisir le scénario``

2. Cliquez sur :button:`Actualiser la feuille`. La demande annuelle dans le scénario (fichier adb ou ldb) sera indiquée dans la même feuille. Seules les données du ou des pays chargés (dans la feuille ``Principal``) seront affichées.

3. Dans l'onglet ``PeakDemand``, répétez les étapes 1 et 2 pour récupérer la demande de pointe pour le scénario sélectionné.

.. note::
    Des dispositions ont été prises pour travailler soit avec une demande "envoyée", soit avec une demande sectorielle telle que industrielle, urbaine et rurale. L'utilisateur verra les données de demande classées dans ces niveaux de demande multiples. Si le modèle utilise uniquement la demande d'émission, l'utilisateur doit définir les données sur les autres niveaux de demande à zéro, et vice versa, sinon la demande sera comptée deux fois. Notez également que les données brutes sont stockées dans les fichiers adb et ldb de MWyr. Les valeurs MWyr sont converties par SPLAT en GWh par défaut.

.. note::
La demande de pointe n'est pas une entrée directe dans le modèle SPLAT. La demande de pointe est estimée sur la base des valeurs énergétiques annuelles et du paramétrage du profil correspondant stocké dans le fichier Application Database (adb).

.. change_demand :

Modification de l'entrée de la demande
----------------------

1. Dans l'onglet ``Demande``, cliquez sur :button:`Refresh Sheet` pour obtenir les données enregistrées dans le modèle.

2. Apportez des modifications à la série de demandes dans la feuille.

3. Cliquez sur :button:`Mettre à jour la feuille` pour mettre à jour le modèle avec les nouvelles données.

.. image:: /images/demand_update.PNG



