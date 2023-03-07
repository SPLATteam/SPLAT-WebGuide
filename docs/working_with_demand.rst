.. role:: inputcell
:class: inputcell
.. role:: interfacecell
:class: interfacecell
.. role:: button
:class: button

Travailler avec la demande
============================

.. important::
L&#39;interface doit �tre li�e au mod�le avant d&#39;ex�cuter l&#39;une des �tapes de cette section.
Voir :ref:`link_interface`.

Cette section d�crit comment afficher, modifier et ajouter une demande � l&#39;aide de l&#39;interface SPLAT.

.. view_demand�:

Affichage de la saisie de la demande
-----------------------------

1. Dans l&#39;onglet ``Demande``, entrez le sc�nario � interroger dans la cellule ``Choisir le sc�nario``

2. Cliquez sur :button:`Actualiser la feuille`. La demande annuelle dans le sc�nario (fichier adb ou ldb) sera indiqu�e dans la m�me feuille. Seules les donn�es du ou des pays charg�s (dans la feuille ``Principal``) seront affich�es.

3. Dans l&#39;onglet ``PeakDemand``, r�p�tez les �tapes 1 et 2 pour r�cup�rer la demande de pointe pour le sc�nario s�lectionn�.

.. note::
Des dispositions ont �t� prises pour travailler soit avec une demande &quot;envoy�e&quot;, soit avec une demande sectorielle telle que industrielle, urbaine et rurale. L&#39;utilisateur verra les donn�es de demande class�es dans ces niveaux de demande multiples. Si le mod�le utilise uniquement la demande d&#39;�mission, l&#39;utilisateur doit d�finir les donn�es sur les autres niveaux de demande � z�ro, et vice versa, sinon la demande sera compt�e deux fois. Notez �galement que les donn�es brutes sont stock�es dans les fichiers adb et ldb de MWyr. Les valeurs MWyr sont converties par SPLAT en GWh par d�faut.

.. note::
La demande de pointe n&#39;est pas une entr�e directe dans le mod�le SPLAT. La demande de pointe est estim�e sur la base des valeurs �nerg�tiques annuelles et du param�trage du profil correspondant stock� dans le fichier Application Database (adb).

.. change_demand�:

Modification de l&#39;entr�e de la demande
------------------------------

1. Dans l&#39;onglet ``Demande``, cliquez sur :button:`Refresh Sheet` pour obtenir les donn�es enregistr�es dans le mod�le.

2. Apportez des modifications � la s�rie de demandes dans la feuille.

3. Cliquez sur :button:`Mettre � jour la feuille` pour mettre � jour le mod�le avec les nouvelles donn�es.

.. image:: /images/demand_update.PNG



