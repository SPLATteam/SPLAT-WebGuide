.. role:: inputcell
    :class: inputcell
.. role:: interfacecell
    :class: interfacecell
.. role:: button
    :class: button


Commencer
===============
Cette section vise à guider le lecteur à travers un certain nombre d'étapes de base.

.. _conditions préalables:

Conditions préalables
--------------
Avant d'utiliser l'interface SPLAT, assurez-vous que les logiciels suivants sont installés et que les fichiers sont téléchargés :

.. note::
Si vous avez déjà reçu le kit d'apprentissage SPLAT, les logiciels suivants (à l'exception de Microsoft Excel) sont accessibles dans le dossier des logiciels. Si le kit ne vous a pas encore été délivré, veuillez remplir le `formulaire de demande`_ , ou contactez la personne IRENA avec laquelle vous êtes en contact.


- Microsoft Excel (version 64 bits, à vérifier :ref:`checking_bits`)
- Outil AIEA MESSAGE
-  	Un modèle
- Interface Excel SPLAT
- Solveur CBC (recommandé)

Le logiciel MESSAGE est livré avec un solveur gratuit appelé GLPK. Si un autre solveur est nécessaire, il devra être installé séparément. Nous vous recommandons d'utiliser le solveur CBC pour une utilisation avec l'interface SPLAT. Reportez-vous à :ref:`install_solver` pour utiliser des solveurs alternatifs comme cbc.


.. _formulaire de demande:
https://forms.office.com/Pages/ResponsePage.aspx?id=sOvdzLvS0ESYSo5CpcBis8X-QNFmuJNIrZ3pyvqZdPxURVJMTUw0Mzg1SkFHOTFFV0lXTFhLN1NEVS4u


.. _conventions:

Conventions
----------------
:inputcell:`Cellule d'entrée utilisateur`

Les cellules formatées comme ci-dessus (police sombre avec fond orange) sont des cellules de saisie utilisateur, où l'utilisateur est autorisé et censé saisir des données.

:interfacecell:`Réservé pour l'interface`

Les cellules formatées comme ci-dessus (police foncée avec fond gris pâle) sont des cellules réservées à l'interface. Ces cellules sont remplies par des macros dans le classeur ou sont des cellules calculées.

Les onglets sont organisés selon les conventions suivantes :

- Feuille ``Index`` : liste toutes les feuilles du classeur
- Feuille ``Main`` : où les utilisateurs définissent le chemin du modèle et sélectionnent les pays dans le modèle
- Onglets jaunes : pour revoir et mettre à jour les entrées de base du modèle
- Onglets rouges : pour exécuter un modèle et extraire les résultats
- Onglets gris : utilitaires disponibles pour les utilisateurs plus avancés

.. _first_steps :

Premiers pas
--------------
Cette documentation utilise un modèle simple pour la démonstration. Vous pouvez utiliser un modèle MESSAGE existant pour la plupart des exemples de cette documentation.

.. _checking_bits :

Vérification de la version Excel
+++++++++++++++++++++++++

L'interface SPLAT Excel nécessite la version 64 bits par défaut d'Excel pour ses fonctions principales. Vous pouvez vérifier votre version d'Excel en cliquant sur le menu :button:`Fichier` > :button:`Compte` > :button:`À propos d'Excel`. Si vous avez l'ancien Excel 32 bits, il est recommandé de désinstaller et de réinstaller votre logiciel Microsoft Office avec 64 bits sélectionné, ou d'utiliser un ordinateur avec un logiciel 64 bits déjà installé.

.. image:: /images/getting_started_opening_file_2.PNG

.. _restoring_model :

Restaurer le modèle dans MESSAGE
++++++++++++++++++++++++++

Afin d'exécuter le modèle à l'aide de l'interface Excel SPLAT, vous devrez peut-être restaurer le modèle dans MESSAGE une fois. Reportez-vous au guide pratique sur :ref:`using_message` pour obtenir des instructions sur l'utilisation de MESSAGE.

.. _opening_file :

Ouverture du dossier
++++++++++++++++++
Ouvrez le fichier Excel qui commence par *SPLAT_Interface_...*.

Lorsque vous ouvrez le fichier, vous devez cliquer sur :button:`Activer le contenu` (comme indiqué ci-dessous) pour que le fichier fonctionne.

.. image:: /images/getting_started_opening_file.PNG

De plus, les macros doivent être activées. Reportez-vous au lien pour `activer les macros`_.

.. _activer les macros :
https://support.microsoft.com/en-gb/office/enable-or-disable-macros-in-microsoft-365-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6

.. _checking_decimal :

Vérification du symbole décimal du système
++++++++++++++++++++++++++++++++++++
Le séparateur décimal de votre système doit être défini sur '.' (point) pour que l'interface SPLAT Excel fonctionne correctement. S'il en est autrement, par ex. ',' (virgule), allez dans ``Panneau de configuration`` > ``Région`` > ``Paramètres supplémentaires``, et remplacez le symbole décimal par '.'.

.. note::
    Le séparateur virgule est souvent le séparateur par défaut dans les environnements Windows français et devrait être modifié afin de pouvoir utiliser l'interface. Reportez-vous à :ref:`change_decimal_seperator`.

.. _link_interface :

Lier l'interface à votre fichier modèle
+++++++++++++++++++++++++++++++++++++++++

1. Dans l'onglet ``Main`` du fichier, assurez-vous que les champs :inputcell:`Model Folder` et :inputcell:`Main Region` sont correctement définis, comme indiqué ci-dessous, pour refléter l'emplacement du dossier modèle MESSAGE restauré sur votre ordinateur.

2. dans la section ``Sous-régions`` de l'onglet ``Principal``, choisissez le(s) pays que vous souhaitez activer, en plaçant un "1" à côté dans la colonne orange, et un "0" à côté de tout autre pays.

3. Cliquez sur le bouton :button:`Reload Global` en haut de la page (ceci connecte les fichiers de modèle MESSAGE avec ce classeur Excel). Les fichiers modèles sont lus et chargés en mémoire dans Excel.

4. Vous verrez une fenêtre pop-up indiquant "Données de 2 pays chargées en mémoire" (comme indiqué ci-dessous) ; appuyez sur :button:`OK`.

.. image:: /images/getting_started_linking_interface_1.PNG

.. image:: /images/getting_started_linking_interface_2.PNG

.. _view_input :

Affichage de l'entrée du modèle
++++++++++++++++++++++++

L'interface SPLAT Excel permet à un utilisateur de voir les données d'entrée stockées dans les modèles SPLAT-MESSAGE.

1. Dans l'un des onglets jaunes, choisissez le scénario dans la liste déroulante de la cellule C3.

2. Cliquez sur :button:`Refresh Sheet`, les données stockées dans le modèle s'afficheront dans le tableau.

Ce processus fonctionne de la même manière pour tous les onglets jaunes (``Demande``, ``Transmission``, ``Distribution``, etc.) de l'interface SPLAT Excel. Vous pouvez également actualiser toutes les feuilles dans ces onglets en cliquant sur :button:`Actualiser toutes les feuilles` dans l'onglet ``Principal``.

.. image:: /images/getting_started_viewing_input.PNG


.. caution::
Si vous avez vidé les cellules sous l'en-tête du tableau, appuyer sur 'Actualiser la feuille' provoquera une erreur. Cela se produit car le code de macro sous-jacent ne parvient pas à identifier la cellule de départ pour commencer à coller les données de modèle requises. Si vous rencontrez cette erreur, cliquez sur 'fin'> Recharger global> écrivez un simple alphabet simple dans la cellule juste sous la première cellule de l'en-tête du tableau> actualisez la feuille.


.. note::
    Gardez à l'esprit que le scénario "adb" (Application Database) contient toutes les données de base du modèle. Le choix d'un autre scénario n'affichera que les données **différentes** dans ce scénario. Donc, si vous choisissez un scénario et que les données sont vides, cela signifie qu'il a les mêmes données que "adb".


.. _run_model :

Exécution du modèle
++++++++++++++++++++

**Après** avoir lié votre modèle au fichier d'interface dans l'onglet ``Main``, vous pouvez exécuter votre modèle SPLAT à l'aide de l'onglet ``ReportGen-Annual``.

1. Sélectionnez la bonne combinaison de scénario et de pays que vous souhaitez exécuter.
Pour exécuter le modèle pour l'ensemble du continent, sélectionnez tous les pays et "MAINa" dans les sous-régions/pays.

2. Sélectionnez l'option préférée (avec ou sans interconnexions entre les sous-régions) sous ``Options d'exécution (sous-régions)``.
Pour un modèle à un seul comté, sélectionnez :inputcell:`Separate Subregions`.
Pour un modèle multi-pays, :inputcell:`Sous-régions séparées` ou :inputcell:`Interconnectées` peuvent être sélectionnées en fonction du récit du scénario pour l'interconnexion entre les pays.
Dans cet exemple, nous sélectionnons l'option :inputcell:`Interconnecté``.

3. Sélectionnez l'option correcte sous les catégories "Exécuter". Les catégories correspondent aux mêmes options dans le menu "Exécuter" MESSAGE :
:inputcell:`Mxg` = générateur de matrice ;
:inputcell:`Opt` = Optimisation ;
:inputcell:`Cap` = Création du fichier Cap ;
:inputcell:`All` = effectuer tout ce qui précède.
Il existe trois options différentes fournies dans l'interface pour CPLEX, CBC et GUROBI selon le solveur que vous avez préinstallé. Si vous êtes un nouvel utilisateur, veuillez installer et utiliser CBC (:ref:`install_solver`).

4. Appuyez sur le bouton :button:`Exécuter`. Vous devriez voir la fenêtre MESSAGE noire apparaître et commencer à s'exécuter.

.. image:: /images/getting_started_running_model.PNG

.. _extract_results :

Extraction des résultats
++++++++++++++++++++++++

Utiliser l'onglet ReportGen
~~~~~~~~~~~~~~~~~~~~~~~~~
L'onglet ``ReportGen-Annual`` est également l'endroit où vous pouvez extraire les résultats du modèle que vous venez d'exécuter.

1. Sélectionnez la combinaison scénario(s), pays(s), variable(s) et année(s) dont vous souhaitez afficher les résultats. Veuillez vous assurer que le scénario souhaité a été chargé dans la mémoire Excel. S'il n'apparaît pas dans la liste déroulante, veuillez revenir à l'onglet « Principal » et marquer le scénario souhaité « 1 » et appuyer sur le bouton « Recharger global ».

2. Sélectionnez le format de sortie et entrez le chemin de sortie (le cas échéant) dans la section ``Destination des résultats``.

3. Cliquez sur :button:`Get Results` (cercle rouge dans l'image ci-dessous). Si :inputcell:`sur cette feuille` est sélectionné, vous devriez voir les résultats bruts apparaître sur la feuille lorsque le processus est terminé. Si :inputcell:`csv` est sélectionné, les résultats seront écrits dans un fichier csv à l'emplacement spécifié. Si l'emplacement n'existe pas, il y aura un message d'erreur. L'option csv est plus pratique lorsque vous travaillez avec un grand nombre de résultats, et ils peuvent être liés à d'autres tableaux croisés dynamiques dans Excel ou d'autres logiciels tels que PowerBi ou Tableau.

.. image:: /images/getting_started_extract_results_1.PNG

Mettre à jour les tableaux de résultats
~~~~~~~~~~~~~~~~~~~~~~~~~
Vous pouvez trouver les tableaux de résultats annuels dans les feuilles rouges : ``Capacity``, ``Output``, ``New Capacity``, ``CO2`` et ``Costs``.

.. important::

    Assurez-vous de vérifier que le scénario et le pays corrects sont choisis en haut du tableau.

Cliquez avec le bouton droit n'importe où dans le tableau de la feuille de calcul et sélectionnez :button:`Actualiser` dans les options. Ces graphiques doivent être mis à jour ** chaque fois ** que vous obtenez de nouveaux résultats.

.. image:: /images/getting_started_extract_results_2.PNG
