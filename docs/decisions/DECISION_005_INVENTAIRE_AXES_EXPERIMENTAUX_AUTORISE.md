# Décision 005 — Inventaire d’axes expérimentaux ouverts

**Date :** 26 août 2026

**Statut :** autorisé pour inventaire de métadonnées uniquement ; aucune exécution de v3 ou F1′/F2″ n’est autorisée par cette décision.

## Question traitée

Le projet doit déterminer si les métadonnées ouvertes des 55 fichiers RNA-seq GDC contiennent un axe expérimental réellement mesuré, qui pourrait éventuellement ordonner les observations pour un futur essai de compatibilité de pipeline. Cet inventaire ne lit pas les valeurs de la matrice RNA-seq et ne déduit aucun axe à partir de l’expression.

## Critères d’admissibilité

| Critère | Exigence |
| --- | --- |
| Origine | Champ fourni par la source, et non calculé à partir du transcriptome. |
| Nature | Temps, durée, passage, cycle, dose, concentration, série spatiale ou autre mesure explicitement ordonnée. |
| Définition | Unité, convention et sens de progression documentés par la source. |
| Portée | Défini pour chaque fichier ou de manière traçable pour un sous-ensemble clairement déclaré. |
| Répétition | Mesures répétées d’un système, ou design expérimental rendant l’ordre comparable. |
| Réplicats | Réplicats, lots et appariements identifiables lorsque disponibles. |
| Falsifiabilité | L’ordre peut être vérifié indépendamment à partir des métadonnées ou de la documentation source. |

Un axe n’est considéré que comme **candidat** s’il satisfait tous les critères. La conclusion « aucun axe admissible identifié » est une sortie valable et ne bloque pas les analyses transversales futures ; elle interdit seulement une interprétation dynamique du pipeline.

## Exclusions

Les identifiants de fichier, identifiants de cas, noms de fichiers, dates administratives de soumission ou de publication, taille de fichier, ordre d’API, ordre alphabétique, métadonnées cliniques, survie, réponse clinique, étiquettes normal/cancer et toute grandeur apprise du transcriptome sont exclus comme axes d’ordonnancement. Aucune de ces variables ne doit être convertie en pseudo-temps.

## Sorties autorisées

L’inventaire peut produire la liste de champs disponibles, leur couverture, leur type apparent et une décision d’admissibilité. Il ne peut ni ordonner les 55 fichiers selon une règle nouvelle, ni sélectionner des flux, ni exécuter v3/CSD/F1′/F2″, ni produire un seuil ou une interprétation biologique.
