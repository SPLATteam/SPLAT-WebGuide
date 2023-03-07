.. role:: button
    :class: button

Travailler avec des scénarios
=======================

.. note::
    L'interface Excel SPLAT est limitée dans la gestion directe des scénarios. Veuillez ajouter et supprimer des scénarios directement via MESSAGE.

.. _add_scenario :

Ajouter un scénario
--------------
Les scénarios doivent être ajoutés via l'interface MESSAGE. Il est recommandé à l'utilisateur de faire une copie d'un scénario existant via l'interface MESSAGE et de le charger dans l'interface SPLAT. Reportez-vous à :ref:`message_copy_scenario`.

.. _select_scenario :

Sélectionnez un scénario
-----------------
Pour sélectionner un scénario spécifique dans SPLAT, le scénario respectif doit être activé (mettez "1" dans la colonne Scénario à recharger pour le scénario respectif dans le tableau Scénario) dans la feuille principale.
Ensuite, le rechargement global doit être activé pour charger les données du modèle pour le modèle spécifié pour une sous-région et un scénario donnés spécifiés dans le tableau.

Les données doivent être définies dans les fiches d'entrée et les fiches de contraintes pour correspondre aux récits et aux hypothèses du scénario spécifique.

.. note::
    Lorsqu'une feuille d'entrées ou de contraintes est rafraîchie pour un scénario (sauf adb) et qu'un champ de données est vide, cela implique que le scénario prend la même valeur que celle définie dans le scénario adb.
    Pour définir une nouvelle valeur pour le champ de données, les données doivent être saisies et :button:`Mettre à jour les données du modèle` doit être enfoncé pour mettre à jour les données du modèle pour le scénario donné.

.. .. _define_fullintegration_scenario :

.. Définition du scénario FullIntegration
.. ---------------------------------
.. Un scénario d'intégration complète considère l'intégration au niveau national et régional dans le modèle. Contrairement à d'autres scénarios, les interconnexions génériques sont mises en ligne dans ce scénario.
.. Par conséquent, les coûts de nuit des interconnexions génériques ($/kW) doivent être "bien définis" dans la feuille ``Interconnectors`` dans le cas du scénario FullIntegration.


