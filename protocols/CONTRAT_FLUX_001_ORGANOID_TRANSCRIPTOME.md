# CONTRAT_FLUX_001 — Caractérisation transcriptomique d’organoïdes PDAC

## Jeu de données retenu à titre de démarrage

La source candidate retenue est le sous-ensemble **ouvert de quantifications d’expression RNA-seq** du projet GDC `ORGANOID-PANCREATIC` (« Pancreas Cancer Organoid Profiling »). Le GDC affiche 49 cas avec RNA-seq, tandis que la notice AWS distingue explicitement les quantifications RNA-seq ouvertes des lectures alignées et autres modalités contrôlées. [1] [2]

La sélection concerne une première étape de **caractérisation d’états précliniques**. Aucun endpoint de réponse médicamenteuse, aucune combinaison et aucun indicateur clinique ne sont disponibles ou inférés dans ce contrat.

## Séparation des objets

| Catégorie | Objets prévus | Utilisation | Interdictions |
| --- | --- | --- | --- |
| Mesure d’entrée | Quantifications RNA-seq ouvertes avec identifiants de fichier et version GDC figés. | Apprentissage de modules descriptifs. | Pas de lecture contrôlée, mutation, WGS/WXS ou donnée identifiante. |
| Flux biologiques provisoires | `TX_MODULE_01` à `TX_MODULE_06` : six facteurs transcriptomiques appris sans cible, uniquement dans chaque partition d’entraînement. | Cartographier une hétérogénéité d’expression et tester la stabilité hors modèles retenus. | Ne pas leur attribuer une voie, un gène maître ou une causalité avant annotation indépendante. |
| Contrôles techniques | Taille de bibliothèque, nombre de gènes détectés, proportions de zéros et métriques explicitement présentes dans les fichiers. | Contrôle de qualité, stratification et analyse de sensibilité. | Ne jamais les traiter comme flux biologiques ni les optimiser contre une différence tumorale. |
| Métadonnées de groupe | Type d’organoïde déclaré, type de tissu, appariement disponible, identifiant de cas/modèle, lot et plateforme. | Appariement, séparation des folds, contrôle de fuite et évaluation externe. | Ne jamais les encoder comme flux numériques ou axes de pseudo-temps. |
| Endpoints | Aucun au premier jalon. | Aucun. | Pas de viabilité, synergie, survie, réponse ou traitement fabriqué à partir du transcriptome. |

## Pourquoi six modules et non un panel de gènes présélectionné ?

Un panel de voies ou de gènes choisi d’avance risquerait d’importer une histoire mécanistique avant d’avoir vérifié les données. Les six modules seront donc construits comme axes descriptifs **non supervisés**, avec une convention gelée avant l’analyse :

1. filtres de qualité et transformation définis dans les seules partitions d’entraînement ;
2. sélection des gènes variables dans les seules partitions d’entraînement ;
3. apprentissage de six facteurs reproductibles ;
4. projection de la partition de test sans réajustement ;
5. comparaison de la stabilité des facteurs et de leur recouvrement de gènes entre folds ;
6. annotation biologique seulement après la mesure de stabilité, en gardant les annotations contradictoires.

Le nombre six est un **budget initial de représentation**, pas une vérité biologique ni un optimum tiré de résultats. Une modification ultérieure nécessitera une décision versionnée qui ne consulte aucun résultat de réponse ou de survie.

## Analyses autorisées au premier jalon

| Analyse | Autorisée ? | Condition |
| --- | --- | --- |
| Vérifier le schéma, les licences, les unités et les fichiers ouverts | Oui. | Figer la release, le manifeste et les empreintes. |
| Mesurer qualité, valeurs manquantes et hétérogénéité technique | Oui. | Rapporter les échecs et conserver les métadonnées de lot. |
| Construire les six modules descriptifs dans les folds d’entraînement | Oui. | Pas de cible clinique/médicamenteuse ; projection hors fold obligatoire. |
| Comparer des distributions entre organoïdes déclarés normaux/cancéreux | Oui, exploratoire. | Le groupe reste une évaluation, jamais une variable d’apprentissage. |
| Utiliser v3, CSD, F1′ ou F2″ | Non. | Aucune série longitudinale dense et réellement répétée n’est encore démontrée. |
| Proposer une combinaison, une dose ou un traitement | Non. | Hors portée du jalon. |

## Critères de sortie

Le contrat est validé seulement si les six modules sont techniquement définissables, reproductibles sous exclusion de modèles et séparables des artefacts techniques. Dans le cas contraire, le résultat officiel est : **« données insuffisantes pour des flux biologiques stables »**.

## Références

[1] [GDC Data Portal — ORGANOID-PANCREATIC](https://portal.gdc.cancer.gov/projects/ORGANOID-PANCREATIC)

[2] [AWS Open Data Registry — Pancreatic Cancer Organoid Profiling](https://registry.opendata.aws/organoid-pancreatic/)
