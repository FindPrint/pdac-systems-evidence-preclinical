# Décision 004 — Contrôle qualité numérique limité

**Date :** 26 août 2026

**État :** Autorisé par l’utilisateur ; contrôle de validité technique uniquement.

## Portée autorisée

Le contrôle peut lire les six champs de quantification afin de confirmer leur validité syntaxique et leur domaine numérique. Il n’est autorisé à produire que des indicateurs d’intégrité : nombre de cellules vides, non numériques, non finies ou négatives ; nombre d’identifiants `gene_id` dupliqués ou vides ; et statut de passage/échec par fichier. Aucune valeur individuelle, moyenne, quantile, variance, corrélation, classement ou comparaison d’expression ne doit être enregistré ou affiché.

| Élément | Règle de contrôle |
| --- | --- |
| Fichiers | Les 55 TSV ouverts du manifeste local uniquement. |
| Préambule et en-tête | Doivent rester ceux validés au jalon précédent. |
| `gene_id` | Non vide et unique à l’intérieur de chaque fichier. |
| `gene_name`, `gene_type` | Présence contrôlée ; les champs vides sont seulement signalés. |
| `unstranded`, `stranded_first`, `stranded_second` | Entier syntaxiquement valide et supérieur ou égal à zéro. |
| `tpm_unstranded`, `fpkm_unstranded`, `fpkm_uq_unstranded` | Nombre décimal fini et supérieur ou égal à zéro. |
| Résultats admis | Comptes d’anomalies et statuts techniques seulement. |

## Règles d’arrêt

Le traitement doit s’arrêter sur un écart de manifeste, une structure non conforme ou une erreur de lecture. Des anomalies de cellule n’autorisent ni correction, ni imputation, ni filtrage ; elles sont seulement consignées. Le reçu doit rester non sensible et ne contenir aucune valeur de quantification.

## Exclusions explicites

Ce jalon n’autorise pas la normalisation, l’agrégation, les statistiques d’expression, la sélection de gènes, les comparaisons entre organoïdes, l’annotation normal/cancer, l’apprentissage de modules, l’inférence mécanistique, la simulation ou toute décision thérapeutique.

## Amendement technique constaté pendant l’exécution

Le contrôle brut a d’abord signalé quatre lignes non annotées par fichier. Leur diagnostic structurel montre les mêmes quatre identifiants dans le même ordre dans les 55 fichiers : `N_unmapped`, `N_multimapping`, `N_noFeature` et `N_ambiguous`. Ils sont désormais traités comme **lignes techniques de synthèse**, non comme gènes : leur présence doit être exactement une fois par fichier, et leurs trois colonnes de compte restent contrôlées comme entiers non négatifs. L’absence d’annotation de gène et de valeurs transformées dans ces quatre lignes n’est pas assimilée à une anomalie de gène.

Cet amendement ne corrige, ne supprime et ne remplace aucune donnée. Il n’autorise aucune statistique des comptes ni aucune conclusion biologique.
