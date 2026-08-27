# Inventaire de sources PDAC ouvertes ordonnées — candidature pour v3/F1′/F2″

## Cadre

Cette recherche vise des données PDAC précliniques avec un **ordre expérimental mesuré**, afin d’évaluer ultérieurement la compatibilité avec le pipeline v3 conservé. Aucun fichier de ces sources candidates n’a été téléchargé, aucune image n’a été analysée, aucune matrice n’a été lue et v3/F1′/F2″ n’a pas été exécuté.

La lecture statique de v3 montre un garde-fou d’entrée : 50 points minimum en mode `fast`, 80 en `stable` et 100 en `robust` avec les paramètres par défaut. L’interface expose une taille de fenêtre, mais tout réglage inférieur devrait être justifié et gelé avant résultat. Le module F1′/F2″ conservé est spécifique aux chemins et contrôles historiques Apamea, et ne peut pas être appliqué directement à une nouvelle source sans adaptation versionnée.

## Sources vérifiées

| Source | Axe mesuré | Données ouvertes indiquées | Compatibilité avec v3 inchangé | Décision |
| --- | --- | --- | --- | --- |
| **GSE262627** — circadien PDA | Sept temps : 0, 4, 8, 12, 16, 20, 24 h ; six organoïdes PDAC et quatre lignées cellulaires. | Comptages `featureCounts` organoïdes et lignées ; 68 échantillons GEO. | **Non** par système : 7 points est inférieur au garde-fou le plus permissif de v3. La mise en commun d’organoïdes/lignées ne serait pas une série répétée unique. | Non présélectionné pour v3 inchangé ; référence utile de design temporel authentique. |
| **OrganoIDNetData** — imagerie d’organoïdes PDAC | Acquisition toutes les 4 h jusqu’à 100 h ; noms de fichiers publics contenant des heures ; imagerie de champs de vue PDAC humains et murins avec co-culture immunitaire. | Archive Zenodo ouverte CC BY 4.0, 4,6 GB, images et annotations ; 180 images dans la notice Zenodo. | **Indéterminée mais potentiellement compatible** : une trajectoire complète pourrait fournir environ 26 positions, ce qui nécessite une configuration v3 courte explicitement gelée ; l’appartenance des images à une même trajectoire doit être vérifiée. | **Présélectionné pour inventaire de manifestes seulement**, sans téléchargement d’archive. |
| **GSE186960** — Panc1 + gemcitabine scRNA-seq | Une condition gemcitabine 24 h et comparaisons de cellules résistantes traitées ; pas une série de plusieurs instants/passage fournie dans la table de six échantillons. | Données traitées ouvertes, fichiers RDS et données brutes SRA. | Non : seulement un point de temps explicite et conditions hétérogènes. | Non retenu. |
| **ORGANOID-PANCREATIC** GDC déjà importé | Aucun axe expérimental ouvert admissible dans les 55 métadonnées de fichiers examinées. | 55 quantifications RNA-seq ouvertes. | Non comme série dynamique. | Conservé pour future analyse transversale séparée. |

## Pourquoi OrganoIDNetData est la seule présélection actuelle

La publication décrit 180 champs de vue acquis toutes les quatre heures jusqu’à 100 heures, ce qui fournit un temps réel mesuré. L’aperçu public de l’archive montre aussi des noms comprenant un identifiant de culture et un suffixe en heures, par exemple `Human_1_004h`, `Human_1_008h` et `Human_1_012h`. [1] [2] [3]

Il ne faut pas conclure que les 180 images constituent déjà une unique série utilisable. La publication indique que les images sont des champs de vue issus de cultures humaines et murines, certaines en co-culture avec cellules immunitaires ; l’archive mélange aussi images, masques, augmentations et sorties de modèles. Une extraction non contrôlée risquerait de mélanger systèmes, champs de vue ou dérivés artificiels. L’inventaire de manifestes doit donc précéder tout import et toute définition de flux.

Une divergence documentaire est elle-même consignée : la notice Zenodo et l’article Science Data indiquent 180 images, tandis que le README du dépôt public associé annonce 190 images. Cette discordance devra être résolue à partir de l’inventaire réel de l’archive avant toute utilisation.

## Limites et décision

> Une série ordonnée est nécessaire mais insuffisante. Pour exécuter v3 de manière défendable, il faudra vérifier la longueur par trajectoire, l’identité du système suivi, l’absence d’images augmentées dans les trajectoires, la régularité de la cadence, les réplicats, la définition de flux physiques et une configuration pré-spécifiée.

Aucune source ne satisfait actuellement, sur la seule documentation accessible, tous les critères pour une exécution **inchangée** de v3 avec ses paramètres par défaut. OrganoIDNetData est néanmoins la meilleure piste pour une future évaluation de compatibilité : elle offre un ordre temporel réel et des annotations permettant potentiellement de dériver des flux morphologiques, sans sélectionner de gène ou de médicament.

La seule action recommandée au prochain jalon est un inventaire **metadata-only** de l’archive OrganoIDNetData : noms de fichiers, tailles, MD5, structure des dossiers et correspondance déclarée entre culture/champ de vue/heure. Ce jalon ne téléchargerait pas l’archive de 4,6 GB, ne consulterait aucune image et n’exécuterait aucun pipeline.

## Références

[1] [GEO GSE262627](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE262627)

[2] [Sharma et al., JCI Insight, 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11141942/)

[3] [OrganoIDNetData — Zenodo](https://zenodo.org/records/10643410)

[4] [Kulkarni et al., Scientific Data, 2024](https://www.nature.com/articles/s41597-024-03631-3)

[5] [GEO GSE186960](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE186960)
