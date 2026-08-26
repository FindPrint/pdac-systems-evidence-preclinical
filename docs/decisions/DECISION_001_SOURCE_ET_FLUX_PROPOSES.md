# DECISION_001 — Source et flux proposés pour validation

## Statut

**Proposition pré-spécifiée — en attente de validation utilisateur.** Aucun fichier de données n’a été téléchargé, aucun flux n’a été activé, et aucune analyse n’a été exécutée.

## Source proposée

Le premier jeu de données proposé est le sous-ensemble ouvert de **quantifications RNA-seq** de `ORGANOID-PANCREATIC` dans le GDC, après gel de la release et inventaire des fichiers ouverts. Le projet comporte des organoïdes pancréatiques normaux et cancéreux ; les autres modalités (lectures, WGS/WXS, mutations, jonctions) sont exclues de ce premier jalon car elles sont contrôlées ou hors contrat. [1] [2]

## Flux proposés

| Identifiant | Nature | Statut | Rôle |
| --- | --- | --- | --- |
| `TX_MODULE_01`–`TX_MODULE_06` | Six modules transcriptomiques non supervisés appris dans les partitions d’entraînement. | Proposé, non actif. | Description d’états de modèles. |
| `QC_LIBRARY_SIZE` | Taille de bibliothèque si explicitement disponible. | Proposé, non actif. | Contrôle qualité seulement. |
| `QC_DETECTED_FEATURES` | Nombre de gènes/entités détectés si explicitement disponible. | Proposé, non actif. | Contrôle qualité seulement. |
| `QC_ZERO_FRACTION` | Proportion de valeurs nulles si applicable. | Proposé, non actif. | Contrôle qualité seulement. |
| `MODEL_GROUP` | Type d’organoïde et métadonnées normal/cancer disponibles. | Proposé, non actif. | Évaluation exploratoire, jamais flux d’apprentissage. |
| `PAIRING_METADATA` | Appariement déclaré et identifiants de modèle. | Proposé, non actif. | Séparation des folds et contrôle de fuite. |

## Exclusions explicites

Les éléments suivants restent absents : réponse médicamenteuse, dose, synergie, toxicité, mutation, WGS/WXS, données sous accès contrôlé, score de survie, pseudo-temps, combinaison de médicaments, v3, CSD, F1′ et F2″.

## Règle de validation

L’import ne pourra commencer qu’après confirmation utilisateur de cette proposition. Le premier acte après confirmation sera l’inventaire des fichiers ouverts, leurs manifestes, leurs licences et leurs empreintes ; ce ne sera pas une analyse biologique.

## Références

[1] [GDC Data Portal — ORGANOID-PANCREATIC](https://portal.gdc.cancer.gov/projects/ORGANOID-PANCREATIC)

[2] [AWS Open Data Registry — Pancreatic Cancer Organoid Profiling](https://registry.opendata.aws/organoid-pancreatic/)
