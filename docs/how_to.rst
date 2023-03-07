.. role:: inputcell
    :class: inputcell
.. role:: interfacecell
    :class: interfacecell
.. role:: button
    :class: button

Guides pratiques
=============

.. _change_decimal_seperator :

Changer le séparateur décimal dans l'environnement Windows
----------------------------------------------


.. image:: /images/how_to_ChangeDecimalSeparator1.png

.. image:: /images/how_to_ChangeDecimalSeparator2.png

.. image:: /images/how_to_ChangeDecimalSeparator3.png

.. image:: /images/how_to_ChangeDecimalSeparator4.png

.. image:: /images/how_to_ChangeDecimalSeparator5.png

.. image:: /images/how_to_ChangeDecimalSeparator6.png

.. image:: /images/how_to_ChangeDecimalSeparator7.png


.. _install_solver :

Installation d'un solveur gratuit alternatif (plus rapide)
----------------------------------------------

Le logiciel MESSAGE est livré par défaut avec un solveur gratuit appelé GLPK. Ce solveur est adéquat pour travailler avec de petits modèles, cependant, lorsqu'un modèle plus grand doit être utilisé (par exemple, de nombreuses tranches de temps, de nombreuses technologies et sous-régions), ce solveur devient inadéquat et nécessite beaucoup de temps pour terminer un "RUN".

Il existe un solveur gratuit alternatif qui peut être utilisé avec MESSAGE appelé le CBC (`Coil-or Branch and Cut solver`_) qui est plus puissant et peut résoudre des problèmes plus importants à des vitesses comparables à certains des solveurs commerciaux tels que CPLEX.

Cependant, pour exécuter des exécutions avec ce solveur, il faut utiliser l'interface SPLAT Excel pour lancer les exécutions (voir Tutoriel C - Utilisation de l'interface SPLAT Excel) et il faut ajouter le solveur à l'installation MESSAGE existante de l'utilisateur. Ce guide donne une brève description sur la façon de faire cette installation.

1. Téléchargez le fichier d'archive cbc.rar à partir du `cbc link`_ et placez-le dans le dossier d'installation de MESSAGE appelé :
``C:\Programmes\MESSAGE_INT\message_bin``

.. _cbc link: https://irena.sharepoint.com/:u:/r/sites/EPS/PTG%20Tools%20and%20Data/SPLAT%20kit/Software/AlternativeSolver/cbc_files.rar?csf=1&web=1&e=QPdmhj

.. _Coil-or Branch and Cut solver: https://github.com/coin-or/Cbc

.. image:: /images/how_to_1.png


2. Utilisez un logiciel tiers tel que Winrar pour extraire les fichiers de ``cbc.rar`` dans le dossier ``C:\Programs\MESSAGE_INT\message_bin`` (utilisez "extraire ici")
Certains fichiers peuvent déjà exister dans le dossier, vous pouvez accepter d'écraser ces fichiers avec ceux de l'archive ``cbc.rar``.


.. _using_message :

Restauration et ouverture d'un modèle à l'aide de l'interface MESSAGE
-------------------------------------------------- --------

1. Enregistrez le fichier ZIP du modèle (SPLAT) qui commence par ``\MAINa_...`` dans un emplacement connu de l'ordinateur

2. Après l'installation de MESSAGE, ouvrez le programme et deux fenêtres s'ouvriront ; le bleu est l'interface utilisateur pour le système d'exploitation Windows et le noir est la fenêtre de commande pour MESSAGE.

.. important::

    Vous utiliserez les fenêtres bleues. Ne fermez PAS la fenêtre noire car cela fermera l'interface MESSAGE :

.. image:: /images/how_to_using_message_1.png

.. image:: /images/how_to_using_message_2.png

3. Sélectionnez :button:`Cases` > :button:`Restaurer`

.. image:: /images/how_to_using_message_3.png

4. Sélectionnez le fichier ZIP ``MAINa_...`` situé à l'endroit où vous avez précédemment enregistré

.. image:: /images/how_to_using_message_4.png

5. Sélectionnez :button:`Requêtes` > :button:`Ouvrir`

.. image:: /images/how_to_using_message_5.png

.. image:: /images/how_to_using_message_6.png

6. Sélectionnez « Afrique » et votre code de pays (veuillez consulter le tableau).

.. image:: /images/how_to_using_message_9.png

Par exemple, supposons que votre pays soit le Cameroun, alors vous choisissez le code CMa, alors la fenêtre suivante apparaîtra avec Case Study : CMa.

.. image:: /images/how_to_using_message_7.png

.. image:: /images/how_to_using_message_8.png

7. Vous avez maintenant le modèle de pays de votre choix, que vous pouvez modifier ou utiliser. Si vous cliquez sur :button:`Edit` puis cliquez sur :button:`application db`, vous obtenez l'écran suivant que vous pouvez utiliser pour afficher la plupart des données d'entrée de votre modèle.

.. image:: /images/how_to_using_message_10.png

.. _message_copy_scenario :

Copier un scénario à l'aide de l'interface MESSAGE
-----------------------------------------------

1. Ouvrez votre modèle dans MESSAGE. Si vous n'avez pas restauré votre modèle auparavant, veuillez le restaurer pour la première fois. (:ref:`using_message`)

2. Sélectionnez :button:`Cases` > :button:`Scenario`> :button:`Copy scenario`

3. Dans la fenêtre contextuelle, sélectionnez le scénario de votre choix et entrez le nom de la nouvelle copie. Cliquez sur :button:`OK`.

.. image:: /images/how_to_copy_scenario.PNG

4. Si vous travaillez dans une région avec plusieurs sous-régions, sélectionnez :button:`Oui` pour :button:`Créer une copie pour toutes les sous-régions` ?

.. image:: /images/how_to_copy_scenario_2.PNG

5. Dans la feuille principale de l'interface SPLAT, Recharger global. Vous trouverez le nouveau scénario que vous avez copié dans le tableau Scénarios. Pour utiliser le nouveau scénario, sélectionnez ``1`` dans Scénarios à recharger