# Reçu de contrôle qualité numérique — ORGANOID-PANCREATIC

## Résultat technique

Le contrôle qualité numérique limité est **conforme** sur les 55 TSV RNA-seq ouverts importés. Il a vérifié la présence et l’unicité des identifiants, la complétude de l’annotation de gène, ainsi que la syntaxe, la finitude et la non-négativité des six colonnes de quantification. Aucune valeur individuelle n’est conservée dans ce reçu.

| Contrôle | Résultat consolidé |
| --- | --- |
| Fichiers évalués | 55 sur 55 |
| Fichiers au statut technique `pass` | 55 sur 55 |
| `gene_id` manquants | 0 |
| `gene_id` dupliqués | 0 |
| `gene_name` manquants sur lignes de gènes | 0 |
| `gene_type` manquants sur lignes de gènes | 0 |
| Champs vides, non numériques, non finis ou négatifs dans les six colonnes testées | 0 |
| Comptes non entiers dans les trois colonnes de compte | 0 |
| Lignes techniques de synthèse | 220, soit exactement 4 dans chacun des 55 fichiers |
| Identifiants techniques attendus manquants ou dupliqués | 0 |

Les quatre identifiants techniques observés uniformément sont `N_unmapped`, `N_multimapping`, `N_noFeature` et `N_ambiguous`. Ils ne sont pas assimilés à des gènes : leurs annotations de gène et valeurs transformées vides ne sont donc pas des données manquantes biologiques. Leurs colonnes de compte demeurent soumises au contrôle d’entiers non négatifs.

## Portée et non-interprétation

> Un statut `pass` établit seulement que le fichier satisfait les règles techniques pré-spécifiées. Il ne démontre pas une qualité biologique, une comparabilité entre organoïdes, une absence de biais, ni la pertinence d’une mesure pour une hypothèse donnée.

Ce jalon n’a produit ni moyenne, ni distribution, ni normalisation, ni filtrage, ni matrice, ni contrôle de batch, ni expression différentielle, ni attribution normal/cancer, ni module transcriptomique. Aucune cible, aucun médicament, aucune combinaison et aucune recommandation clinique ne sont impliqués.

L’ajustement de règle concernant les quatre lignes techniques est documenté dans `docs/decisions/DECISION_004_CONTROLE_QUALITE_NUMERIQUE_AUTORISE.md`. Le reçu machine, limité aux nombres d’anomalies et aux statuts par fichier, est `data/external-links/GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_NUMERIC_QC_RECEIPT.json`.

## Suite conditionnelle

La suite ne peut pas être une analyse automatique. Une autorisation distincte est nécessaire pour un futur jalon de préparation de matrice, qui devrait être pré-spécifié séparément : choix de colonne de quantification, traitement des quatre lignes techniques, maintien de l’identifiant de gène, tests de cohérence et règles de non-fuite. Aucun choix de gène, de seuil biologique, de médicament ou de combinaison ne serait autorisé à ce stade.
