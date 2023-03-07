.. role:: inputcell
:class: inputcell
.. role:: interfacecell
:class: interfacecell
.. role:: button
:class: button

D�finir le temps
==================

.. important::
L&#39;interface doit �tre li�e au mod�le avant d&#39;ex�cuter l&#39;une des �tapes de cette section.
Voir :ref:`link_interface`.

La feuille ``Timeslices (Load Regions)`` permet � l&#39;utilisateur de voir quelles r�gions de chargement se trouvent dans le mod�le. Il permet �galement � l&#39;utilisateur de s�lectionner le fuseau horaire avec lequel ex�cuter le mod�le. Pour apporter des modifications � la d�finition de la r�gion de chargement, les donn�es de demande et de profil doivent �tre fournies dans un dossier sp�cifi� conform�ment aux sp�cifications d�crites plus loin dans ce document.

Notez qu&#39;actuellement, l&#39;interface ne prend pas en charge plusieurs types de jours (par exemple, les jours de semaine ou les week-ends), bien que cela sera ajout� dans les futures versions de l&#39;interface.

L&#39;utilisateur peut revoir la d�finition des r�gions de chargement en cliquant sur le bouton :button:`Afficher TS en m�moire`.

.. _time_zones�:

D�finition des fuseaux horaires et de la granularit�
-------------------------------------------------

1. Ajoutez les informations de fuseau horaire local � regid_AllRegions.tit (par rapport � UTC).

2. Dans la feuille ``Timeslices (Load Regions)``, s�lectionnez l&#39;une des configurations pr�d�finies et le fuseau horaire du mod�le

.. note::

Il existe 4�configurations de r�gion de chargement pr�d�finies dans l&#39;interface�:

- Grand mod�le�: 30 tranches horaires/r�gions de chargement (3�saisons de 10�blocs chacune)

- Petit mod�le : 10 time-slices/load regions (3 saisons, 2 � 3 blocs, 1 � 4 blocs)

- Petit mod�le V2 : 10 time-slices/load regions (1 saison avec 10 blocs)

- Tr�s petit mod�le�: 3�tranches/r�gions de charge (1�saison avec 3�blocs)

3. Mettez � jour les d�finitions de tranches de temps dans le mod�le en cliquant sur le bouton :button:`Mettre � jour les fichiers`. Cette volont�:

- Mettre � jour les d�finitions de tranches de temps dans les fichiers adb, ldb et ldr

- D�calez les s�ries chronologiques du facteur de capacit� et les s�ries chronologiques de la demande des fuseaux horaires locaux des r�gions vers le fuseau horaire du mod�le s�lectionn�.

- Mettre � jour les profils RE et les profils de demande qui sont stock�s dans des s�ries de donn�es 8760 dans des fichiers csv s�par�s. Les fichiers csv pour les profils de demande et d&#39;ER sont stock�s dans le dossier de donn�es de chaque pays/sous-r�gion.

.. note::
Requis : Macros-&gt; outils -&gt; R�f�rences (Microsoft Active X …..)
