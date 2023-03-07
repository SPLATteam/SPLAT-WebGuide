.. role:: inputcell
:class: inputcell
.. role:: interfacecell
:class: interfacecell
.. role:: button
:class: button

Définir le temps
==================

.. important::
L&#39;interface doit être liée au modèle avant d&#39;exécuter l&#39;une des étapes de cette section.
Voir :ref:`link_interface`.

La feuille ``Timeslices (Load Regions)`` permet à l&#39;utilisateur de voir quelles régions de chargement se trouvent dans le modèle. Il permet également à l&#39;utilisateur de sélectionner le fuseau horaire avec lequel exécuter le modèle. Pour apporter des modifications à la définition de la région de chargement, les données de demande et de profil doivent être fournies dans un dossier spécifié conformément aux spécifications décrites plus loin dans ce document.

Notez qu&#39;actuellement, l&#39;interface ne prend pas en charge plusieurs types de jours (par exemple, les jours de semaine ou les week-ends), bien que cela sera ajouté dans les futures versions de l&#39;interface.

L&#39;utilisateur peut revoir la définition des régions de chargement en cliquant sur le bouton :button:`Afficher TS en mémoire`.

.. _time_zones :

Définition des fuseaux horaires et de la granularité
-------------------------------------------------

1. Ajoutez les informations de fuseau horaire local à regid_AllRegions.tit (par rapport à UTC).

2. Dans la feuille ``Timeslices (Load Regions)``, sélectionnez l&#39;une des configurations prédéfinies et le fuseau horaire du modèle

.. note::

Il existe 4 configurations de région de chargement prédéfinies dans l&#39;interface :

- Grand modèle : 30 tranches horaires/régions de chargement (3 saisons de 10 blocs chacune)

- Petit modèle : 10 time-slices/load regions (3 saisons, 2 à 3 blocs, 1 à 4 blocs)

- Petit modèle V2 : 10 time-slices/load regions (1 saison avec 10 blocs)

- Très petit modèle : 3 tranches/régions de charge (1 saison avec 3 blocs)

3. Mettez à jour les définitions de tranches de temps dans le modèle en cliquant sur le bouton :button:`Mettre à jour les fichiers`. Cette volonté:

- Mettre à jour les définitions de tranches de temps dans les fichiers adb, ldb et ldr

- Décalez les séries chronologiques du facteur de capacité et les séries chronologiques de la demande des fuseaux horaires locaux des régions vers le fuseau horaire du modèle sélectionné.

- Mettre à jour les profils RE et les profils de demande qui sont stockés dans des séries de données 8760 dans des fichiers csv séparés. Les fichiers csv pour les profils de demande et d&#39;ER sont stockés dans le dossier de données de chaque pays/sous-région.

.. note::
Requis : Macros-&gt; outils -&gt; Références (Microsoft Active X â€¦..)
