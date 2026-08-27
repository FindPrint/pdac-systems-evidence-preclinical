# PROTOCOL_003 — Recherche de séries PDAC ouvertes ordonnées

## Objet et limite

Ce protocole définit la recherche d’un jeu de données PDAC qui pourrait, après vérification et autorisation distincte, servir à évaluer techniquement le pipeline v3 et le module CSD F1′/F2″ sur un axe réellement mesuré. À ce stade, aucune donnée n’est téléchargée, aucune matrice n’est analysée et aucun code v3 n’est exécuté.

## Critères d’inclusion

| Critère | Exigence minimale |
| --- | --- |
| Domaine | PDAC, organoïdes PDAC, lignées cellulaires PDAC ou modèle préclinique PDAC explicitement documenté. |
| Accessibilité | Données et table d’échantillons accessibles ouvertement, sans identifiants individuels ni accès contrôlé. |
| Mesure | RNA-seq, transcriptomique ou série de flux moléculaires clairement documentée. |
| Axe ordonné | Temps, passage, cycle, dose, concentration ou autre variable expérimentale mesurée avec unité ou niveaux explicitement définis. |
| Répétition | Au moins trois positions ordonnées ; les réplicats et la structure de lot doivent être indiqués lorsqu’ils existent. |
| Traçabilité | Accession stable, table d’échantillons et publication ou protocole décrivant le design. |
| Séparation | L’axe d’ordre ne doit pas être une survie clinique, une réponse patient, un classement par expression ou un pseudo-temps inféré. |

La préférence va à un suivi répété d’un même système. Une série de doses ou de passages peut être retenue comme axe expérimental si elle est explicitement définie, mais elle devra être interprétée comme réponse le long de cette condition — jamais comme temps intrinsèque du cancer.

## Exclusions

Sont exclus les jeux sans table de métadonnées par échantillon, les cohortes purement transversales, les études où l’ordre est seulement administratif, les données sous accès contrôlé, les données cliniques identifiantes, et les séries dont l’ordre serait dérivé de survie, de résultat thérapeutique ou du transcriptome lui-même.

## Grille de vérification

| Question | Réponse attendue avant toute présélection |
| --- | --- |
| Quelle variable ordonne la série ? | Nom, unité, définition et sens de l’axe. |
| Combien de positions et de réplicats ? | Décompte documenté, sans estimation. |
| Quel système est répété ? | Même organoïde, lignée, modèle ou unité expérimentale clairement indiquée. |
| Où sont les données et la table d’échantillons ? | URL/accession ouverte et stable. |
| Quel est le risque principal de confusion ? | Lot, lignée, donneur, dosage, préparation ou autre facteur documenté. |
| Quel résultat est permis ? | Compatibilité technique / exploratoire ; jamais prescription, dose ou pronostic clinique. |

## Sorties de cette étape

La sortie autorisée est une comparaison documentée de sources candidates avec les statuts « présélectionné pour vérification », « non retenu » ou « indéterminé ». Une présélection n’est pas une autorisation de téléchargement ni d’exécution de v3/F1′/F2″.
