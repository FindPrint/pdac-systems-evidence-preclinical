# Reçu de construction — matrice technique `unstranded` GDC

## Résultat de construction

La matrice technique pré-spécifiée a été construite localement avec succès. Elle recopie textuellement la colonne `unstranded` des 55 TSV GDC validés, sans conversion numérique, arrondi, transformation, normalisation, filtrage biologique ou analyse statistique.

| Élément | Résultat |
| --- | --- |
| Fichiers d’entrée | 55 TSV GDC ouverts, tous revalidés par MD5 pendant la construction |
| Lignes de gènes | 60 660 |
| Colonnes de fichiers | 55 `file_id` GDC |
| Dimensions | 60 660 × 55 (`gene_id × file_id`) |
| Colonne copiée | `unstranded` uniquement |
| Lignes exclues | `N_unmapped`, `N_multimapping`, `N_noFeature`, `N_ambiguous` |
| Motif d’exclusion | Lignes de synthèse techniques, déjà contrôlées séparément |
| Matrice locale | `data/processed/GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_20260826/ORGANOID_PANCREATIC_unstranded_gene_by_file.tsv.gz` |
| Table de correspondance locale | `ORGANOID_PANCREATIC_file_map.tsv` |
| Suivi Git de la matrice et de la table | Exclu ; 0 fichier de données ajouté au dépôt |

## Empreintes de reproductibilité

| Objet | SHA-256 |
| --- | --- |
| Manifeste d’entrée gelé | `f713edebf0f8afb20305b1472d480564e45ac31ce79e28350d7dde6ae496220b` |
| Ordre des `gene_id` de la matrice | `eed79a6e4ab83f04b1dcfcd2dbf14364cd5137942aee6f89d5ecc7bced03f993` |
| Matrice gzip | `7c15bed155af6182a037e51248c865bc82a4fc2519f6a074ef210d3551f0ca4d` |
| Table de correspondance | `fe6d7a0359667e68b4b1bd50801b9f212c901c0134840c19518b7fb21e8d1b91` |

Une vérification indépendante a confirmé les dimensions `60 660 × 55`, l’ordre des `gene_id` par SHA-256, l’empreinte de la matrice, l’empreinte de la table de correspondance et l’exclusion des deux sorties de Git.

## Ce que le résultat signifie, et ne signifie pas

> La matrice est un objet technique reproductible. Elle n’est pas une analyse biologique et ne constitue pas un résultat sur le PDAC, les organoïdes, une cible, un mécanisme, un médicament ou un traitement.

La matrice comporte un fichier par colonne, non un cas par colonne : les 55 fichiers du manifeste représentent 49 cas distincts. Aucune agrégation, sélection d’échantillon ou résolution d’appariement n’a été réalisée. Les six modules transcriptomiques demeurent inactifs.

Aucune valeur n’a été résumée ni comparée. Aucun filtre de gènes, retrait de zéros, correction de batch, transformation logarithmique, normalisation, cluster, test différentiel, pseudo-temps, modèle CSD ou simulation n’a été exécuté.

Le reçu machine correspondant est `data/external-links/GDC_ORGANOID_PANCREATIC_UNSTRANDED_MATRIX_RECEIPT.json`. Le script exécutable, les règles d’arrêt et les conventions gelées sont respectivement dans `scripts/build_gdc_unstranded_matrix.py` et `protocols/PROTOCOL_002_CONSTRUCTION_MATRICE_RNASEQ_TECHNIQUE.md`.
