.. role:: inputcell
:class: inputcell
.. role:: interfacecell
:class: interfacecell
.. role:: button
:class: button


Commencer
=====================
Cette section vise à guider le lecteur à travers un certain nombre d&#39;étapes de base.

.. _conditions préalables:

Conditions préalables
------------------
Avant d&#39;utiliser l&#39;interface SPLAT, assurez-vous que les logiciels suivants sont installés et que les fichiers sont téléchargés :

.. note::
Si vous avez déjà reçu le kit d&#39;apprentissage SPLAT, les logiciels suivants (à l&#39;exception de Microsoft Excel) sont accessibles dans le dossier des logiciels. Si le kit ne vous a pas encore été délivré, veuillez remplir le `formulaire de demande`_ , ou contactez la personne IRENA avec laquelle vous êtes en contact.


- Microsoft Excel (version 64 bits, à vérifier :ref:`checking_bits`)
- Outil AIEA MESSAGE
- Un modèle
- Interface Excel SPLAT
- Solveur CBC (recommandé)

Le logiciel MESSAGE est livré avec un solveur gratuit appelé GLPK. Si un autre solveur est nécessaire, il devra être installé séparément. Nous vous recommandons d&#39;utiliser le solveur CBC pour une utilisation avec l&#39;interface SPLAT. Reportez-vous à :ref:`install_solver` pour utiliser des solveurs alternatifs comme cbc.


.. _formulaire de demande:
https://forms.office.com/Pages/ResponsePage.aspx?id=sOvdzLvS0ESYSo5CpcBis8X-QNFmuJNIrZ3pyvqZdPxURVJMTUw0Mzg1SkFHOTFFV0lXTFhLN1NEVS4u


.. _conventions:

Conventions
----------------------
:inputcell:`Cellule d&#39;entrée utilisateur`

Les cellules formatées comme ci-dessus (police sombre avec fond orange) sont des cellules de saisie utilisateur, où l&#39;utilisateur est autorisé et censé saisir des données.

:interfacecell:`Réservé pour l&#39;interface`

Les cellules formatées comme ci-dessus (police foncée avec fond gris pâle) sont des cellules réservées à l&#39;interface. Ces cellules sont remplies par des macros dans le classeur ou sont des cellules calculées.

Les onglets sont organisés selon les conventions suivantes :

- Feuille ``Index`` : liste toutes les feuilles du classeur
- Feuille ``Main`` : où les utilisateurs définissent le chemin du modèle et sélectionnent les pays dans le modèle
- Onglets jaunes : pour revoir et mettre à jour les entrées de base du modèle
- Onglets rouges : pour exécuter un modèle et extraire les résultats
- Onglets gris : utilitaires disponibles pour les utilisateurs plus avancés

.. _first_steps :

Premiers pas
------------------
Cette documentation utilise un modèle simple pour la démonstration. Vous pouvez utiliser un modèle MESSAGE existant pour la plupart des exemples de cette documentation.

.. _checking_bits :

Vérification de la version Excel
+++++++++++++++++++++++++++++++++

L&#39;interface SPLAT Excel nécessite la version 64 bits par défaut d&#39;Excel pour ses fonctions principales. Vous pouvez vérifier votre version d&#39;Excel en cliquant sur le menu :button:`Fichier` &gt; :button:`Compte` &gt; :button:`À propos d&#39;Excel`. Si vous avez l&#39;ancien Excel 32 bits, il est recommandé de désinstaller et de réinstaller votre logiciel Microsoft Office avec 64 bits sélectionné, ou d&#39;utiliser un ordinateur avec un logiciel 64 bits déjà installé.

.. image:: /images/getting_started_opening_file_2.PNG

.. _restoring_model :

Restaurer le modèle dans MESSAGE
++++++++++++++++++++++++++++++++++

Afin d&#39;exécuter le modèle à l&#39;aide de l&#39;interface Excel SPLAT, vous devrez peut-être restaurer le modèle dans MESSAGE une fois. Reportez-vous au guide pratique sur :ref:`using_message` pour obtenir des instructions sur l&#39;utilisation de MESSAGE.

.. _opening_file :

Ouverture du fichier
++++++++++++++++++++++++
Ouvrez le fichier Excel qui commence par *SPLAT_Interface_...*.

Lorsque vous ouvrez le fichier, vous devez cliquer sur :button:`Activer le contenu` (comme indiqué ci-dessous) pour que le fichier fonctionne.

.. image:: /images/getting_started_opening_file.PNG

De plus, les macros doivent être activées. Reportez-vous au lien pour `activer les macros`_.

.. _activer les macros :
https://support.microsoft.com/en-gb/office/enable-or-disable-macros-in-microsoft-365-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6

.. _checking_decimal :

Vérification du symbole décimal du système
++++++++++++++++++++++++++++++++++++++++++++++
Le séparateur décimal de votre système doit être défini sur &#39;.&#39; (point) pour que l&#39;interface SPLAT Excel fonctionne correctement. S&#39;il en est autrement, par exemple &#39;,&#39; (virgule), allez dans ``Panneau de configuration`` &gt; ``Région`` &gt; ``Paramètres supplémentaires``, et remplacez le symbole décimal par &#39;.&#39;.

.. note::
Le séparateur virgule est souvent le séparateur par défaut dans les environnements Windows français et devrait être modifié afin de pouvoir utiliser l&#39;interface. Reportez-vous à :ref:`change_decimal_seperator`.

.. _link_interface :

Lier l&#39;interface à votre fichier modèle
++++++++++++++++++++++++++++++++++++++++++++++++++ +++++++

1. Dans l&#39;onglet ``Main`` du fichier, assurez-vous que les champs :inputcell:`Model Folder` et :inputcell:`Main Region` sont correctement définis, comme indiqué ci-dessous, pour refléter l&#39;emplacement du dossier modèle MESSAGE restauré sur votre ordinateur.

2. dans la section ``Sous-régions`` de l&#39;onglet ``Principal``, choisissez le(s) pays que vous souhaitez activer, en plaçant un &quot;1&quot; à côté dans la colonne orange, et un &quot;0&quot; à côté de tout autre pays.

3. Cliquez sur le bouton :button:`Reload Global` en haut de la page (ceci connecte les fichiers de modèle MESSAGE avec ce classeur Excel). Les fichiers modèles sont lus et chargés en mémoire dans Excel.

4. Vous verrez une fenêtre pop-up indiquant &quot;Données de 2 pays chargées en mémoire&quot; (comme indiqué ci-dessous) ; appuyez sur :button:`OK`.

.. image:: /images/getting_started_linking_interface_1.PNG

.. image:: /images/getting_started_linking_interface_2.PNG

.. _view_input :

Affichage de l&#39;entrée du modèle
++++++++++++++++++++++++++++++++

L&#39;interface SPLAT Excel permet à un utilisateur de voir les données d&#39;entrée stockées dans les modèles SPLAT-MESSAGE.

1. Dans l&#39;un des onglets jaunes, choisissez le scénario dans la liste déroulante de la cellule C3.

2. Cliquez sur :button:`Refresh Sheet`, les données stockées dans le modèle s&#39;afficheront dans le tableau.

Ce processus fonctionne de la même manière pour tous les onglets jaunes (``Demande``, ``Transmission``, ``Distribution``, etc.) de l&#39;interface SPLAT Excel. Vous pouvez également actualiser toutes les feuilles dans ces onglets en cliquant sur :button:`Actualiser toutes les feuilles` dans l&#39;onglet ``Principal``.

.. image:: /images/getting_started_viewing_input.PNG


.. caution::
Si vous avez vidé les cellules sous l&#39;en-tête du tableau, appuyer sur &#39;Actualiser la feuille&#39; provoquera une erreur. Cela se produit car le code de macro sous-jacent ne parvient pas à identifier la cellule de départ pour commencer à coller les données de modèle requises. Si vous rencontrez cette erreur, cliquez sur &#39;fin&#39;&gt; Recharger global&gt; écrivez un simple alphabet simple dans la cellule juste sous la première cellule de l&#39;en-tête du tableau&gt; actualisez la feuille.


.. note::
Gardez à l&#39;esprit que le scénario &quot;adb&quot; (Application Database) contient toutes les données de base du modèle. Le choix d&#39;un autre scénario n&#39;affichera que les données **différentes** dans ce scénario. Donc, si vous choisissez un scénario et que les données sont vides, cela signifie qu&#39;il a les mêmes données que &quot;adb&quot;.


.. _run_model :

Exécution du modèle
++++++++++++++++++++++++++

**Après** avoir lié votre modèle au fichier d&#39;interface dans l&#39;onglet ``Main``, vous pouvez exécuter votre modèle SPLAT à l&#39;aide de l&#39;onglet ``ReportGen-Annual``.

1. Sélectionnez la bonne combinaison de scénario et de pays que vous souhaitez exécuter.
Pour exécuter le modèle pour l&#39;ensemble du continent, sélectionnez tous les pays et &quot;MAINa&quot; dans les sous-régions/pays.

2. Sélectionnez l&#39;option préférée (avec ou sans interconnexions entre les sous-régions) sous ``Options d&#39;exécution (sous-régions)``.
Pour un modèle à un seul comté, sélectionnez :inputcell:`Separate Subregions`.
Pour un modèle multi-pays, :inputcell:`Sous-régions séparées` ou :inputcell:`Interconnectées` peuvent être sélectionnées en fonction du récit du scénario pour l&#39;interconnexion entre les pays.
Dans cet exemple, nous sélectionnons l&#39;option :inputcell:`Interconnecté``.

3. Sélectionnez l&#39;option correcte sous les catégories &quot;Exécuter&quot;. Les catégories correspondent aux mêmes options dans le menu &quot;Exécuter&quot; MESSAGE :
:inputcell:`Mxg` = générateur de matrice ;
:inputcell:`Opt` = Optimisation ;
:inputcell:`Cap` = Création du fichier Cap ;
:inputcell:`All` = effectuer tout ce qui précède.
Il existe trois options différentes fournies dans l&#39;interface pour CPLEX, CBC et GUROBI selon le solveur que vous avez préinstallé. Si vous êtes un nouvel utilisateur, veuillez installer et utiliser CBC (:ref:`install_solver`).

4. Appuyez sur le bouton :button:`Exécuter`. Vous devriez voir la fenêtre MESSAGE noire apparaître et commencer à s&#39;exécuter.

.. image:: /images/getting_started_running_model.PNG

.. _extract_results :

Extraction des résultats
++++++++++++++++++++++++++++++++

Utiliser l&#39;onglet ReportGen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
L&#39;onglet ``ReportGen-Annual`` est également l&#39;endroit où vous pouvez extraire les résultats du modèle que vous venez d&#39;exécuter.

1. Sélectionnez la combinaison scénario(s), pays(s), variable(s) et année(s) dont vous souhaitez afficher les résultats. Veuillez vous assurer que le scénario souhaité a été chargé dans la mémoire Excel. S&#39;il n&#39;apparaît pas dans la liste déroulante, veuillez revenir à l&#39;onglet « Principal » et marquer le scénario souhaité « 1 » et appuyer sur le bouton « Recharger global ».

2. Sélectionnez le format de sortie et entrez le chemin de sortie (le cas échéant) dans la section ``Destination des résultats``.

3. Cliquez sur :button:`Get Results` (cercle rouge dans l&#39;image ci-dessous). Si :inputcell:`sur cette feuille` est sélectionné, vous devriez voir les résultats bruts apparaître sur la feuille lorsque le processus est terminé. Si :inputcell:`csv` est sélectionné, les résultats seront écrits dans un fichier csv à l&#39;emplacement spécifié. Si l&#39;emplacement n&#39;existe pas, il y aura un message d&#39;erreur. L&#39;option csv est plus pratique lorsque vous travaillez avec un grand nombre de résultats, et ils peuvent être liés à d&#39;autres tableaux croisés dynamiques dans Excel ou d&#39;autres logiciels tels que PowerBi ou Tableau.

.. image:: /images/getting_started_extract_results_1.PNG

Mettre à jour les tableaux de résultats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Vous pouvez trouver les tableaux de résultats annuels dans les feuilles rouges : ``Capacity``, ``Output``, ``New Capacity``, ``CO2`` et ``Costs``.

.. important::

Assurez-vous de vérifier que le scénario et le pays corrects sont choisis en haut du tableau.

Cliquez avec le bouton droit n&#39;importe où dans le tableau de la feuille de calcul et sélectionnez :button:`Actualiser` dans les options. Ces graphiques doivent être mis à jour ** chaque fois ** que vous obtenez de nouveaux résultats.

.. image:: /images/getting_started_extract_results_2.PNG
