.. role:: inputcell
:class: inputcell
.. role:: interfacecell
:class: interfacecell
.. role:: button
:class: button

Description des feuilles
========================

.. _principal:

Principal
----------

D�finissez le chemin du mod�le, rechargez les donn�es du mod�le dans la m�moire et s�lectionnez les pays actifs pour l&#39;interrogation

:inputcell:`Model Folder` chemin du mod�le MESSAGE � connecter � l&#39;interface SPLAT

:inputcell:`R�gion principale` nom du mod�le MESSAGE � connecter � l&#39;interface SPLAT

:inputcell:`Region Active?` liste des sous-r�gions (pays) � charger en m�moire

:inputcell:`Scenarios to Load` liste des sc�narios actuellement sp�cifi�s dans la r�gion principale et pour sp�cifier les sc�narios � charger en m�moire

:interfacecell:`Country Name` codes pays dans le mod�le MESSAGE

:interfacecell:`Description` noms de pays d�velopp�s

:interfacecell:`Power Pool` le pool �nerg�tique auquel appartient un pays

:interfacecell:`TimeSlices/Load Regions` nombre de tranches de temps mod�lis�es par an

:interfacecell:`# Demands` nombre de composants de la demande

:interfacecell:`# Technologies` nombre de technologies dans le pays

:interfacecell:`# Contraintes` nombre de contraintes dans le pays

:interfacecell:`Scenarios` nom des sc�narios

:interfacecell:`Taux d&#39;actualisation` taux d&#39;actualisation des technologies

:button:`Reload Global` importe les donn�es du mod�le stock�es dans les fichiers adb et ldb dans la m�moire, effectue divers calculs.

:button:`Actualiser toutes les feuilles` rafra�chit les feuilles de donn�es (feuilles jaunes) pour les sous-r�gions et les sc�narios recharg�s

:button:`Enregistrer tous les fichiers de sc�nario en utilisant le formatage SPLAT` enregistrer tous les fichiers de mod�le (adb et ldb) en utilisant le formatage Excel-SPLAT pour les sous-r�gions s�lectionn�es (utilisez ceci apr�s avoir apport� une modification avec l&#39;interface MESSAGE)
Si vous appuyez sur ce bouton, les fichiers MAINa ldb seront �galement mis � jour si MAINa est s�lectionn�, pour exclure les interconnexions des sous-r�gions qui ne sont pas s�lectionn�es ci-dessous.

.. _input_sheets�:

Feuilles d&#39;entr�e
--------------

Cette section contient la liste des param�tres (ainsi que le code des param�tres, leur unit� et leurs d�finitions) pr�sents dans chaque feuille de saisie de l&#39;interface SPLAT.

.. note::
1. Les valeurs des param�tres se r�f�rent � la valeur du param�tre et au pays donn�, au sc�nario donn� et � la ou aux ann�es donn�es.
2. Si aucune ann�e n&#39;est mentionn�e dans la feuille de saisie, la valeur est constante pour toutes les ann�es.
3. Si les feuilles d&#39;entr�e contiennent uniquement des espaces r�serv�s et des ann�es sp�cifiques, les valeurs du param�tre et les ann�es interm�diaires sont interpol�es lin�airement.
4. Les co�ts sont fournis en termes de valeurs de l&#39;ann�e de r�f�rence (2019 � ce jour).

.. _demand_sheet�:

Demande
+++++++++++++++++++++

.. table-csv ::
:file: csv_file/demand_sheet.csv
:lignes d&#39;en-t�te�: 1
:widths: 20 10 50

.. _peakdemand_sheet�:

Pic de demande
+++++++++++++++
.. table-csv ::
:file: csv_file/peakdemand_sheet.csv
:lignes d&#39;en-t�te�: 1
:widths: 20 10 50

.. _t&amp;d_sheet�:

Transport et distribution
++++++++++++++++++++++++++++++++

.. table-csv ::
:file: csv_file/t&amp;d_sheet.csv
:lignes d&#39;en-t�te�: 1
:widths: 20 10 50

.. note::
Pour la distribution, les valeurs doivent �tre saisies pour les types de distribution urbaine, rurale, industrielle et commerciale.

.. _fuelprices_sheet�:

Prix du carburant
+++++++++++++++++++++
.. table-csv ::
:file: csv_file/fuelprices_sheet.csv
:lignes d&#39;en-t�te�: 1
:widths: 20 10 50

.. _tech_sheet�:

GenericTech et SpecificTech
++++++++++++++++++++++++++++

La feuille ``GenericTech`` affiche les param�tres technologiques g�n�riques qui sont constants sur l&#39;horizon du mod�le

La feuille ``SpecificTech`` est utilis�e pour examiner et mettre � jour les param�tres de la technologie de production d&#39;�nergie sp�cifiques au site qui ne varient pas d&#39;une ann�e � l&#39;autre.
La feuille ``SpecificTech`` a un bouton suppl�mentaire�: :button:`Add missing Tech`, qui permet � l&#39;utilisateur d&#39;ajouter une nouvelle technologie sp�cifique au site au mod�le MESSAGE qui est li�. Actuellement cette technologie effectue l&#39;ajout en copiant les param�tres technologiques d&#39;une technologie g�n�rique du m�me type de technologie tel que sp�cifi� par les 6 premiers caract�res du nom de la technologie. Une nouvelle technologie sera automatiquement ajout�e � tous les sc�narios actifs. Un code de technologie MESSAGE est cr�� automatiquement sur la base des produits d&#39;entr�e et de sortie (tels que sp�cifi�s par la technologie g�n�rique associ�e) et des technologies d�j� existantes ayant les m�mes entr�es et sorties.
Une fois qu&#39;une nouvelle technologie est ajout�e, ses param�tres doivent �tre mis � jour � l&#39;aide du bouton :button:`Mettre � jour les donn�es du mod�le`.

.. table-csv ::
:file: csv_file/tech_sheet.csv
:lignes d&#39;en-t�te�: 1
:widths: 20 20 10 50

.. note::
1. Les profils/courbes de charge sont calcul�s par SPLAT sur la base des valeurs horaires (8760) pr�sentes dans le fichier *.tit du dossier de donn�es. Ils sont stock�s dans les fichiers adb, ldb et ldr. La raison pour laquelle ils ne figurent pas dans la feuille de calcul est qu&#39;ils varient en fonction de la d�finition de la r�gion de chargement/de la tranche de temps (par exemple, grand mod�le/petit mod�le) et qu&#39;il serait tr�s difficile de les g�rer efficacement dans une feuille de calcul.

2. ** Param�tres pertinents pour la feuille ``SpecificTech`` uniquement.

.. _techcosts_sheet�:

GenericTechCosts et SpecificTechCosts
+++++++++++++++++++++++++++++++++++++++

Ces feuilles affichent les param�tres de co�t qui sont constants ou changent sur l&#39;horizon du mod�le.

.. table-csv ::
:file: csv_file/techcosts_sheet.csv
:lignes d&#39;en-t�te�: 1
:widths: 20 10 50

.. _specifictechhydrodams_sheet�:

SpecificTechHydroDams
+++++++++++++++++++++

Cette fiche affiche les param�tres technologiques sp�cifiques au site qui sont sp�cifiques aux centrales hydro�lectriques avec stockage (barrages).
La feuille ``SpecificTechHydroDams`` manipule les barrages hydro�lectriques dans le mod�le.
Le bouton :button:`Refresh Sheet` extrait les technologies appartenant au `TechSetL2`�: `Large Hydro Dams`.
Et le bouton :button:`Create River Tech+Storage Constraint` ajoute une technologie et une contrainte de stockage pour chaque barrage.
Le :button:`Mettre � jour les donn�es du mod�le` met � jour les donn�es d&#39;entr�e de l&#39;utilisateur.

.. table-csv ::
:file: csv_file/specifictechhydrodams_sheet.csv
:lignes d&#39;en-t�te�: 1
:widths: 20 20 10 50

.. _batterie&amp;pumpstorage_sheet�:

Stockage de la batterie et de la pompe
+++++++++++++++++++++

.. table-csv ::
:file: csv_file/batterie&amp;pumpstorage_sheet.csv
:lignes d&#39;en-t�te�: 1
:widths: 20 20 10 50

.. _interconnectors_sheet�:

Interconnexions
+++++++++++++++++++++

.. table-csv ::
:file: csv_file/interconnectors_sheet.csv
:lignes d&#39;en-t�te�: 1
:widths: 20 20 10 50

.. _caplimits_sheet�:

SpecificCapacityLimits et InterconnectorsCapLimits
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. table-csv ::
:file: csv_file/caplimits_sheet.csv
:lignes d&#39;en-t�te�: 1
:widths: 20 10 50

.. _vrezones_sheet�:

PVZones, WindZones, OffshoreWindZones, CSP6hrZones et CSP12hrZones
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. table-csv ::
:file: csv_file/vrezones_sheet.csv
:lignes d&#39;en-t�te�: 1
:widths: 20 20 10 50

.. note::
1. Les donn�es de latitude et de longitude peuvent �tre stock�es dans les fichiers adb avec le reste des donn�es d&#39;entr�e du mod�le. Il n&#39;est pas utilis� par SPLAT ou MESSAGE pour quoi que ce soit, mais il peut �tre utilis� par les visualiseurs de r�sultats pour l&#39;affichage sur des cartes (par exemple dans Tableau).

2. Pour les param�tres d&#39;investissement compensatoire et d&#39;investissement multiplicateur, il ne faut pas oublier d&#39;utiliser l&#39;option d�roulante &quot;R�initialiser l&#39;investissement&quot; dans la cellule F6, lorsque les co�ts g�n�riques sont mis � jour pour une raison quelconque, ou avant qu&#39;une mise � jour ne soit effectu�e dans les donn�es MSR brutes, avant -l&#39;application de &quot;l&#39;Investissement Offset&quot;.

3. Le param�tre d&#39;investissement multiplicateur (selon la classe de turbine) se trouve uniquement dans la feuille ``WindZones``. Cette cat�gorisation ne s&#39;applique pas � l&#39;offshore car il est suppos� que toutes les �oliennes offshore sont de la m�me classe.

.. .. _demande:

.. Demande
.. ++++++++

.. Affiche toutes les s�ries de demande dans le mod�le, y compris la demande totale &quot;envoy�e&quot; (c&#39;est-�-dire secondaire, ou avant la transmission et la distribution) et la demande finale par secteur

.. .. _picdedemande�:

.. Pic de demande
.. ++++++++++++++++

.. Affiche les s�ries de demande de pointe en MW dans le mod�le, y compris la demande totale &quot;envoy�e&quot; (c&#39;est-�-dire secondaire, ou avant la transmission et la distribution) et la demande finale par secteur

.. .. _Prix du carburant:

.. Prix du carburant
.. ------------------

.. Affiche les prix des carburants utilis�s dans le mod�le

.. .. _fichestechniques�:

.. Fiches techniques
.. ------------------

.. .. _generictech�:

.. GenericTech
.. +++++++++++

.. Affiche les param�tres technologiques g�n�riques qui sont constants sur l&#39;horizon du mod�le

.. .. _generictechcosts�:

.. Co�ts techniques g�n�riques
.. ++++++++++++++++++++++++++++

.. Affiche les param�tres g�n�riques de co�t de la technologie qui sont constants ou changent sur l&#39;horizon du mod�le (par exemple CAPEX, FOM, VOM)

.. .. _specifictec�:

.. SpecificTech
.. +++++++++++++++

.. Affiche les param�tres technologiques sp�cifiques au site qui sont constants sur l&#39;horizon du mod�le


.. La feuille ``SpecificTech`` est utilis�e pour revoir et mettre � jour les param�tres de la technologie de production d&#39;�nergie sp�cifiques au site qui ne varient pas d&#39;une ann�e � l&#39;autre.

.. La feuille SpecificTech a un bouton suppl�mentaire�: :button:`Add missing Tech`, qui permet � l&#39;utilisateur d&#39;ajouter une nouvelle technologie sp�cifique au site au mod�le MESSAGE qui est li�. Actuellement cette technologie effectue l&#39;ajout en copiant les param�tres technologiques d&#39;une technologie g�n�rique du m�me type de technologie tel que sp�cifi� par les 6 premiers caract�res du nom de la technologie. Une nouvelle technologie sera automatiquement ajout�e � tous les sc�narios actifs. Un code de technologie MESSAGE est cr�� automatiquement sur la base des produits d&#39;entr�e et de sortie (tels que sp�cifi�s par la technologie g�n�rique associ�e) et des technologies d�j� existantes ayant les m�mes entr�es et sorties.

.. Une fois qu&#39;une nouvelle technologie est ajout�e, ses param�tres doivent �tre mis � jour � l&#39;aide du bouton :button:`Mettre � jour les donn�es du mod�le`.



.. .. _specifictechhydrodams�:

.. SpecificTechHydroDams
.. +++++++++++++++++++++++

.. Affiche les param�tres technologiques sp�cifiques au site qui sont sp�cifiques aux centrales hydro�lectriques avec stockage (barrages)

.. La feuille ``SpecificTechHydroDams`` manipule les barrages hydrauliques dans le mod�le.

.. Le bouton :button:`Refresh Sheet` extrait les technologies appartenant au `TechSetL2`�: `Large Hydro Dams`.

.. Le bouton :button:`Create River Tech+Storage Constraint` ajoute une technologie et une contrainte de stockage pour chaque barrage.

.. :button:`Mettre � jour les donn�es du mod�le` met � jour les donn�es d&#39;entr�e de l&#39;utilisateur.


.. .. _co�ts techniques sp�cifiques�:

.. Co�ts techniques sp�cifiques
.. ++++++++++++++++++++++++++++++++

.. Affiche les param�tres de co�t de la technologie sp�cifiques au site qui sont constants ou changent sur l&#39;horizon du mod�le (par exemple CAPEX, FOM, VOM)

.. .. _limitessp�cifiquesdecapacit�:

.. LimitesDeCapacit�Sp�cifiques
.. +++++++++++++++++++++++++++++

.. Affiche les limites de capacit� technologique sp�cifiques au site qui sont constantes ou changent sur l&#39;horizon du mod�le

.. .. _stockagebatterie�:

.. Stockage de la batterie
.. ++++++++++++++

.. Affiche les param�tres de stockage de la batterie

.. .. _pvzones�:

.. PVZones
.. ++++++++

.. Affiche les donn�es des zones PV

.. .. _zones de vent�:

.. Zones de vent
.. ++++++++++++++

.. Affiche les donn�es des zones de vent

.. .. _zones de vent offshore�:

.. Zones de vent offshore
.. +++++++++++++++++++++++

.. Affiche les donn�es des zones de vent offshore

.. .. _csp6hrzones�:

.. CSP6hrZones
.. ++++++++++++

.. Affiche les donn�es des zones CSP 6 h

.. .. _csp12hrzones�:

.. CSP12hrZones
.. ++++++++++++

.. Affiche les donn�es des zones CSP 12 h

.. .. _interconnexions�:

.. Interconnexions
.. +++++++++++++++++

.. Affiche les param�tres de l&#39;interconnexion r�gionale

.. .. _transmission:

.. Transmission
.. ++++++++++++

.. Affiche les param�tres du r�seau de transmission par pays

.. .. _distribution:

.. Distribution
.. ++++++++++++

.. Affiche les param�tres du r�seau de distribution par pays et par secteur

.. _constraint_sheets�:

Feuilles de contraintes
-----------------

Les contraintes sont des �quations math�matiques lin�aires applicables � plusieurs technologies (centrales �lectriques, stockage, transmission, etc.
Ce sont des relations d�finies par l&#39;utilisateur pour guider un mod�le bas� sur des r�cits de sc�narios.
Dans MESSAGE, une contrainte est d�finie comme un produit somme d&#39;un coefficient et d&#39;une variable avec des limites sup�rieures ou inf�rieures d�finies par l&#39;utilisateur, comme indiqu� ci-dessous�:

.. image:: /images/constraint_form.PNG

Cette section d�crit les diff�rentes contraintes (y compris leurs �quations et param�tres) pr�sentes dans diff�rentes feuilles de contraintes dans SPLAT.

.. _constraintlist_sheet�:

Liste de contraintes
++++++++++++++++

Cette feuille contient la liste de toutes les contraintes du mod�le qui sont d�finies dans les feuilles suivantes.

.. _buildlimconstraint_sheet�:

PVAnnualBuildLim et WindAnnualBuildLim
+++++++++++++++++++++++++++++++++++++++

Ces deux feuilles sont utilis�es pour fixer les limites annuelles de construction pour le solaire PV et l&#39;�olien terrestre respectivement.
La ou les �quations utilis�es dans la feuille sont les suivantes�:

Somme(NewCapacity_PV, t) &lt;= PVBR_RHS(t)

Somme(NewCapacity_Wind, t) &lt;= WindBR_RHS(t)

L&#39;�quation sugg�re que la nouvelle capacit� install�e d&#39;�nergie solaire PV ou �olienne pour un pays donn� pour une ann�e donn�e devrait �tre inf�rieure aux limites sup�rieures d�finies dans cette feuille.

Les param�tres utilis�s dans cette fiche sont les suivants :

.. table-csv ::
:file: csv_file/buildlimconstraint_sheet.csv
:lignes d&#39;en-t�te�: 1
:widths: 20 20 10 50

.. note::
La cible (% de la demande de pointe), les valeurs Min et Max sont d�finies comme d�cision/suggestion de conception. Ces valeurs pourraient �tre rendues plus grandes ou plus petites.
On peut �galement cr�er des coefficients sp�cifiques � chaque pays en �crasant les formules des limites sup�rieures.

.. _rmconstraint_sheet�:

ReserveMarginConstraint
+++++++++++++++++++++++++

Dans un syst�me �lectrique, la production doit toujours �tre �gale � la consommation.
Lorsque l&#39;�quilibre est rompu, cela peut entra�ner des pannes et des pannes compl�tes.
De nombreux �v�nements peuvent perturber l&#39;�quilibre (beaucoup d&#39;entre eux sont stochastiques/pr�visibles avec probabilit�) tels que la maintenance planifi�e, les arr�ts non planifi�s, les changements/variations de la demande et les changements de l&#39;offre.
Par cons�quent, des r�serves sont n�cessaires dans le syst�me pour s&#39;assurer que la demande de puissance est toujours satisfaite.

Sur la base de la r�ponse (temps de r�action), r�serv� peut �tre class� comme�:

je. R�serves primaires : partie de la capacit� op�rationnelle (courante) ou rapide � activer disponible imm�diatement (en secondes) pour couvrir les perturbations.

ii. R�serve secondaire : peut �tre une capacit� op�rationnelle ou froide (non op�rationnelle) � activer en quelques minutes (apr�s la perturbation initiale et l&#39;activation de la r�serve primaire, la r�serve secondaire est activ�e et les unit�s sont r�exp�di�es afin de r�activer les capacit�s de la r�serve primaire.)

iii. R�serve tertiaire : il s&#39;agit g�n�ralement d&#39;unit�s de secours qui peuvent �tre activ�es en quelques minutes/heures pour permettre la r�activation des capacit�s de r�serve secondaire.

Dans le cadre MESSAGE, toutes les informations sur le syst�me �lectrique actuel et futur sont suppos�es connues (avec une certitude � 100%), c&#39;est-�-dire non stochastiques, par cons�quent, les d�cisions relatives au mod�le de production doivent toujours �tre d�terministes.
Lors de la mod�lisation du d�veloppement � long terme d&#39;un syst�me �lectrique, un analyste doit s&#39;assurer que la capacit� future est suffisante pour couvrir la demande pendant les p�riodes critiques (g�n�ralement pendant les heures de pointe) et pour couvrir les autres besoins op�rationnels (par exemple, la maintenance).

.. note::
1. Il y a beaucoup de comportements stochastiques dans un syst�me r�el qui ne peuvent pas �tre captur�s de la m�me mani�re dans le mod�le.
2. Il est possible d&#39;effectuer une analyse avec divers mod�les de disponibilit� de la demande et de l&#39;offre et de mod�liser des conditions op�rationnelles extr�mes.

La marge de r�serve est la marge de capacit� ferme requise au-dessus de la demande/charge de pointe. Elle varie g�n�ralement entre 10 % et 25 % de la charge de pointe.
Par exemple, si une r�gion a 12 GW de capacit� ferme et 10 GW de demande de pointe, la marge de r�serve serait de 20 %.

Marge de r�serve (RM) = (Capacit� ferme - Demande de pointe) / Demande de pointe

La repr�sentation de la r�serve syst�me dans le cadre de mod�lisation MESSAGE est illustr�e ci-dessous�:

.. image:: /images/system_reserve_in_message.PNG

L&#39;�quation de contrainte utilis�e dans la feuille ``ReserveMarginConstraint`` est la suivante�:

:math:`\sum\limits_{PP}(CapacityCredit_{PP} \times Capacity_{PP}) - \dfrac{1+RM}{1-LS} \cdot Capacity_{Ptnd} \geq 0`

o�,

CapacityCredit_PP et Capacity_PP font r�f�rence au cr�dit de capacit� et � la capacit� install�e de la centrale �lectrique.

RM = marge de r�serve

LS = Pertes de transmission

Capacity_Pt&amp;d = Capacit� de transport et de distribution

&quot;ConCap_RM&quot; signifie Coefficient applicable sur la Capacit� (MW) et associ� � la contrainte de Marge de R�serve

.. table-csv ::
:file: csv_file/rmconstraint_sheet.csv
:lignes d&#39;en-t�te�: 1
:widths: 20 20 10 50

.. _localreconstraint_sheet�:

LocalREConstraint
+++++++++++++++++++

Diff�rents pays ou r�gions peuvent avoir pour objectif d&#39;atteindre une certaine part minimale d&#39;ER dans la production totale d&#39;�lectricit� d&#39;ici une certaine ann�e.
Dans la feuille ``LocalREConstraint``, la part minimale des technologies RE (plus sp�cifiquement VRE) dans la production totale d&#39;�lectricit� est d�finie comme une contrainte dans le mod�le pour diff�rentes ann�es.
L&#39;�quation repr�sentant cette contrainte peut �tre repr�sent�e ci-dessous :

vres_gen &gt;= vres_share * total_gen

vres_gen &gt;= vres_share * (vres_gen + other_gen)

vres_gen - vres_share * vres_gen - vres_share * other_gen &gt;=0

(1 - vres_share) * vres_gen - vres_share * other_gen &gt;= 0

o�,

vres_gen = g�n�ration issue de la technologie VRE

vres_share = part d&#39;ERV dans la production totale (total_gen) qui est d�finie comme la part cible minimale par un pays ou une r�gion

other_gen = g�n�ration � partir de technologies non VRE

&quot;ConAct_RE&quot; fait r�f�rence au coefficient d&#39;Activit�/G�n�ration (GWh) d&#39;une technologie de centrale �lectrique.

.. table-csv ::
:file: csv_file/localreconstraint_sheet.csv
:lignes d&#39;en-t�te�: 1
:widths: 20 20 10 50


.. _co2constraint_sheet�:

Contrainte CO2 :
++++++++++++++++

Les contraintes d&#39;�missions de CO2 sont fix�es dans des sc�narios plus ambitieux.
Dans cette fiche, l&#39;objectif de r�duction des �missions de CO2 pour diff�rentes ann�es est fix� par rapport � un sc�nario de r�f�rence pr�cis.
Cela fixe � son tour la limite sup�rieure des �missions de CO2 provenant de la production d&#39;�lectricit� � partir de diff�rentes technologies.
L&#39;�quation de contrainte utilis�e dans le mod�le est la suivante�:

Somme(CO2_PP, t) &lt;= Max_CO2_PP(t)

o�,

LHS repr�sente la somme des �missions de CO2 du secteur de l&#39;�lectricit� au cours de l&#39;ann�e t.

RHS repr�sente la limite maximale des �missions de CO2 du secteur de l&#39;�lectricit� au cours de la m�me ann�e t.

.. table-csv ::
:file: csv_file/co2constraint_sheet.csv
:lignes d&#39;en-t�te�: 1
:widths: 20 10 50


.. _reportgen_annual�:

ReportGen-Annuel
-----------------

Cette feuille permet d&#39;ex�cuter le mod�le et d&#39;obtenir des r�sultats en r�solution annuelle.
Les �tapes sont d�crites dans :ref:`run_model`.

.. _reportgen_profiles�:

ReportGen-Profils
-------------------

Cette feuille permet de g�n�rer un fichier de r�sultats sous-annuel (profils). Les �tapes sont d�crites dans :ref:`extract_results`.

.. _timeslices�:

Tranches de temps
-----------------

Affiche les d�finitions de tranches de temps (r�gions de chargement) utilis�es dans le mod�le
