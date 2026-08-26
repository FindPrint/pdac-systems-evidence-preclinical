# Cadre de redémarrage — recherche préclinique sur systèmes PDAC

> **Avertissement médical.** Ce projet ne peut pas garantir une guérison, empêcher le décès d’un patient ou assurer l’absence de souffrance et de toxicité. Il s’agit d’une infrastructure de recherche préclinique destinée à générer et à falsifier des hypothèses. Tout passage au soin humain exige des validations expérimentales, cliniques, éthiques et réglementaires indépendantes.

## Intention scientifique

L’ambition du nouveau projet est de chercher des hypothèses permettant simultanément d’étudier : l’activité anti-tumorale, la résistance/adaptation, les tissus sains, la toxicité cumulative et la durabilité d’un effet. Il ne doit jamais confondre cette ambition avec une promesse thérapeutique.

La question de recherche générale est :

> Quelles hypothèses mécanistiques précliniques présentent un signal reproductible d’activité anti-tumorale, sans dégradation disproportionnée des indicateurs de tissus sains dans des systèmes expérimentaux indépendants ?

## Conditions de réussite par niveau de preuve

| Niveau | Preuve exigée | Formulation autorisée | Formulation interdite |
| --- | --- | --- | --- |
| Données et associations | Cohortes/mesures bien définies, validation externe et incertitude. | « association observée » ou « signal reproductible ». | « cause », « fenêtre thérapeutique patient » ou « traitement ». |
| Séries longitudinales | Mesures répétées réelles sur la même entité, ordre temporel vérifié et robustesse. | « candidat de changement de régime ». | « point de non-retour clinique ». |
| Simulation | Paramètres sourcés ou calibrés, incertitude et scénarios alternatifs. | « scénario mécanistique compatible avec les hypothèses ». | « efficacité attendue », dose ou calendrier de soin. |
| Lignée/organoïde | Réplication, contrôles, doses mesurées, cytotoxicité et lecture des cellules non tumorales. | « signal préclinique dans ce modèle ». | « traitement sûr chez l’humain ». |
| Animal puis essai clinique | Protocoles éthiques, pharmacocinétique, toxicologie et endpoints approuvés. | Niveau d’évidence défini par le protocole. | Toute généralisation au-delà des données. |

## Axes obligatoires du projet

1. **Efficacité anti-tumorale.** Toute hypothèse doit définir une mesure biologique et un contrôle approprié ; une diminution simulée n’est jamais suffisante.
2. **Protection des tissus sains.** La sécurité doit être mesurée dans des systèmes indépendants et non calculée à partir d’un coefficient favorable au modèle.
3. **Résistance et long terme.** Les mécanismes d’échappement, de repousse et de plasticité doivent être recherchés comme résultats possibles, pas supprimés du récit.
4. **Réplicabilité.** Une hypothèse doit survivre à des lots, plateformes, lignées, organoïdes ou cohortes indépendants selon sa couche de preuve.
5. **Falsifiabilité.** Toute hypothèse doit inclure au moins un résultat qui conduirait explicitement à son rejet.
6. **Traçabilité.** Données, transformations, paramètres, code, graines, résultats négatifs et sources doivent être immuables et vérifiables.

## Règles de départ

- Le pipeline v3 et le module CSD F1′/F2″ doivent être conservés comme références historiques séparées ; ils ne sont pas présumés valides en oncologie.
- Aucun code existant n’est importé dans le nouveau projet sans audit de rôle, de provenance et de limites.
- Les données transversales, longitudinales, de simulation et d’expérience sont stockées dans des couches séparées.
- Aucune variable de résultat clinique futur ne peut servir d’axe temporel ou de prédicteur.
- Aucun classement de cible ne peut se transformer automatiquement en combinaison, dose, calendrier ou recommandation.
- Un nouvel élément n’est publié dans le dépôt privé qu’avec son manifeste, sa provenance et une déclaration de portée.

## Premier objectif réaliste

Le premier objectif n’est pas de trouver un traitement. Il est de construire un **registre de preuves et d’hypothèses** qui peut montrer, de manière auditée, qu’un signal est :

- soutenu par plusieurs sources indépendantes ;
- contredit par une source ou un test ;
- insuffisamment informé ;
- ou prêt à être évalué dans une expérience préclinique définie par des spécialistes.

Cette première étape est ce qui rend possible un programme durable, au lieu d’un résultat séduisant mais non vérifiable.
