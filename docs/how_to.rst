.. role:: inputcell
:class: inputcell
.. role:: interfacecell
:class: interfacecell
.. role:: button
:class: button

Guides pratiques
=================

.. _change_decimal_seperator�:

Changer le s�parateur d�cimal dans l&#39;environnement Windows
----------------------------------------------------------------


.. image:: /images/how_to_ChangeDecimalSeparator1.png

.. image:: /images/how_to_ChangeDecimalSeparator2.png

.. image:: /images/how_to_ChangeDecimalSeparator3.png

.. image:: /images/how_to_ChangeDecimalSeparator4.png

.. image:: /images/how_to_ChangeDecimalSeparator5.png

.. image:: /images/how_to_ChangeDecimalSeparator6.png

.. image:: /images/how_to_ChangeDecimalSeparator7.png


.. _install_solver�:

Installation d&#39;un solveur gratuit alternatif (plus rapide)
------------------------------------------------------------------

Le logiciel MESSAGE est livr� par d�faut avec un solveur gratuit appel� GLPK. Ce solveur est ad�quat pour travailler avec de petits mod�les, cependant, lorsqu&#39;un mod�le plus grand doit �tre utilis� (par exemple, de nombreuses tranches de temps, de nombreuses technologies et sous-r�gions), ce solveur devient inad�quat et n�cessite beaucoup de temps pour terminer un &quot;RUN&quot;.

Il existe un solveur gratuit alternatif qui peut �tre utilis� avec MESSAGE appel� le CBC (`Coil-or Branch and Cut solver`_) qui est plus puissant et peut r�soudre des probl�mes plus importants � des vitesses comparables � certains des solveurs commerciaux tels que CPLEX.

Cependant, pour ex�cuter des ex�cutions avec ce solveur, il faut utiliser l&#39;interface SPLAT Excel pour lancer les ex�cutions (voir Tutoriel C - Utilisation de l&#39;interface SPLAT Excel) et il faut ajouter le solveur � l&#39;installation MESSAGE existante de l&#39;utilisateur. Ce guide donne une br�ve description sur la fa�on de faire cette installation.

1. T�l�chargez le fichier d&#39;archive cbc.rar � partir du `cbc link`_ et placez-le dans le dossier d&#39;installation de MESSAGE appel�:
``C:\Programmes\MESSAGE_INT\message_bin``

.. _cbc link: https://irena.sharepoint.com/:u:/r/sites/EPS/PTG%20Tools%20and%20Data/SPLAT%20kit/Software/AlternativeSolver/cbc_files.rar?csf=1&amp;web=1&amp;e=QPdmhj

.. _Coil-or Branch and Cut solver: https://github.com/coin-or/Cbc

.. image:: /images/how_to_1.png


2. Utilisez un logiciel tiers tel que Winrar pour extraire les fichiers de ``cbc.rar`` dans le dossier ``C:\Programs\MESSAGE_INT\message_bin`` (utilisez &quot;extraire ici&quot;)
Certains fichiers peuvent d�j� exister dans le dossier, vous pouvez accepter d&#39;�craser ces fichiers avec ceux de l&#39;archive ``cbc.rar``.


.. _using_message�:

Restauration et ouverture d&#39;un mod�le � l&#39;aide de l&#39;interface MESSAGE
-----------------------------------------------------------------------------------

1. Enregistrez le fichier ZIP du mod�le (SPLAT) qui commence par ``\MAINa_...`` dans un emplacement connu de l&#39;ordinateur

2. Apr�s l&#39;installation de MESSAGE, ouvrez le programme et deux fen�tres s&#39;ouvriront ; le bleu est l&#39;interface utilisateur pour le syst�me d&#39;exploitation Windows et le noir est la fen�tre de commande pour MESSAGE.

.. important::

Vous utiliserez les fen�tres bleues. Ne fermez PAS la fen�tre noire car cela fermera l&#39;interface MESSAGE�:

.. image:: /images/how_to_using_message_1.png

.. image:: /images/how_to_using_message_2.png

3. S�lectionnez :button:`Cases` &gt; :button:`Restaurer`

.. image:: /images/how_to_using_message_3.png

4. S�lectionnez le fichier ZIP ``MAINa_...`` situ� � l&#39;endroit o� vous avez pr�c�demment enregistr�

.. image:: /images/how_to_using_message_4.png

5. S�lectionnez :button:`Requ�tes` &gt; :button:`Ouvrir`

.. image:: /images/how_to_using_message_5.png

.. image:: /images/how_to_using_message_6.png

6. S�lectionnez ��Afrique�� et votre code de pays (veuillez consulter le tableau).

.. image:: /images/how_to_using_message_9.png

Par exemple, supposons que votre pays soit le Cameroun, alors vous choisissez le code CMa, alors la fen�tre suivante appara�tra avec Case Study : CMa.

.. image:: /images/how_to_using_message_7.png

.. image:: /images/how_to_using_message_8.png

7. Vous avez maintenant le mod�le de pays de votre choix, que vous pouvez modifier ou utiliser. Si vous cliquez sur :button:`Edit` puis cliquez sur :button:`application db`, vous obtenez l&#39;�cran suivant que vous pouvez utiliser pour afficher la plupart des donn�es d&#39;entr�e de votre mod�le.

.. image:: /images/how_to_using_message_10.png

.. _message_copy_scenario�:

Copier un sc�nario � l&#39;aide de l&#39;interface MESSAGE
-----------------------------------------------------------

1. Ouvrez votre mod�le dans MESSAGE. Si vous n&#39;avez pas restaur� votre mod�le auparavant, veuillez le restaurer pour la premi�re fois. (:ref:`using_message`)

2. S�lectionnez :button:`Cases` &gt; :button:`Scenario`&gt; :button:`Copy scenario`

3. Dans la fen�tre contextuelle, s�lectionnez le sc�nario de votre choix et entrez le nom de la nouvelle copie. Cliquez sur :button:`OK`.

.. image:: /images/how_to_copy_scenario.PNG

4. Si vous travaillez dans une r�gion avec plusieurs sous-r�gions, s�lectionnez :button:`Oui` pour :button:`Cr�er une copie pour toutes les sous-r�gions`�?

.. image:: /images/how_to_copy_scenario_2.PNG

5. Dans la feuille principale de l&#39;interface SPLAT, Recharger global. Vous trouverez le nouveau sc�nario que vous avez copi� dans le tableau Sc�narios. Pour utiliser le nouveau sc�nario, s�lectionnez ``1`` dans Sc�narios � recharger
