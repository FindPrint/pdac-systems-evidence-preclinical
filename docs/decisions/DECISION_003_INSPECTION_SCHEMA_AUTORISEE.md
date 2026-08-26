# Décision 003 — Inspection descriptive du schéma RNA-seq

**Date :** 26 août 2026

**État :** Autorisée par l’utilisateur ; exécution non analytique.

## Portée autorisée

L’utilisateur autorise une inspection structurale des 55 fichiers TSV RNA-seq ouverts déjà importés. Cette inspection peut lire l’en-tête et parcourir les lignes afin de vérifier la largeur tabulaire, de compter les lignes, de contrôler l’absence d’identifiant primaire vide et de produire des empreintes de schéma et de séquence d’identifiants. Elle peut comparer ces propriétés entre fichiers.

| Élément | Autorisé |
| --- | --- |
| En-tête et noms de colonnes | Oui. |
| Nombre de colonnes et lignes | Oui. |
| Identifiant primaire de chaque ligne | Oui, uniquement pour les contrôles de présence et d’empreinte. |
| Cohérence de la structure entre fichiers | Oui. |
| Valeurs de compte ou d’expression | Non : ni extraction, ni résumé, ni conversion numérique. |
| Normalisation, filtrage, clustering ou différence d’expression | Non. |
| Comparaison normal/cancer ou attribution de phénotype | Non. |
| Modules transcriptomiques, cibles ou hypothèses thérapeutiques | Non. |

## Règles d’arrêt

L’inspection doit s’arrêter et produire un reçu partiel si l’ensemble local diffère du manifeste, si un fichier est illisible, si la largeur tabulaire varie à l’intérieur d’un fichier ou si les schémas ne sont pas homogènes. Aucun correctif de données, aucune suppression de ligne et aucune imputation ne sont autorisés.

## Résultat attendu

Le résultat doit être un reçu de structure non sensible, traçant les en-têtes, les comptes de lignes et de colonnes, les empreintes de séquence d’identifiants et tout écart observé. Les TSV bruts demeurent exclus de Git. Cette étape ne constitue pas une analyse biologique, préclinique ou clinique.
