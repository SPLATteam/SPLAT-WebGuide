.. role:: inputcell
    :class: inputcell
.. role:: interfacecell
    :class: interfacecell
.. role:: button
    :class: button


Travailler avec les technologies
==========================

.. important::
    L'interface doit être liée au modèle avant d'exécuter l'une des étapes de cette section.
    Voir :ref:`link_interface`.

Une technologie dans le modèle est une unité de production d'électricité ou une combinaison de ces unités ou une ligne de transmission avec des paramètres spécifiques tels que la capacité maximale, le facteur de capacité, le CAPEX, le FOM, le coût du carburant, etc.

Une technologie peut être spécifique à un site (une centrale ou une ligne de transmission spécifique avec des paramètres connus) ou générique (une technologie avec des paramètres généralisés).
Les technologies dans SPLAT sont classées en quatre types principaux :

**1. Existing technologies:** Les technologies qui sont déjà en place à partir de l'année de référence.

**2. Committed technologies:** Les technologies en cours de construction ou dont la mise en œuvre a été approuvée. Le déploiement de ces technologies peut être considéré comme garanti dans les résultats du modèle.

**3. Candidate technologies:** Les technologies qui peuvent ou non être mises en service à long terme et donc faire partie du processus d'optimisation. Les caractéristiques de ces projets (taille, emplacement, technologie, etc.) doivent être cohérentes avec les infrastructures existantes, l'évolution des prix et le potentiel des ressources énergétiques.
Le modèle les sélectionnera s'ils présentent un avantage net pour le système électrique modélisé, ce qui implique que leur construction, leur exploitation et leur maintenance devraient minimiser le coût total de l'expansion du système électrique.

Le modèle SPLAT Africa utilisé dans le projet Continental Power System Master Plan (CMP) utilise le modèle énergétique « supply regions » (MSR).
MSR comprend des options d'approvisionnement solaire PV géoréférencées, solaires CSP, éoliennes terrestres et offshore conçues par l'IRENA grâce à une analyse géospatiale systématique expliquée dans cet article <https://www.nature.com/articles/s41597-022-01786 -5>`_.
Ces technologies d'énergies renouvelables variables sont également considérées comme des technologies candidates.

**4. Generic technologies:** Ces technologies ne sont pas spécifiques au site. Ils ont des paramètres généralisés. À l'instar des technologies candidates, ces technologies font également partie du processus d'optimisation. Le modèle sélectionnerait ces technologies si elles présentent un avantage net pour le système électrique modélisé.

Les technologies génériques sont normalement configurées de manière à ne pas être mises en ligne dans des scénarios de référence. L'une des principales motivations pour avoir des technologies génériques dans le modèle est de rendre le modèle indépendant de la technologie, ce qui à son tour augmente l'acceptation parmi les parties prenantes.

Les onglets Technologie sont répertoriés dans :ref:`technologysheets`

Cette section décrit comment afficher, ajouter et modifier des technologies à l'aide de l'interface SPLAT Excel.


.. _view_tech_inputs :

Affichage des entrées technologiques
-------------------------

1. Dans l'une des :ref:`fiches technologiques` (à l'exception des onglets contenant des informations sur des zones spécifiques), saisissez le scénario à interroger dans la cellule ``Choisir un scénario``

2. Cliquez sur :button:`Actualiser la feuille`. Les technologies et leurs paramètres dans le scénario seront présentés dans la même feuille. Seules les données du ou des pays chargés (dans la feuille ``Principal``) seront affichées.

3. Reportez-vous à :ref:`renewable_tech` pour connaître les étapes de récupération des informations sur les zones renouvelables (Solar PV, Solar CSP, Onshore Wind, Offshore Wind).

.. _add_tech :

Ajouter une technologie
-------------------

1. Actualisez la feuille :ref:`SpecificTech` pour le scénario sélectionné.

2. Ajoutez un nouveau nom de technologie spécifique et des paramètres dans le tableau. Assurez-vous que le code de technologie est unique et non répété.

3. Cliquez sur :button:`Ajouter de nouveaux techniciens`. Une technologie est ajoutée avec les paramètres de la technologie générique sous-jacente.

4. Actualisez la feuille pour voir la nouvelle technologie ajoutée. Actualisez les autres feuilles avant de modifier les paramètres pertinents.

.. note::
Les technologies de stockage de batterie et de pompe doivent être définies séparément dans la feuille :ref:`Battery&PumpStorage` dans l'interface SPLAT.

.. _rename_tech :

Renommer une technologie
---------------------

1. Entrez les anciens et nouveaux noms de technologie dans :ref:`RenameTechFacility` et cliquez sur :button:`Rename Techs in List`.

2. Pour confirmer que la technologie a été renommée, actualisez les onglets correspondants (``GenericTech`` ou ``SpecificTech``) pour voir les noms mis à jour. Plusieurs technologies peuvent être renommées.

.. image:: /images/technology_rename.PNG

.. _delete_tech :

Suppression d'une technologie
----------------------

1. Entrez les noms des technologies dans :ref:`DeleteTechFacility` et cliquez sur :button:`Delete Techs in List`.

2. Pour confirmer que la technologie a bien été supprimée, actualisez les onglets correspondants (``GenericTech`` ou ``SpecificTech``) pour voir la mise à jour. Plusieurs technologies peuvent être supprimées.

.. image:: /images/technology_delete.PNG

.. _change_tech :

Changer de technologie
----------------------

1. Dans l'une des :ref:`fiches techniques` (à l'exception des onglets contenant des informations sur des zones spécifiques), cliquez sur :button:`Actualiser la feuille` pour obtenir les données enregistrées dans le modèle pour le scénario choisi.

2. Apportez des modifications aux technologies de la feuille.

3. Cliquez sur :button:`Mettre à jour les données du modèle` pour mettre à jour le modèle avec les nouvelles données.

.. .. _carburant:

.. Prix du carburant
.. -----------

.. 1. Dans l'onglet :ref:`fuelprices`, cliquez sur :button:`Refresh Sheet` pour récupérer les données enregistrées dans le modèle pour le scénario et les pays choisis.

.. 2. Apportez des modifications aux prix du carburant dans la feuille.

.. 3. Cliquez sur :button:`Mettre à jour les données du modèle` pour mettre à jour le modèle avec les nouvelles données.

.. .. note::
.. 1. Le prix du carburant est indiqué en $/GJ. Il n'est actuellement pas possible d'ajouter de nouvelles technologies d'approvisionnement en carburant via l'interface SPLAT, cela est laissé pour un développement futur (ainsi que la possibilité de spécifier des limites, qui seraient nécessaires si l'on voulait modéliser une courbe d'approvisionnement pour un carburant particulier).
.. 2. Si un utilisateur spécifie des valeurs à la fois dans la colonne Constante et dans les colonnes de l'année du jalon, seule la valeur constante sera utilisée pour mettre à jour le modèle MESSAGE et les autres valeurs seront ignorées.

.. .. _tech_cost :

.. Coûts technologiques
.. -----------------

.. 1. Dans l'onglet :ref:`generictechcosts` et :ref:`specifictechcosts`, cliquez sur :button:`Refresh Sheet` pour obtenir les données de coûts enregistrées dans le modèle pour le scénario et les pays choisis.

.. 2. Apportez des modifications aux coûts (coût de nuit-$/kW, coût fixe d'O&M-$/kW, coût variable d'O&M-$/MWh) dans la feuille.

.. 3. Cliquez sur :button:`Mettre à jour les données du modèle` pour mettre à jour le modèle avec les nouvelles données.

.. .. note::
.. Si un utilisateur spécifie des valeurs à la fois dans la colonne Constante et dans les colonnes de l'année du jalon, seule la valeur constante sera utilisée pour mettre à jour le modèle MESSAGE et les autres valeurs seront ignorées.

.. .. _tech_capacity :

.. Limite de capacité
.. ---------------

.. 1. Dans l'onglet :ref:`specificcapacitylimits`, cliquez sur :button:`Refresh Sheet` pour obtenir les limites de capacité enregistrées dans le modèle pour le scénario et les pays choisis.

.. 2. Modifiez les limites de capacité dans la feuille.

.. 3. Cliquez sur :button:`Mettre à jour les données du modèle` pour mettre à jour le modèle avec les nouvelles données.

.. .. note::
.. 1. Il n'y a pas de limite de capacité pour les technologies génériques.
.. 2. Si un utilisateur spécifie des valeurs à la fois dans la colonne Constante et dans les colonnes de l'année du jalon, seule la valeur constante sera utilisée pour mettre à jour le modèle MESSAGE et les autres valeurs seront ignorées.

.. _renewable_tech :

Définir les technologies d'énergies renouvelables variables
-----------------------------------------------

.. _solar_wind :

Solaire PV, CSP, Eolien onshore et offshore
+++++++++++++++++++++++++++++++++++++

Les technologies ERV peuvent être définies de deux manières : soit comme des technologies génériques, soit comme des technologies spécifiques à un site. Vous trouverez ci-dessous un exemple d'ajout d'éolien offshore, d'abord en tant que technologie générique, puis en tant que zones.

1. Dans l'onglet :ref:`GenericTech`, ajoutez la technologie "XXWDLCO00" (XX étant l'ID du pays, par exemple DZ) avec la description de la technologie "Technologie générique offshore". Utilisez le bouton Ajouter une nouvelle technologie. La macro mettra à jour les fichiers sous-jacents et se rechargera à la fin.

2. Accédez à la feuille :ref:`RenameTechFacility`. Remplacez les technologies offshore nouvellement ajoutées par le nom de technologie générique approprié, c'est-à-dire XXWDOC00. La macro mettra à jour les fichiers sous-jacents et se rechargera à la fin.

3. Accédez à la feuille :ref:`OffshoreWindZones`. Ajoutez de nouvelles technologies dans chaque pays. Cliquez sur :button:`Ajouter de nouveaux techniciens`. La macro mettra à jour les fichiers sous-jacents et se rechargera à la fin.

4. Localisez le fichier .tit du modèle et ouvrez-le en tant qu'Excel, il vous demandera le paramètre de délimitation. Sélectionnez virgule. Les zones génériques éoliennes offshore et offshore nouvellement ajoutées auront les mêmes profils. Maintenant, allez à la feuille :ref:`OffshoreWindZones`. Donnez l'adresse au fichier qui contient les profils, dans la section fichier de données MSR. Cela mettra à jour les profils de zone dans le fichier .tit. Actuellement, la technologie générique éolienne offshore a le même profil que l'éolien générique. Mais rappelez-vous, la technologie générique éolienne terrestre a été évincée du modèle en définissant la première année = 2050

5. Les profils mis à jour dans le fichier .tit doivent être insérés dans les fichiers modèles. Accédez à la feuille :ref:`TimeSlices`, appuyez sur :button:`Update Files`.

.. _hydro_dam :

Barrage hydroélectrique
++++++++++

La feuille ``SpecificTechHydroDams`` manipule les barrages hydroélectriques dans le modèle.

1. Cliquez sur le bouton :button:`Refresh Sheet` pour extraire les technologies appartenant au `TechSetL2` : `Large Hydro Dams`.

2. Le bouton :button:`Create River Tech+Storage Constraint` ajoute une technologie et une contrainte de stockage pour chaque barrage.

Une nouvelle technologie factice pour chaque centrale hydroélectrique avec barrage est ajoutée pour modéliser les apports de la rivière au barrage. La convention de dénomination de la technologie factice est XXRIDM_rivername, par exemple CMRIDM_LAGDO (en utilisant LAGDO comme exemple). La sortie est réglée sur la forme d'énergie elc fictive existante.

Une nouvelle contrainte de stockage est ajoutée, exemple D_LAGDO avec le nom court DXXX. La contrainte de stockage est liée à CMRIDM_LAGDO avec un coefficient de +1, donc chaque flux de MWyr de CMRIDM_LAGDO augmente le contenu de stockage de 1 MWyr.

La contrainte de stockage est liée à CMHYDM_LAGDO avec un coefficient -1 (c'est-à-dire que chaque flux de MWyr de CMHYDM_LAGDO diminue le contenu du stockage de 1 MWyr). Il serait en théorie possible de faire une modélisation en cascade en liant le débit des usines amont à des contraintes de stockage en aval (plutôt qu'une technologie fluviale). Les coefficients devraient être mis à l'échelle par "l'énergie par unité de volume (MJ/m3)" relative des usines en amont et en aval. Cette fonctionnalité devra être revisitée en tant que nouvelle tâche de développement s'il y a un besoin pressant.

L'utilisateur doit spécifier 2 paramètres, dont les valeurs peuvent être calculées dans le tableau le plus à droite et copiées-collées.

3. Une fois cela fait, l'utilisateur peut cliquer sur :button:`Mettre à jour les données du modèle` :

La capacité est définie sur le débit maximal (en MW, débit maximal en m3/s mis à l'échelle par le débit de conception). La capacité est spécifiée comme limite de capacité sur la River Technology (bdi) .

Le volume maximal de la contrainte de stockage est défini sur Volume maximal en MWyr conformément au tableau.

L'utilisateur doit ensuite ajouter une série temporelle dans le fichier csv sous les technologies CMRIDM_LAGDO et :button:`Update Timeslices` dans la feuille ``Timeslice``. Les valeurs dans le fichier csv doivent être le débit moyen mensuel divisé par le "débit max" qui a été utilisé pour définir la "capacité de la rivière", en utilisant la même valeur de débit max quel que soit le scénario.
Si l'utilisateur souhaite simuler différents scénarios de précipitations sans série temporelle complète, il peut utiliser le facteur de plante pour augmenter ou réduire le profil dans la feuille ``SpecificTech``. Il n'est actuellement pas possible de spécifier un profil saisonnier différent par scénario, mais cette fonctionnalité est sur la liste des tâches dans un avenir proche.

.. _batteries:

Batteries et stockage de la pompe
++++++++++++++++++++++++++++

Les technologies de stockage de batteries et de pompes peuvent être ajoutées et modifiées de la même manière via l'interface excel SPLAT.

1. Dans la feuille ``Battery&PumpStorage`` : créez la technologie avec la convention techname : xxELSTyyyy pour une batterie ou xxELSTPSyyyy pour le stockage de la pompe, où xx est le code du pays et yyyy est la description du site. (Par exemple, ZAELSTPSDrakensberg)

2. :button:`Recharger Global`

3. Dans la même feuille ``Battery&PumpStorage`` cliquez sur :button:`Refresh` puis spécifiez les heures de stockage et l'efficacité du cycle

4. Dans les fiches ``TechSpecific`` précisez les autres paramètres usuels hc, bdi, inv etc...

.. .. _csp :

.. Énergie Solaire Concentrée (CSP)
.. ++++++++++++++++++++++++++++++

.. Reportez-vous aux étapes de :ref:`solar_wind`. (Améliorations à venir)

.. .. _transmission_distribution :

.. Transport et Distribution
.. -----------------------------

.. Les fiches :ref:`transmission` et :ref:`distribution` sont utilisées pour réviser ou modifier les paramètres des technologies de transmission et de distribution selon les définitions de la feuille ``TechnologySets`` (voir section ci-dessous).

.. .. note::
.. 1. Si l'utilisateur veut modéliser avec une demande "envoyée" (voir :ref:`demande`), l'efficacité de transmission doit être réglée sur 100 % et les coûts d'investissement sur une petite valeur. Dans la configuration par défaut, aucune technologie de distribution n'est spécifiée pour l'électricité "envoyée".

.. 2. Si un utilisateur spécifie des valeurs à la fois dans la colonne Constante et dans les colonnes de l'année du jalon, seule la valeur constante sera utilisée pour mettre à jour le modèle MESSAGE et les autres valeurs seront ignorées.

.. .. _interconnexion :

.. Interconnexion
.. -----------------

.. La fiche :ref:`interconnexions` permet de revoir et de mettre à jour les paramètres des interconnexions transfrontalières.

.. Au minimum les deux pays interconnectés (qui doivent être actifs) doivent être spécifiés pour visualiser les interconnexions entre eux.

.. _tech_naming :

Nommage de la technologie dans le modèle SPLAT
-----------------------------------------

La convention de dénomination des différentes technologies, y compris les niveaux de jeu de technologies 1 et 2, et les technologies génériques, est indiquée dans le tableau ci-dessous.
Le "??" dans le code de technologie au début fait référence au code de pays à deux lettres (alpha-2). Et le * fournit des informations supplémentaires sur la technologie.

La dénomination de l'ensemble technologique de niveau 1 suit les conventions suivantes dans le modèle SPLAT :

.. table-csv ::
    :file: csv_file/level1sets_sheet.csv
    :lignes d'en-tête : 1

La dénomination de l'ensemble technologique de niveau 2 suit les conventions suivantes dans le modèle SPLAT :

.. table-csv ::
    :file: csv_file/level2sets_sheet.csv
    :lignes d'en-tête : 1

La convention de dénomination des technologies génériques est donnée dans le tableau ci-dessous :

.. table-csv ::
    :file: csv_file/generictechcodes_sheet.csv
    :lignes d'en-tête : 1

.. _country_code :

Code pays dans le modèle SPLAT
-------------------------------

Les codes de pays à deux ou trois lettres utilisés dans le modèle SPLAT sont basés sur la norme `ISO 3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1>`_.