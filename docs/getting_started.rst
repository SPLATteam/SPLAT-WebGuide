.. role:: inputcell
:class: inputcell
.. role:: interfacecell
:class: interfacecell
.. role:: button
:class: button


Commencer
=====================
Cette section vise � guider le lecteur � travers un certain nombre d&#39;�tapes de base.

.. _conditions pr�alables:

Conditions pr�alables
------------------
Avant d&#39;utiliser l&#39;interface SPLAT, assurez-vous que les logiciels suivants sont install�s et que les fichiers sont t�l�charg�s�:

.. note::
Si vous avez d�j� re�u le kit d&#39;apprentissage SPLAT, les logiciels suivants (� l&#39;exception de Microsoft Excel) sont accessibles dans le dossier des logiciels. Si le kit ne vous a pas encore �t� d�livr�, veuillez remplir le `formulaire de demande`_ , ou contactez la personne IRENA avec laquelle vous �tes en contact.


- Microsoft Excel (version 64 bits, � v�rifier :ref:`checking_bits`)
- Outil AIEA MESSAGE
- Un mod�le
- Interface Excel SPLAT
- Solveur CBC (recommand�)

Le logiciel MESSAGE est livr� avec un solveur gratuit appel� GLPK. Si un autre solveur est n�cessaire, il devra �tre install� s�par�ment. Nous vous recommandons d&#39;utiliser le solveur CBC pour une utilisation avec l&#39;interface SPLAT. Reportez-vous � :ref:`install_solver` pour utiliser des solveurs alternatifs comme cbc.


.. _formulaire de demande:
https://forms.office.com/Pages/ResponsePage.aspx?id=sOvdzLvS0ESYSo5CpcBis8X-QNFmuJNIrZ3pyvqZdPxURVJMTUw0Mzg1SkFHOTFFV0lXTFhLN1NEVS4u


.. _conventions:

Conventions
----------------------
:inputcell:`Cellule d&#39;entr�e utilisateur`

Les cellules format�es comme ci-dessus (police sombre avec fond orange) sont des cellules de saisie utilisateur, o� l&#39;utilisateur est autoris� et cens� saisir des donn�es.

:interfacecell:`R�serv� pour l&#39;interface`

Les cellules format�es comme ci-dessus (police fonc�e avec fond gris p�le) sont des cellules r�serv�es � l&#39;interface. Ces cellules sont remplies par des macros dans le classeur ou sont des cellules calcul�es.

Les onglets sont organis�s selon les conventions suivantes�:

- Feuille ``Index``�: liste toutes les feuilles du classeur
- Feuille ``Main``�: o� les utilisateurs d�finissent le chemin du mod�le et s�lectionnent les pays dans le mod�le
- Onglets jaunes : pour revoir et mettre � jour les entr�es de base du mod�le
- Onglets rouges : pour ex�cuter un mod�le et extraire les r�sultats
- Onglets gris : utilitaires disponibles pour les utilisateurs plus avanc�s

.. _first_steps�:

Premiers pas
------------------
Cette documentation utilise un mod�le simple pour la d�monstration. Vous pouvez utiliser un mod�le MESSAGE existant pour la plupart des exemples de cette documentation.

.. _checking_bits�:

V�rification de la version Excel
+++++++++++++++++++++++++++++++++

L&#39;interface SPLAT Excel n�cessite la version 64 bits par d�faut d&#39;Excel pour ses fonctions principales. Vous pouvez v�rifier votre version d&#39;Excel en cliquant sur le menu :button:`Fichier` &gt; :button:`Compte` &gt; :button:`� propos d&#39;Excel`. Si vous avez l&#39;ancien Excel 32 bits, il est recommand� de d�sinstaller et de r�installer votre logiciel Microsoft Office avec 64 bits s�lectionn�, ou d&#39;utiliser un ordinateur avec un logiciel 64 bits d�j� install�.

.. image:: /images/getting_started_opening_file_2.PNG

.. _restoring_model�:

Restaurer le mod�le dans MESSAGE
++++++++++++++++++++++++++++++++++

Afin d&#39;ex�cuter le mod�le � l&#39;aide de l&#39;interface Excel SPLAT, vous devrez peut-�tre restaurer le mod�le dans MESSAGE une fois. Reportez-vous au guide pratique sur :ref:`using_message` pour obtenir des instructions sur l&#39;utilisation de MESSAGE.

.. _opening_file�:

Ouverture du fichier
++++++++++++++++++++++++
Ouvrez le fichier Excel qui commence par *SPLAT_Interface_...*.

Lorsque vous ouvrez le fichier, vous devez cliquer sur :button:`Activer le contenu` (comme indiqu� ci-dessous) pour que le fichier fonctionne.

.. image:: /images/getting_started_opening_file.PNG

De plus, les macros doivent �tre activ�es. Reportez-vous au lien pour `activer les macros`_.

.. _activer les macros�:
https://support.microsoft.com/en-gb/office/enable-or-disable-macros-in-microsoft-365-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6

.. _checking_decimal�:

V�rification du symbole d�cimal du syst�me
++++++++++++++++++++++++++++++++++++++++++++++
Le s�parateur d�cimal de votre syst�me doit �tre d�fini sur &#39;.&#39; (point) pour que l&#39;interface SPLAT Excel fonctionne correctement. S&#39;il en est autrement, par exemple &#39;,&#39; (virgule), allez dans ``Panneau de configuration`` &gt; ``R�gion`` &gt; ``Param�tres suppl�mentaires``, et remplacez le symbole d�cimal par &#39;.&#39;.

.. note::
Le s�parateur virgule est souvent le s�parateur par d�faut dans les environnements Windows fran�ais et devrait �tre modifi� afin de pouvoir utiliser l&#39;interface. Reportez-vous � :ref:`change_decimal_seperator`.

.. _link_interface�:

Lier l&#39;interface � votre fichier mod�le
++++++++++++++++++++++++++++++++++++++++++++++++++ +++++++

1. Dans l&#39;onglet ``Main`` du fichier, assurez-vous que les champs :inputcell:`Model Folder` et :inputcell:`Main Region` sont correctement d�finis, comme indiqu� ci-dessous, pour refl�ter l&#39;emplacement du dossier mod�le MESSAGE restaur� sur votre ordinateur.

2. dans la section ``Sous-r�gions`` de l&#39;onglet ``Principal``, choisissez le(s) pays que vous souhaitez activer, en pla�ant un &quot;1&quot; � c�t� dans la colonne orange, et un &quot;0&quot; � c�t� de tout autre pays.

3. Cliquez sur le bouton :button:`Reload Global` en haut de la page (ceci connecte les fichiers de mod�le MESSAGE avec ce classeur Excel). Les fichiers mod�les sont lus et charg�s en m�moire dans Excel.

4. Vous verrez une fen�tre pop-up indiquant &quot;Donn�es de 2 pays charg�es en m�moire&quot; (comme indiqu� ci-dessous)�; appuyez sur :button:`OK`.

.. image:: /images/getting_started_linking_interface_1.PNG

.. image:: /images/getting_started_linking_interface_2.PNG

.. _view_input�:

Affichage de l&#39;entr�e du mod�le
++++++++++++++++++++++++++++++++

L&#39;interface SPLAT Excel permet � un utilisateur de voir les donn�es d&#39;entr�e stock�es dans les mod�les SPLAT-MESSAGE.

1. Dans l&#39;un des onglets jaunes, choisissez le sc�nario dans la liste d�roulante de la cellule C3.

2. Cliquez sur :button:`Refresh Sheet`, les donn�es stock�es dans le mod�le s&#39;afficheront dans le tableau.

Ce processus fonctionne de la m�me mani�re pour tous les onglets jaunes (``Demande``, ``Transmission``, ``Distribution``, etc.) de l&#39;interface SPLAT Excel. Vous pouvez �galement actualiser toutes les feuilles dans ces onglets en cliquant sur :button:`Actualiser toutes les feuilles` dans l&#39;onglet ``Principal``.

.. image:: /images/getting_started_viewing_input.PNG


.. caution::
Si vous avez vid� les cellules sous l&#39;en-t�te du tableau, appuyer sur &#39;Actualiser la feuille&#39; provoquera une erreur. Cela se produit car le code de macro sous-jacent ne parvient pas � identifier la cellule de d�part pour commencer � coller les donn�es de mod�le requises. Si vous rencontrez cette erreur, cliquez sur &#39;fin&#39;&gt; Recharger global&gt; �crivez un simple alphabet simple dans la cellule juste sous la premi�re cellule de l&#39;en-t�te du tableau&gt; actualisez la feuille.


.. note::
Gardez � l&#39;esprit que le sc�nario &quot;adb&quot; (Application Database) contient toutes les donn�es de base du mod�le. Le choix d&#39;un autre sc�nario n&#39;affichera que les donn�es **diff�rentes** dans ce sc�nario. Donc, si vous choisissez un sc�nario et que les donn�es sont vides, cela signifie qu&#39;il a les m�mes donn�es que &quot;adb&quot;.


.. _run_model�:

Ex�cution du mod�le
++++++++++++++++++++++++++

**Apr�s** avoir li� votre mod�le au fichier d&#39;interface dans l&#39;onglet ``Main``, vous pouvez ex�cuter votre mod�le SPLAT � l&#39;aide de l&#39;onglet ``ReportGen-Annual``.

1. S�lectionnez la bonne combinaison de sc�nario et de pays que vous souhaitez ex�cuter.
Pour ex�cuter le mod�le pour l&#39;ensemble du continent, s�lectionnez tous les pays et &quot;MAINa&quot; dans les sous-r�gions/pays.

2. S�lectionnez l&#39;option pr�f�r�e (avec ou sans interconnexions entre les sous-r�gions) sous ``Options d&#39;ex�cution (sous-r�gions)``.
Pour un mod�le � un seul comt�, s�lectionnez :inputcell:`Separate Subregions`.
Pour un mod�le multi-pays, :inputcell:`Sous-r�gions s�par�es` ou :inputcell:`Interconnect�es` peuvent �tre s�lectionn�es en fonction du r�cit du sc�nario pour l&#39;interconnexion entre les pays.
Dans cet exemple, nous s�lectionnons l&#39;option :inputcell:`Interconnect�``.

3. S�lectionnez l&#39;option correcte sous les cat�gories &quot;Ex�cuter&quot;. Les cat�gories correspondent aux m�mes options dans le menu &quot;Ex�cuter&quot; MESSAGE�:
:inputcell:`Mxg` = g�n�rateur de matrice�;
:inputcell:`Opt` = Optimisation�;
:inputcell:`Cap` = Cr�ation du fichier Cap�;
:inputcell:`All` = effectuer tout ce qui pr�c�de.
Il existe trois options diff�rentes fournies dans l&#39;interface pour CPLEX, CBC et GUROBI selon le solveur que vous avez pr�install�. Si vous �tes un nouvel utilisateur, veuillez installer et utiliser CBC (:ref:`install_solver`).

4. Appuyez sur le bouton :button:`Ex�cuter`. Vous devriez voir la fen�tre MESSAGE noire appara�tre et commencer � s&#39;ex�cuter.

.. image:: /images/getting_started_running_model.PNG

.. _extract_results�:

Extraction des r�sultats
++++++++++++++++++++++++++++++++

Utiliser l&#39;onglet ReportGen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
L&#39;onglet ``ReportGen-Annual`` est �galement l&#39;endroit o� vous pouvez extraire les r�sultats du mod�le que vous venez d&#39;ex�cuter.

1. S�lectionnez la combinaison sc�nario(s), pays(s), variable(s) et ann�e(s) dont vous souhaitez afficher les r�sultats. Veuillez vous assurer que le sc�nario souhait� a �t� charg� dans la m�moire Excel. S&#39;il n&#39;appara�t pas dans la liste d�roulante, veuillez revenir � l&#39;onglet ��Principal�� et marquer le sc�nario souhait� ��1�� et appuyer sur le bouton ��Recharger global��.

2. S�lectionnez le format de sortie et entrez le chemin de sortie (le cas �ch�ant) dans la section ``Destination des r�sultats``.

3. Cliquez sur :button:`Get Results` (cercle rouge dans l&#39;image ci-dessous). Si :inputcell:`sur cette feuille` est s�lectionn�, vous devriez voir les r�sultats bruts appara�tre sur la feuille lorsque le processus est termin�. Si :inputcell:`csv` est s�lectionn�, les r�sultats seront �crits dans un fichier csv � l&#39;emplacement sp�cifi�. Si l&#39;emplacement n&#39;existe pas, il y aura un message d&#39;erreur. L&#39;option csv est plus pratique lorsque vous travaillez avec un grand nombre de r�sultats, et ils peuvent �tre li�s � d&#39;autres tableaux crois�s dynamiques dans Excel ou d&#39;autres logiciels tels que PowerBi ou Tableau.

.. image:: /images/getting_started_extract_results_1.PNG

Mettre � jour les tableaux de r�sultats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Vous pouvez trouver les tableaux de r�sultats annuels dans les feuilles rouges�: ``Capacity``, ``Output``, ``New Capacity``, ``CO2`` et ``Costs``.

.. important::

Assurez-vous de v�rifier que le sc�nario et le pays corrects sont choisis en haut du tableau.

Cliquez avec le bouton droit n&#39;importe o� dans le tableau de la feuille de calcul et s�lectionnez :button:`Actualiser` dans les options. Ces graphiques doivent �tre mis � jour ** chaque fois ** que vous obtenez de nouveaux r�sultats.

.. image:: /images/getting_started_extract_results_2.PNG
