.. role:: inputcell
:class: inputcell
.. role:: interfacecell
:class: interfacecell
.. role:: button
:class: button

Travailler avec la demande
===========================

.. important::
L&#39;interface doit être liée au modèle avant d&#39;exécuter l&#39;une des étapes de cette section.
Voir :ref:`link_interface`.

Cette section décrit comment afficher, modifier et ajouter une demande à l&#39;aide de l&#39;interface SPLAT.

.. view_demand :

Affichage de la saisie de la demande
---------------------------------------

1. Dans l&#39;onglet ``Demande``, entrez le scénario à interroger dans la cellule ``Choisir le scénario``

2. Cliquez sur :button:`Actualiser la feuille`. La demande annuelle dans le scénario sera indiquée dans la même feuille. Seules les données du ou des pays chargés (dans la feuille ``Principal``) seront affichées.

3. Dans l&#39;onglet ``PeakDemand``, répétez les étapes 1 et 2 pour récupérer la demande de pointe pour le scénario sélectionné.

.. note::
La plupart des modèles SPLAT n&#39;ont qu&#39;une demande envoyée. Cependant, certains modèles ont également une demande aux niveaux industriel, urbain et rural. L&#39;utilisateur verra les données de demande classées dans ces niveaux de demande multiples. Si le modèle utilise uniquement la demande d&#39;émission, l&#39;utilisateur peut simplement ignorer les données sur les autres niveaux de demande. Ces niveaux de demande existent pour indiquer qu&#39;un utilisateur a toujours la possibilité de modéliser ces demandes s&#39;il le souhaite.

.. note::
La demande de pointe n&#39;est pas une entrée directe dans le modèle SPLAT. Cette feuille est alimentée par des macro-codes qui multiplient le pic d&#39;une courbe de charge normalisée par la demande annuelle d&#39;électricité de la région (wattheures).


.. change_demand :

Modification de l&#39;entrée de la demande
--------------------------------------------

1. Dans l&#39;onglet ``Demande``, cliquez sur :button:`Refresh Sheet` pour obtenir les données enregistrées dans le modèle.

2. Apportez des modifications à la série de demandes dans la feuille.

3. Cliquez sur :button:`Mettre à jour la feuille` pour mettre à jour le modèle avec les nouvelles données.

.. image:: /images/demand_update.PNG



