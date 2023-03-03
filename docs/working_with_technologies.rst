.. role:: inputcell
:class: inputcell
.. role:: interfacecell
:class: interfacecell
.. role:: button
:class: button


Travailler avec les technologies
=================================

.. important::
L&#39;interface doit �tre li�e au mod�le avant d&#39;ex�cuter l&#39;une des �tapes de cette section.
Voir :ref:`link_interface`.

Une technologie dans le mod�le est une unit� de production d&#39;�lectricit� ou une combinaison de ces unit�s ou une ligne de transmission avec des param�tres sp�cifiques tels que la capacit� maximale, le facteur de capacit�, le CAPEX, le FOM, le co�t du carburant, etc.

Une technologie peut �tre sp�cifique � un site (une centrale ou une ligne de transmission sp�cifique avec des param�tres connus) ou g�n�rique (une technologie avec des param�tres g�n�ralis�s).
Les technologies dans SPLAT sont class�es en quatre types principaux�:

**1. Existing technologies:** Les technologies qui sont d�j� en place � partir de l&#39;ann�e de r�f�rence.

**2. Committed technologies:** Les technologies en cours de construction ou dont la mise en �uvre a �t� approuv�e. Le d�ploiement de ces technologies peut �tre consid�r� comme garanti dans les r�sultats du mod�le.

**3. Candidate technologies:** Les technologies qui peuvent ou non �tre mises en service � long terme et donc faire partie du processus d&#39;optimisation. Les caract�ristiques de ces projets (taille, emplacement, technologie, etc.) doivent �tre coh�rentes avec les infrastructures existantes, l&#39;�volution des prix et le potentiel des ressources �nerg�tiques.
Le mod�le les s�lectionnera s&#39;ils pr�sentent un avantage net pour le syst�me �lectrique mod�lis�, ce qui implique que leur construction, leur exploitation et leur maintenance devraient minimiser le co�t total de l&#39;expansion du syst�me �lectrique.

Le mod�le SPLAT Africa utilis� dans le projet Continental Power System Master Plan (CMP) utilise le mod�le �nerg�tique � supply regions � (MSR).
MSR comprend des options d&#39;approvisionnement solaire PV g�or�f�renc�es, solaires CSP, �oliennes terrestres et offshore con�ues par l&#39;IRENA gr�ce � une analyse g�ospatiale syst�matique expliqu�e dans cet article.<https://www.nature.com/articles/s41597-022-01786-5> `_.
Ces technologies d&#39;�nergies renouvelables variables sont �galement consid�r�es comme des technologies candidates.

**4. Generic technologies:** Ces technologies ne sont pas sp�cifiques au site. Ils ont des param�tres g�n�ralis�s. � l&#39;instar des technologies candidates, ces technologies font �galement partie du processus d&#39;optimisation. Le mod�le s�lectionnerait ces technologies si elles pr�sentent un avantage net pour le syst�me �lectrique mod�lis�.

Les technologies g�n�riques sont normalement configur�es de mani�re � ne pas �tre mises en ligne dans des sc�narios de r�f�rence. L&#39;une des principales motivations pour avoir des technologies g�n�riques dans le mod�le est de rendre le mod�le ind�pendant de la technologie, ce qui � son tour augmente l&#39;acceptation parmi les parties prenantes.

Les onglets Technologie sont r�pertori�s dans :ref:`technologysheets`

Cette section d�crit comment afficher, ajouter et modifier des technologies � l&#39;aide de l&#39;interface SPLAT Excel.


.. _view_tech_inputs�:

Affichage des entr�es technologiques
--------------------------------------

1. Dans l&#39;une des :ref:`fiches technologiques` (� l&#39;exception des onglets contenant des informations sur des zones sp�cifiques), saisissez le sc�nario � interroger dans la cellule ``Choisir un sc�nario``

2. Cliquez sur :button:`Actualiser la feuille`. Les technologies et leurs param�tres dans le sc�nario seront pr�sent�s dans la m�me feuille. Seules les donn�es du ou des pays charg�s (dans la feuille ``Principal``) seront affich�es.

3. Reportez-vous � :ref:`renewable_tech` pour conna�tre les �tapes de r�cup�ration des informations sur les zones renouvelables (Solar PV, Solar CSP, Onshore Wind, Offshore Wind).

.. _add_tech�:

Ajouter une technologie
------------------------

1. Actualisez la feuille :ref:`SpecificTech` pour le sc�nario s�lectionn�.

2. Ajoutez un nouveau nom de technologie sp�cifique et des param�tres dans le tableau. Assurez-vous que le code de technologie est unique et non r�p�t�.

3. Cliquez sur :button:`Ajouter de nouveaux techniciens`. Une technologie est ajout�e avec les param�tres de la technologie g�n�rique sous-jacente.

4. Actualisez la feuille pour voir la nouvelle technologie ajout�e. Actualisez les autres feuilles avant de modifier les param�tres pertinents.

.. note::
Les technologies de stockage de batterie et de pompe doivent �tre d�finies s�par�ment dans la feuille :ref:`Battery&amp;PumpStorage` dans l&#39;interface SPLAT.

.. _rename_tech�:

Renommer une technologie
--------------------------

1. Entrez les anciens et nouveaux noms de technologie dans :ref:`RenameTechFacility` et cliquez sur :button:`Rename Techs in List`.

2. Pour confirmer que la technologie a �t� renomm�e, actualisez les onglets correspondants (``GenericTech`` ou ``SpecificTech``) pour voir les noms mis � jour. Plusieurs technologies peuvent �tre renomm�es.

.. image:: /images/technology_rename.PNG

.. _delete_tech�:

Suppression d&#39;une technologie
----------------------

1. Entrez les noms des technologies dans :ref:`DeleteTechFacility` et cliquez sur :button:`Delete Techs in List`.

2. Pour confirmer que la technologie a bien �t� supprim�e, actualisez les onglets correspondants (``GenericTech`` ou ``SpecificTech``) pour voir la mise � jour. Plusieurs technologies peuvent �tre supprim�es.

.. image:: /images/technology_delete.PNG

.. _change_tech�:

Changer de technologie
----------------------

1. Dans l&#39;une des :ref:`fiches techniques` (� l&#39;exception des onglets contenant des informations sur des zones sp�cifiques), cliquez sur :button:`Actualiser la feuille` pour obtenir les donn�es enregistr�es dans le mod�le pour le sc�nario choisi.

2. Apportez des modifications aux technologies de la feuille.

3. Cliquez sur :button:`Mettre � jour les donn�es du mod�le` pour mettre � jour le mod�le avec les nouvelles donn�es.

.. _carburant:

Prix du carburant
------------------

1. Dans l&#39;onglet :ref:`fuelprices`, cliquez sur :button:`Refresh Sheet` pour obtenir les donn�es enregistr�es dans le mod�le pour le sc�nario et les pays choisis.

2. Modifiez les prix du carburant dans la feuille.

3. Cliquez sur :button:`Mettre � jour les donn�es du mod�le` pour mettre � jour le mod�le avec les nouvelles donn�es.

.. note::
1. Le prix du carburant est indiqu� en $/GJ. Il n&#39;est actuellement pas possible d&#39;ajouter de nouvelles technologies d&#39;approvisionnement en carburant via l&#39;interface SPLAT, cela est laiss� pour un d�veloppement futur (ainsi que la possibilit� de sp�cifier des limites, qui seraient n�cessaires si l&#39;on voulait mod�liser une courbe d&#39;approvisionnement pour un carburant particulier).
2. Si un utilisateur sp�cifie des valeurs � la fois dans la colonne Constante et dans les colonnes de l&#39;ann�e du jalon, seule la valeur constante sera utilis�e pour mettre � jour le mod�le MESSAGE et les autres valeurs seront ignor�es.

.. _tech_cost�:

Co�ts technologiques
--------------------

1. Dans l&#39;onglet :ref:`generictechcosts` et :ref:`specifictechcosts`, cliquez sur :button:`Refresh Sheet` pour obtenir les donn�es de co�ts enregistr�es dans le mod�le pour le sc�nario et les pays choisis.

2. Modifiez les co�ts (co�t de nuit-$/kW, co�t fixe d&#39;O&amp;M-$/kW, co�t variable d&#39;O&amp;M-$/MWh) dans la feuille.

3. Cliquez sur :button:`Mettre � jour les donn�es du mod�le` pour mettre � jour le mod�le avec les nouvelles donn�es.

.. note::
Si un utilisateur sp�cifie des valeurs � la fois dans la colonne Constante et dans les colonnes de l&#39;ann�e du jalon, seule la valeur constante sera utilis�e pour mettre � jour le mod�le MESSAGE et les autres valeurs seront ignor�es.

.. _tech_capacity�:

Limite de capacit�
------------------------------

1. Dans l&#39;onglet :ref:`specificcapacitylimits`, cliquez sur :button:`Refresh Sheet` pour obtenir les limites de capacit� enregistr�es dans le mod�le pour le sc�nario et les pays choisis.

2. Modifiez les limites de capacit� dans la feuille.

3. Cliquez sur :button:`Mettre � jour les donn�es du mod�le` pour mettre � jour le mod�le avec les nouvelles donn�es.

.. note::
1. Il n&#39;y a pas de limite de capacit� pour les technologies g�n�riques.
2. Si un utilisateur sp�cifie des valeurs � la fois dans la colonne Constante et dans les colonnes de l&#39;ann�e du jalon, seule la valeur constante sera utilis�e pour mettre � jour le mod�le MESSAGE et les autres valeurs seront ignor�es.

.. _renewable_tech�:

Technologies renouvelables et de stockage
------------------------------------------

.. _solar_wind�:

Solaire PV, �olien onshore et offshore
+++++++++++++++++++++++++++++++++++++++

Les technologies VRE peuvent �tre d�finies de deux mani�res : soit comme des technologies g�n�riques, soit comme des technologies sp�cifiques � un site. Vous trouverez ci-dessous un exemple d&#39;ajout d&#39;�olien offshore, d&#39;abord en tant que technologie g�n�rique, puis en tant que zones.

1. Dans l&#39;onglet :ref:`GenericTech`, ajoutez la technologie &quot;XXWDLCO00&quot; (XX �tant l&#39;ID du pays, par exemple DZ) avec la description de la technologie &quot;Technologie g�n�rique offshore&quot;. Utilisez le bouton Ajouter une nouvelle technologie. La macro mettra � jour les fichiers sous-jacents et se rechargera � la fin.

2. Acc�dez � la feuille :ref:`RenameTechFacility`. Remplacez les technologies offshore nouvellement ajout�es par le nom de technologie g�n�rique appropri�, c&#39;est-�-dire XXWDOC00. La macro mettra � jour les fichiers sous-jacents et se rechargera � la fin.

3. Acc�dez � la feuille :ref:`OffshoreWindZones`. Ajoutez de nouvelles technologies dans chaque pays. Cliquez sur :button:`Ajouter de nouveaux techniciens`. La macro mettra � jour les fichiers sous-jacents et se rechargera � la fin.

4. Localisez le fichier .tit du mod�le et ouvrez-le en tant qu&#39;Excel, il vous demandera le param�tre de d�limitation. S�lectionnez virgule. Les zones g�n�riques �oliennes offshore et offshore nouvellement ajout�es auront les m�mes profils. Maintenant, allez � la feuille :ref:`OffshoreWindZones`. Donnez l&#39;adresse au fichier qui contient les profils, dans la section fichier de donn�es MSR. Cela mettra � jour les profils de zone dans le fichier .tit. Actuellement, la technologie g�n�rique �olienne offshore a le m�me profil que l&#39;�olien g�n�rique. Mais rappelez-vous, la technologie g�n�rique �olienne terrestre a �t� �vinc�e du mod�le en d�finissant la premi�re ann�e = 2050

5. Les profils mis � jour dans le fichier .tit doivent �tre ins�r�s dans les fichiers mod�les. Acc�dez � la feuille :ref:`TimeSlices`, appuyez sur :button:`Update Files`.


.. _hydro_dam�:

Barrage hydro�lectrique
++++++++++++++++++++++++++++++

La feuille ``SpecificTechHydroDams`` manipule les barrages hydro�lectriques dans le mod�le.

1. Cliquez sur le bouton :button:`Refresh Sheet` pour extraire les technologies appartenant au `TechSetL2`�: `Large Hydro Dams`.

2. Le bouton :button:`Create River Tech+Storage Constraint` ajoute une technologie et une contrainte de stockage pour chaque barrage.

Une nouvelle technologie factice pour chaque centrale hydro�lectrique avec barrage est ajout�e pour mod�liser les apports de la rivi�re au barrage. La convention de d�nomination de la technologie factice est XXRIDM_rivername, par exemple CMRIDM_LAGDO (en utilisant LAGDO comme exemple). La sortie est r�gl�e sur la forme d&#39;�nergie elc fictive existante.

Une nouvelle contrainte de stockage est ajout�e, exemple D_LAGDO avec le nom abr�g� DXXX. La contrainte de stockage est li�e � CMRIDM_LAGDO avec un coefficient de +1, donc chaque flux de MWyr de CMRIDM_LAGDO augmente le contenu de stockage de 1 MWyr.

La contrainte de stockage est li�e � CMHYDM_LAGDO avec un coefficient -1 (c&#39;est-�-dire que chaque flux de MWyr de CMHYDM_LAGDO diminue le contenu du stockage de 1 MWyr). Il serait en th�orie possible de faire une mod�lisation en cascade en liant le d�bit des usines amont � des contraintes de stockage en aval (plut�t qu&#39;une technologie fluviale). Les coefficients devraient �tre mis � l&#39;�chelle par &quot;l&#39;�nergie par unit� de volume (MJ/m3)&quot; relative des usines en amont et en aval. Cette fonctionnalit� devra �tre revisit�e en tant que nouvelle t�che de d�veloppement s&#39;il y a un besoin pressant.

L&#39;utilisateur doit sp�cifier 2 param�tres, dont les valeurs peuvent �tre calcul�es dans le tableau le plus � droite et copi�es-coll�es.

3. Une fois cela fait, l&#39;utilisateur peut cliquer sur :button:`Mettre � jour les donn�es du mod�le`�:

La capacit� est d�finie sur le d�bit maximal (en MW, d�bit maximal en m3/s mis � l&#39;�chelle par le d�bit de conception). La capacit� est sp�cifi�e comme limite de capacit� sur la River Technology (bdi) .

Le volume maximal de la contrainte de stockage est d�fini sur Volume maximal en MWyr conform�ment au tableau.

L&#39;utilisateur doit ensuite ajouter une s�rie temporelle dans le fichier csv sous les technologies CMRIDM_LAGDO et :button:`Update Timeslices` dans la feuille ``Timeslice``. Les valeurs dans le fichier csv doivent �tre le d�bit moyen mensuel divis� par le &quot;d�bit max&quot; qui a �t� utilis� pour d�finir la &quot;capacit� de la rivi�re&quot;, en utilisant la m�me valeur de d�bit max quel que soit le sc�nario.
Si l&#39;utilisateur souhaite simuler diff�rents sc�narios de pr�cipitations sans s�rie temporelle compl�te, il peut utiliser le facteur de plante pour augmenter ou r�duire le profil dans la feuille ``SpecificTech``. Il n&#39;est actuellement pas possible de sp�cifier un profil saisonnier diff�rent par sc�nario, mais cette fonctionnalit� est sur la liste des t�ches dans un avenir proche.


.. _batteries:

Batteries et stockage de la pompe
++++++++++++++++++++++++++++++++++++++

Les technologies de stockage de batteries et de pompes peuvent �tre ajout�es et modifi�es de la m�me mani�re via l&#39;interface excel SPLAT.

1. Dans la feuille ``Battery&amp;PumpStorage``�: cr�ez la technologie avec la convention techname�: xxELSTyyyy pour une batterie ou xxELSTPSyyyy pour le stockage de la pompe, o� xx est le code du pays et yyyy est la description du site. (Par exemple, ZAELSTPSDrakensberg)

2. :button:`Recharger Global`

3. Dans la m�me feuille ``Battery&amp;PumpStorage`` cliquez sur :button:`Refresh` puis sp�cifiez les heures de stockage et l&#39;efficacit� du cycle

4. Dans les fiches ``TechSpecific`` pr�cisez les autres param�tres usuels hc, bdi, inv etc...

.. _csp�:

�nergie Solaire Concentr�e (CSP)
++++++++++++++++++++++++++++++++

Reportez-vous aux �tapes de :ref:`solar_wind`. (Am�liorations � venir)

.. _transmission_distribution�:

Transport et Distribution
-----------------------------

Les feuilles :ref:`transmission` et :ref:`distribution` sont utilis�es pour revoir ou modifier les param�tres des technologies de transmission et de distribution selon les d�finitions de la feuille ``TechnologySets`` (voir section ci-dessous).

.. note::
1. Si l&#39;utilisateur souhaite mod�liser avec une demande &quot;envoy�e&quot; (voir :ref:`demande`), l&#39;efficacit� de transmission doit �tre d�finie sur 100�% et les co�ts d&#39;investissement sur une petite valeur. Dans la configuration par d�faut, aucune technologie de distribution n&#39;est sp�cifi�e pour l&#39;�lectricit� &quot;envoy�e&quot;.

2. Si un utilisateur sp�cifie des valeurs � la fois dans la colonne Constante et dans les colonnes de l&#39;ann�e du jalon, seule la valeur constante sera utilis�e pour mettre � jour le mod�le MESSAGE et les autres valeurs seront ignor�es.

.. _interconnexion�:

Interconnexion
-----------------

La fiche :ref:`interconnectors` permet de revoir et de mettre � jour les param�tres des interconnexions transfrontali�res.

Au minimum, les deux pays interconnect�s (qui doivent �tre actifs) doivent �tre sp�cifi�s pour visualiser les interconnexions entre eux.

.. _tech_naming�:

Nommage de la technologie dans le mod�le SPLAT
--------------------------------------------------

La d�nomination des technologies suit les conventions suivantes dans le mod�le SPLAT�:

??BMST_[nom] Biomasse Bagasse Cogen
??BWST_[nom] Biomasse Bois Cogen
??COSC_[nom] Charbon
??COCS_[nom] Charbon w CCS
??DSRC_[nom] Moteur diesel
??DSSC_[nom] Turbine Diesel
??NGCC_[nom] Cycle Combin� Gaz
??NGRC_[nom] Moteur � essence
??NGSC_[nom] Cycle d&#39;ouverture du gaz
??GOCV_[nom] G�othermie
??HFRC_[nom] Moteur HFO
??HFSC_[nom] HFO Turbine � vapeur
??HFSC_[nom] HFO Turbine � vapeur
??HYRO_[nom] Hydro au fil de l&#39;eau
??HYMI_[nom] Hydro Small
??HYDM_[nom] Hydro avec barrage
??NUPW_[nom] Nucl�aire
??EPPT_[nom] Stockage pomp�
??SOTN_[nom] Solar CSP pas de stockage
??SOTS_[nom] Solar CSP avec stockage
??SOPC_[nom] Syst�me solaire photovolta�que (service public)
??WDLC_[nom] Vent
