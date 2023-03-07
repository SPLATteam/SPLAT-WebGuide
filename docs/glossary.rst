.. role:: inputcell
:class: inputcell
.. role:: interfacecell
:class: interfacecell
.. role:: button
:class: button

Description des feuilles
=============================

.. _principal:

Principal
-------

Définissez le chemin du modèle, rechargez les données du modèle dans la mémoire et sélectionnez les pays actifs pour l&#39;interrogation

:inputcell:`Model Folder` chemin du modèle MESSAGE à connecter à l&#39;interface SPLAT

:inputcell:`Région principale` nom du modèle MESSAGE à connecter à l&#39;interface SPLAT

:inputcell:`Region Active?` liste des sous-régions (pays) à charger en mémoire

:inputcell:`Scenarios to Load` liste des scénarios actuellement spécifiés dans la région principale et pour spécifier les scénarios à charger en mémoire

:interfacecell:`Country Name` codes pays dans le modèle MESSAGE

:interfacecell:`Description` noms de pays développés

:interfacecell:`Power Pool` le pool énergétique auquel appartient un pays

:interfacecell:`TimeSlices/Load Regions` nombre de tranches de temps modélisées par an

:interfacecell:`# Demands` nombre de composants de la demande

:interfacecell:`# Technologies` nombre de technologies dans le pays

:interfacecell:`# Contraintes` nombre de contraintes dans le pays

:interfacecell:`Scenarios` nom des scénarios

:interfacecell:`Taux d&#39;actualisation` taux d&#39;actualisation des technologies

:button:`Reload Global` importe les données du modèle stockées dans les fichiers adb et ldb dans la mémoire, effectue divers calculs.

:button:`Actualiser toutes les feuilles` rafraîchit les feuilles de données (feuilles jaunes) pour les sous-régions et les scénarios rechargés

:button:`Enregistrer tous les fichiers de scénario en utilisant le formatage SPLAT` enregistrer tous les fichiers de modèle (adb et ldb) en utilisant le formatage Excel-SPLAT pour les sous-régions sélectionnées (utilisez ceci après avoir apporté une modification avec l&#39;interface MESSAGE)
Si vous appuyez sur ce bouton, les fichiers MAINa ldb seront également mis à jour si MAINa est sélectionné, pour exclure les interconnexions des sous-régions qui ne sont pas sélectionnées ci-dessous.

.. _input_sheets :

Feuilles d&#39;entrée
------------------

Cette section contient la liste des paramètres (ainsi que le code des paramètres, leur unité et leurs définitions) présents dans chaque feuille de saisie de l&#39;interface SPLAT.

.. note::
1. Les valeurs des paramètres se réfèrent à la valeur du paramètre pour le pays donné pour le scénario donné pour la ou les années données.
2. Les données de séries chronologiques peuvent parfois être insérées pour un petit nombre d&#39;années et SPLAT les interpolera linéairement pour les années manquantes.
3. Tous les coûts doivent être indiqués dans une année de base commune (par exemple, le modèle CMP a adopté l&#39;année de base 2019.)

.. _demand_sheet :

Demande
+++++++++++++++++++++++++++

.. table-csv ::
:file: csv_file/demand_sheet.csv
:lignes d&#39;en-tête : 1
:widths: 20 10 50

.. _peakdemand_sheet :

Pic de demande
+++++++++++++++++
.. table-csv ::
:file: csv_file/peakdemand_sheet.csv
:lignes d&#39;en-tête : 1
:widths: 20 10 50

.. _t&amp;d_sheet :

Transport et distribution
++++++++++++++++++++++++++++++++++++++++++

Les feuilles :ref:`transmission` et :ref:`distribution` sont utilisées pour réviser ou modifier les paramètres des technologies de transmission et de distribution selon les définitions de la feuille ``TechnologySets`` (voir section ci-dessous).

.. note::
1. Si l&#39;utilisateur souhaite modéliser avec une demande &quot;envoyée&quot; (voir :ref:`demand`), l&#39;efficacité de transmission doit être définie sur 100 % et les coûts d&#39;investissement sur une petite valeur. Dans la configuration par défaut, aucune technologie de distribution n&#39;est spécifiée pour l&#39;électricité &quot;envoyée&quot;.

2. Si un utilisateur spécifie des valeurs à la fois dans la colonne Constante et dans les colonnes de l&#39;année du jalon, seule la valeur constante sera utilisée pour mettre à jour le modèle MESSAGE et les autres valeurs seront ignorées.

.. table-csv ::
:file: csv_file/t&amp;d_sheet.csv
:lignes d&#39;en-tête : 1
:widths: 20 10 50

.. note::
Pour la distribution, les valeurs doivent être saisies pour les types de distribution urbaine, rurale, industrielle et commerciale.

.. _fuelprices_sheet :

Prix du carburant
+++++++++++++++++++++++++++
.. table-csv ::
:file: csv_file/fuelprices_sheet.csv
:lignes d&#39;en-tête : 1
:widths: 20 10 50

.. _tech_sheet :

GenericTech et SpecificTech
+++++++++++++++++++++++++++

La feuille ``GenericTech`` affiche les paramètres génériques de la technologie.

La feuille ``SpecificTech`` est utilisée pour examiner et mettre à jour les paramètres de la technologie de production d&#39;énergie spécifiques au site qui sont constants dans le temps.
La feuille ``SpecificTech`` a un bouton supplémentaire : :button:`Add missing Tech`, qui permet à l&#39;utilisateur d&#39;ajouter une nouvelle technologie spécifique au site au modèle MESSAGE qui est lié.
Actuellement cette action effectue l&#39;ajout en copiant les paramètres technologiques d&#39;une technologie générique du même type de technologie tel que spécifié par les 6 premiers caractères du nom de la technologie. Une nouvelle technologie sera automatiquement ajoutée à tous les scénarios actifs. Un code de technologie MESSAGE est créé automatiquement sur la base des produits d&#39;entrée et de sortie (tels que spécifiés par la technologie générique associée) et des technologies déjà existantes ayant les mêmes entrées et sorties.
Une fois qu&#39;une nouvelle technologie est ajoutée, ses paramètres doivent être mis à jour à l&#39;aide du bouton :button:`Mettre à jour les données du modèle`.

.. table-csv ::
:file: csv_file/tech_sheet.csv
:lignes d&#39;en-tête : 1
:widths: 20 20 10 50

.. note::
1. Les profils/courbes de charge sont calculés par SPLAT sur la base des valeurs horaires (8760) présentes dans le fichier *.tit du dossier de données. Ils sont stockés dans les fichiers adb, ldb et ldr. La raison pour laquelle ils ne figurent pas dans la feuille de calcul est qu&#39;ils varient en fonction de la définition de la région de chargement/de la tranche de temps (par exemple, grand modèle/petit modèle) et qu&#39;il serait très difficile de les gérer efficacement dans une feuille de calcul.

2. ** Paramètres pertinents pour la feuille ``SpecificTech`` uniquement.

.. _techcosts_sheet :

GenericTechCosts et SpecificTechCosts
+++++++++++++++++++++++++++

Ces feuilles affichent les paramètres de coût qui sont constants ou changent sur l&#39;horizon du modèle.

.. table-csv ::
:file: csv_file/techcosts_sheet.csv
:lignes d&#39;en-tête : 1
:widths: 20 10 50

.. _specifictechhydrodams_sheet :

SpecificTechHydroDams
+++++++++++++++++++++++++++

L&#39;approche pour définir les technologies de barrages hydroélectriques dans SPLAT est donnée dans la section :ref:`hydro_dam`. Les paramètres utilisés pour les définir sont donnés ci-dessous :

.. table-csv ::
:file: csv_file/specifictechhydrodams_sheet.csv
:lignes d&#39;en-tête : 1
:widths: 20 20 10 50

.. _batterie&amp;pumpstorage_sheet :

Stockage de la batterie et de la pompe
+++++++++++++++++++++++++++

L&#39;approche pour définir les technologies de stockage de batteries et de pompes dans SPLAT est donnée dans la section :ref:`batteries`. Les paramètres utilisés pour les définir sont donnés ci-dessous :

.. table-csv ::
:file: csv_file/batterie&amp;pumpstorage_sheet.csv
:lignes d&#39;en-tête : 1
:widths: 20 20 10 50

.. _interconnectors_sheet :

Interconnexions
+++++++++++++++++++++++++++

La fiche :ref:`interconnexions` permet de revoir et de mettre à jour les paramètres des interconnexions transfrontalières. Au minimum, les deux pays interconnectés (qui doivent être actifs) doivent être spécifiés pour visualiser les interconnexions entre eux.

.. table-csv ::
:file: csv_file/interconnectors_sheet.csv
:lignes d&#39;en-tête : 1
:widths: 20 20 10 50

.. _caplimits_sheet :

SpecificCapacityLimits et InterconnectorsCapLimits
++++++++++++++++++++++++++++++++++++++++++++++++++ +++++++++++++++++++++++

.. table-csv ::
:file: csv_file/caplimits_sheet.csv
:lignes d&#39;en-tête : 1
:widths: 20 10 50

.. _vrezones_sheet :

PVZones, WindZones, OffshoreWindZones, CSP6hrZones et CSP12hrZones
++++++++++++++++++++++++++++++++++++++++++++++++++ +++++++++++++++++++++++++++++++++++++++++++

L&#39;approche pour définir les technologies VRE (solaire PV, CSP, éolien terrestre et offshore) est donnée dans la section :ref:`solar_wind`.
Les paramètres nécessaires pour définir les zones VRE sont indiqués dans le tableau ci-dessous :

.. table-csv ::
:file: csv_file/vrezones_sheet.csv
:lignes d&#39;en-tête : 1
:widths: 20 20 10 50

.. note::
1. Les données de latitude et de longitude peuvent être stockées dans les fichiers adb avec le reste des données d&#39;entrée du modèle. Il n&#39;est pas utilisé par SPLAT ou MESSAGE pour quoi que ce soit, mais il peut être utilisé par les visualiseurs de résultats pour l&#39;affichage sur des cartes (par exemple dans Tableau).

2. Pour les paramètres d&#39;investissement compensatoire et d&#39;investissement multiplicateur, il ne faut pas oublier d&#39;utiliser l&#39;option déroulante &quot;Réinitialiser l&#39;investissement&quot; dans la cellule F6, lorsque les coûts génériques sont mis à jour pour une raison quelconque, ou avant qu&#39;une mise à jour ne soit effectuée dans les données MSR brutes, avant -l&#39;application de &quot;l&#39;Investissement Offset&quot;.

3. Le paramètre d&#39;investissement multiplicateur (selon la classe de turbine) se trouve uniquement dans la feuille ``WindZones``. Cette catégorisation ne s&#39;applique pas à l&#39;offshore car il est supposé que toutes les éoliennes offshore sont de la même classe.

.. .. _demande:

.. Demande
.. ++++++++

.. Affiche toutes les séries de demande dans le modèle, y compris la demande totale &quot;envoyée&quot; (c&#39;est-à-dire secondaire, ou avant la transmission et la distribution) et la demande finale par secteur

.. .. _picdedemande :

.. Pic de demande
.. ++++++++++++++

.. Affiche les séries de demande de pointe en MW dans le modèle, y compris la demande totale &quot;envoyée&quot; (c&#39;est-à-dire secondaire, ou avant la transmission et la distribution) et la demande finale par secteur

.. .. _Prix du carburant:

.. Prix du carburant
.. --------------

.. Affiche les prix des carburants utilisés dans le modèle

.. .. _fichestechniques :

.. Fiches techniques
.. ------------------------

.. .. _generictech :

.. GenericTech
.. +++++++++++++++++

.. Affiche les paramètres technologiques génériques qui sont constants sur l&#39;horizon du modèle

.. .. _generictechcosts :

.. Coûts techniques génériques
.. ++++++++++++++++++++++++

.. Affiche les paramètres génériques de coût de la technologie qui sont constants ou changent sur l&#39;horizon du modèle (par exemple CAPEX, FOM, VOM)

.. .. _specifictec :

.. SpecificTech
.. +++++++++++++++++++

.. Affiche les paramètres technologiques spécifiques au site qui sont constants sur l&#39;horizon du modèle


.. La feuille ``SpecificTech`` est utilisée pour revoir et mettre à jour les paramètres de la technologie de production d&#39;énergie spécifiques au site qui ne varient pas d&#39;une année à l&#39;autre.

.. La feuille SpecificTech a un bouton supplémentaire : :button:`Add missing Tech`, qui permet à l&#39;utilisateur d&#39;ajouter une nouvelle technologie spécifique au site au modèle MESSAGE qui est lié. Actuellement cette technologie effectue l&#39;ajout en copiant les paramètres technologiques d&#39;une technologie générique du même type de technologie tel que spécifié par les 6 premiers caractères du nom de la technologie. Une nouvelle technologie sera automatiquement ajoutée à tous les scénarios actifs. Un code de technologie MESSAGE est créé automatiquement sur la base des produits d&#39;entrée et de sortie (tels que spécifiés par la technologie générique associée) et des technologies déjà existantes ayant les mêmes entrées et sorties.

.. Une fois qu&#39;une nouvelle technologie est ajoutée, ses paramètres doivent être mis à jour à l&#39;aide du bouton :button:`Mettre à jour les données du modèle`.



.. .. _specifictechhydrodams :

.. SpecificTechHydroDams
.. +++++++++++++++++++++++++++++++

.. Affiche les paramètres technologiques spécifiques au site qui sont spécifiques aux centrales hydroélectriques avec stockage (barrages)

.. La feuille ``SpecificTechHydroDams`` manipule les barrages hydrauliques dans le modèle.

.. Le bouton :button:`Refresh Sheet` extrait les technologies appartenant au `TechSetL2` : `Large Hydro Dams`.

.. Le bouton :button:`Create River Tech+Storage Constraint` ajoute une technologie et une contrainte de stockage pour chaque barrage.

.. :button:`Mettre à jour les données du modèle` met à jour les données d&#39;entrée de l&#39;utilisateur.


.. .. _coûts techniques spécifiques :

.. Coûts techniques spécifiques
.. ++++++++++++++++++++++++++

.. Affiche les paramètres de coût de la technologie spécifiques au site qui sont constants ou changent sur l&#39;horizon du modèle (par exemple CAPEX, FOM, VOM)

.. .. _limitesspécifiquesdecapacité :

.. LimitesDeCapacitéSpécifiques
.. +++++++++++++++++++++++++++++++++

.. Affiche les limites de capacité technologique spécifiques au site qui sont constantes ou changent sur l&#39;horizon du modèle

.. .. _stockagebatterie :

.. Stockage de la batterie
.. ++++++++++++++++++++

.. Affiche les paramètres de stockage de la batterie

.. .. _pvzones :

.. PVZones
.. ++++++++++

.. Affiche les données des zones PV

.. .. _zones de vent :

.. Zones de vent
.. ++++++++++++++

.. Affiche les données des zones de vent

.. .. _zones de vent offshore :

.. Zones de vent offshore
.. +++++++++++++++++++++++++

.. Affiche les données des zones de vent offshore

.. .. _csp6hrzones :

.. CSP6hrZones
.. ++++++++++++++++

.. Affiche les données des zones CSP 6 h

.. .. _csp12hrzones :

.. CSP12hrZones
.. ++++++++++++++++

.. Affiche les données des zones CSP 12 h

.. .. _interconnexions :

.. Interconnexions
.. +++++++++++++++++++++++

.. Affiche les paramètres de l&#39;interconnexion régionale

.. .. _transmission:

.. Transmission
.. ++++++++++++++++

.. Affiche les paramètres du réseau de transmission par pays

.. .. _distribution:

.. Distribution
.. ++++++++++++++++

.. Affiche les paramètres du réseau de distribution par pays et par secteur

.. _constraint_sheets :

Feuilles de contraintes
------------------------

Les contraintes sont des équations mathématiques linéaires applicables à plusieurs technologies (centrales électriques, stockage, transmission, etc.
Ce sont des relations définies par l&#39;utilisateur pour guider un modèle basé sur des récits de scénarios.
Dans MESSAGE, une contrainte est définie comme un produit somme d&#39;un coefficient et d&#39;une variable avec des limites supérieures ou inférieures définies par l&#39;utilisateur, comme indiqué ci-dessous :

.. image:: /images/constraint_form.PNG

Cette section décrit les différentes contraintes (y compris leurs équations et paramètres) présentes dans différentes feuilles de contraintes dans SPLAT.

.. _constraintlist_sheet :

Liste de contraintes
++++++++++++++++++++

Cette feuille contient la liste de toutes les contraintes du modèle qui sont définies dans les feuilles suivantes.

.. _buildlimconstraint_sheet :

PVAnnualBuildLim et WindAnnualBuildLim
++++++++++++++++++++++++++++++++++++++++++++++++++ +++

Ces deux feuilles sont utilisées pour fixer les limites annuelles de construction pour le solaire PV et l&#39;éolien terrestre respectivement.
La ou les équations utilisées dans la feuille sont les suivantes :

.. https://quicklatex.com/
.. https://www.overleaf.com/learn/latex/Integrals%2C_sums_and_limits
:math:`\sum\limits_{PV}Nouveau\, Capacité\, en\, année\, t_{PV} &lt;= PVBR\, en\, année\, t`

:math:`\sum\limits_{Vent}Nouveau\, Capacité\, en\, année\, t_{Vent} &lt;= VentBR\, en\, année\, t`

L&#39;équation suggère que la nouvelle capacité installée d&#39;énergie solaire photovoltaïque ou éolienne pour l&#39;année t devrait être inférieure aux taux de construction définis dans cette feuille.

Les paramètres utilisés dans cette fiche sont les suivants :

.. table-csv ::
:file: csv_file/buildlimconstraint_sheet.csv
:lignes d&#39;en-tête : 1
:widths: 20 20 10 50

.. note::
La cible (% de la demande de pointe), les valeurs Min et Max sont définies comme décision/suggestion de conception. Ces valeurs pourraient être rendues plus grandes ou plus petites.
On peut également créer des coefficients spécifiques à chaque pays en écrasant les formules des limites supérieures.

.. _rmconstraint_sheet :

ReserveMarginConstraint
+++++++++++++++++++++++++++++++++

Dans un système électrique, la production doit toujours être égale à la consommation.
Lorsque l&#39;équilibre est rompu, cela peut entraîner des pannes et des pannes complètes.
De nombreux événements peuvent perturber l&#39;équilibre (beaucoup d&#39;entre eux sont stochastiques/prévisibles avec probabilité) tels que la maintenance planifiée, les arrêts non planifiés, les changements/variations de la demande et les changements de l&#39;offre.
Par conséquent, des réserves sont nécessaires dans le système pour s&#39;assurer que la demande de puissance est toujours satisfaite.

Sur la base de la réponse (temps de réaction), réservé peut être classé comme :

je. Réserves primaires : partie de la capacité opérationnelle (courante) ou rapide à activer disponible immédiatement (en secondes) pour couvrir les perturbations.

ii. Réserve secondaire : peut être une capacité opérationnelle ou froide (non opérationnelle) à activer en quelques minutes (après la perturbation initiale et l&#39;activation de la réserve primaire, la réserve secondaire est activée et les unités sont réexpédiées afin de réactiver les capacités de la réserve primaire.)

iii. Réserve tertiaire : il s&#39;agit généralement d&#39;unités de secours qui peuvent être activées en quelques minutes/heures pour permettre la réactivation des capacités de réserve secondaire.

Dans le cadre MESSAGE, toutes les informations sur le système électrique actuel et futur sont supposées connues (avec une certitude à 100%), c&#39;est-à-dire non stochastiques, par conséquent, les décisions relatives au modèle de production doivent toujours être déterministes.
Lors de la modélisation du développement à long terme d&#39;un système électrique, un analyste doit s&#39;assurer que la capacité future est suffisante pour couvrir la demande pendant les périodes critiques (généralement pendant les heures de pointe) et pour couvrir les autres besoins opérationnels (par exemple, la maintenance).

.. note::
1. Il y a beaucoup de comportements stochastiques dans un système réel qui ne peuvent pas être capturés de la même manière dans le modèle.
2. Il est possible d&#39;effectuer une analyse avec divers modèles de disponibilité de la demande et de l&#39;offre et de modéliser des conditions opérationnelles extrêmes.

La marge de réserve est la marge de capacité ferme requise au-dessus de la demande/charge de pointe. Elle varie généralement entre 10 % et 25 % de la charge de pointe.
Par exemple, si une région a 12 GW de capacité ferme et 10 GW de demande de pointe, la marge de réserve serait de 20 %.

Marge de réserve (RM) = (Capacité ferme - Demande de pointe) / Demande de pointe

La représentation de la réserve système dans le cadre de modélisation MESSAGE est illustrée ci-dessous :

.. image:: /images/system_reserve_in_message.PNG

L&#39;équation de contrainte utilisée dans la feuille ``ReserveMarginConstraint`` est la suivante :

:math:`\sum\limits_{PP}(CapacityCredit_{PP} \times Capacity_{PP}) - \dfrac{1+RM}{1-LS} \cdot Capacity_{Ptnd} \geq 0`

où,

PP fait référence à toutes les centrales électriques applicables.

CapacityCredit_PP et Capacity_PP font référence au crédit de capacité et à la capacité installée de la centrale électrique.

RM = marge de réserve

Capacity_Pt&amp;d = Taille (MW) du réseau de transmission et de distribution utilisée comme approximation de la demande de pointe

LS = Pertes de transmission

&quot;ConCap_RM&quot; signifie Coefficient applicable sur la Capacité (MW) et associé à la contrainte de Marge de Réserve.

.. table-csv ::
:file: csv_file/rmconstraint_sheet.csv
:lignes d&#39;en-tête : 1
:widths: 20 20 10 50

.. note::
Contrairement à la contrainte de taux de construction, SPLAT exige que l&#39;utilisateur insère une contrainte de marge de réserve en tant que contrainte non chronologique, c&#39;est-à-dire une limite supérieure ou inférieure constante appliquée sur toutes les années de l&#39;horizon de modélisation.

.. _localreconstraint_sheet :

LocalREConstraint
+++++++++++++++++++++++++

Différents pays ou régions peuvent avoir pour objectif d&#39;atteindre une certaine part minimale d&#39;ER dans la production totale d&#39;électricité d&#39;ici une certaine année.
Dans la feuille ``LocalREConstraint``, la part minimale &quot;cible&quot; des technologies RE (plus précisément VRE) dans la production totale d&#39;électricité est définie comme une contrainte dans le modèle pour différentes années.
L&#39;équation représentant cette contrainte peut être représentée ci-dessous :

vres_gen &gt;= target_vres_share * total_gen

vres_gen - target_vres_share * total_gen &gt;= 0

vres_gen - target_vres_share * (vres_gen + other_gen) &gt;= 0

vres_gen - target_vres_share * vres_gen - target_vres_share * other_gen &gt;=0

(1 - target_vres_share) * vres_gen - target_vres_share * other_gen &gt;= 0

où,

vres_gen = génération issue de la technologie VRE

vres_share = part d&#39;ERV dans la production totale (total_gen) qui est définie comme la part cible minimale par un pays ou une région

other_gen = génération à partir de technologies non VRE

&quot;ConAct_RE&quot; fait référence au coefficient d&#39;Activité/Génération (GWh) d&#39;une technologie de centrale électrique.

.. table-csv ::
:file: csv_file/localreconstraint_sheet.csv
:lignes d&#39;en-tête : 1
:widths: 20 20 10 50


.. _co2constraint_sheet :

Contrainte CO2 :
++++++++++++++++++++

Les contraintes d&#39;émissions de CO2 sont fixées dans des scénarios plus ambitieux.
Dans cette fiche, l&#39;objectif de réduction des émissions de CO2 pour différentes années est fixé par rapport à un scénario de référence spécifique.
Cela fixe à son tour la limite supérieure des émissions de CO2 provenant de la production d&#39;électricité à partir de différentes technologies.
L&#39;équation de contrainte utilisée dans le modèle est la suivante :

:math:`\sum\limits_{PP}CO2_{PP, t} &lt;= MaxCO2_t`

où,

LHS représente la somme des émissions de CO2 du secteur de l&#39;électricité au cours de l&#39;année t.

RHS représente la limite maximale des émissions de CO2 du secteur de l&#39;électricité au cours de la même année t.

.. table-csv ::
:file: csv_file/co2constraint_sheet.csv
:lignes d&#39;en-tête : 1
:widths: 20 10 50


.. _reportgen_annual :

ReportGen-Annuel
------------------------

Cette feuille permet d&#39;exécuter le modèle et d&#39;obtenir des résultats en résolution annuelle.
Les étapes sont décrites dans :ref:`run_model`.

.. _reportgen_profiles :

ReportGen-Profils
-------------------------

Cette feuille permet de générer un fichier de résultats sous-annuel (profils). Les étapes sont décrites dans :ref:`extract_results`.

.. _timeslices :

Tranches de temps
---------------

Affiche les définitions de tranches de temps (régions de chargement) utilisées dans le modèle
