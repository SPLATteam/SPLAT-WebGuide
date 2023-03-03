.. role:: inputcell
:class: inputcell
.. role:: interfacecell
:class: interfacecell
.. role:: button
:class: button

Travailler avec la demande
===========================

.. important::
L&#39;interface doit �tre li�e au mod�le avant d&#39;ex�cuter l&#39;une des �tapes de cette section.
Voir :ref:`link_interface`.

Cette section d�crit comment afficher, modifier et ajouter une demande � l&#39;aide de l&#39;interface SPLAT.

.. view_demand�:

Affichage de la saisie de la demande
---------------------------------------

1. Dans l&#39;onglet ``Demande``, entrez le sc�nario � interroger dans la cellule ``Choisir le sc�nario``

2. Cliquez sur :button:`Actualiser la feuille`. La demande annuelle dans le sc�nario sera indiqu�e dans la m�me feuille. Seules les donn�es du ou des pays charg�s (dans la feuille ``Principal``) seront affich�es.

3. Dans l&#39;onglet ``PeakDemand``, r�p�tez les �tapes 1 et 2 pour r�cup�rer la demande de pointe pour le sc�nario s�lectionn�.

.. note::
La plupart des mod�les SPLAT n&#39;ont qu&#39;une demande envoy�e. Cependant, certains mod�les ont �galement une demande aux niveaux industriel, urbain et rural. L&#39;utilisateur verra les donn�es de demande class�es dans ces niveaux de demande multiples. Si le mod�le utilise uniquement la demande d&#39;�mission, l&#39;utilisateur peut simplement ignorer les donn�es sur les autres niveaux de demande. Ces niveaux de demande existent pour indiquer qu&#39;un utilisateur a toujours la possibilit� de mod�liser ces demandes s&#39;il le souhaite.

.. note::
La demande de pointe n&#39;est pas une entr�e directe dans le mod�le SPLAT. Cette feuille est aliment�e par des macro-codes qui multiplient le pic d&#39;une courbe de charge normalis�e par la demande annuelle d&#39;�lectricit� de la r�gion (wattheures).


.. change_demand�:

Modification de l&#39;entr�e de la demande
--------------------------------------------

1. Dans l&#39;onglet ``Demande``, cliquez sur :button:`Refresh Sheet` pour obtenir les donn�es enregistr�es dans le mod�le.

2. Apportez des modifications � la s�rie de demandes dans la feuille.

3. Cliquez sur :button:`Mettre � jour la feuille` pour mettre � jour le mod�le avec les nouvelles donn�es.

.. image:: /images/demand_update.PNG



