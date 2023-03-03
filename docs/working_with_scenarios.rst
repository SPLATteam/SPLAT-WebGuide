.. role:: button
:class: button

Travailler avec des sc�narios
===============================

.. note::
L&#39;interface Excel SPLAT est limit�e dans la gestion directe des sc�narios. Veuillez ajouter et supprimer des sc�narios directement via MESSAGE.

.. _add_scenario�:

Ajouter un sc�nario
---------------------
Les sc�narios doivent �tre ajout�s via l&#39;interface MESSAGE. Il est recommand� � l&#39;utilisateur de faire une copie d&#39;un sc�nario existant via l&#39;interface MESSAGE et de le charger dans l&#39;interface SPLAT. Reportez-vous � :ref:`message_copy_scenario`.

.. _select_scenario�:

S�lectionnez un sc�nario
--------------------------
Pour s�lectionner un sc�nario sp�cifique dans SPLAT, le sc�nario respectif doit �tre activ� (mettez &quot;1&quot; dans la colonne Sc�nario � recharger pour le sc�nario respectif dans le tableau Sc�nario) dans la feuille principale.
Ensuite, le rechargement global doit �tre activ� pour charger les donn�es du mod�le pour le mod�le sp�cifi� pour une sous-r�gion et un sc�nario donn�s sp�cifi�s dans le tableau.

Les donn�es doivent �tre d�finies dans les fiches d&#39;entr�e et les fiches de contraintes pour correspondre aux r�cits et aux hypoth�ses du sc�nario sp�cifique.

.. note::
Lorsqu&#39;une feuille d&#39;entr�es ou de contraintes est rafra�chie pour un sc�nario (sauf adb) et qu&#39;un champ de donn�es est vide, cela implique que le sc�nario prend la m�me valeur que celle d�finie dans le sc�nario adb.
Pour d�finir une nouvelle valeur pour le champ de donn�es, les donn�es doivent �tre saisies et :button:`Mettre � jour les donn�es du mod�le` doit �tre enfonc� pour mettre � jour les donn�es du mod�le pour le sc�nario donn�.

.. .. _define_fullintegration_scenario�:

.. D�finition du sc�nario FullIntegration
.. -----------------------------------------
.. Un sc�nario d&#39;int�gration compl�te consid�re l&#39;int�gration au niveau national et r�gional dans le mod�le. Contrairement � d&#39;autres sc�narios, les interconnexions g�n�riques sont mises en ligne dans ce sc�nario.
.. Par cons�quent, les co�ts de nuit des interconnexions g�n�riques ($/kW) doivent �tre &quot;bien d�finis&quot; dans la feuille ``Interconnectors`` dans le cas du sc�nario FullIntegration.


