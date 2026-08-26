# PROTOCOL_000 — Registre d’évidence préclinique PDAC

## Statut et portée

Ce protocole inaugure un programme de recherche préclinique. Il ne permet aucune recommandation clinique, aucune sélection de traitement, aucune posologie et aucune interprétation applicable à un patient individuel.

## Question du jalon

> Comment structurer, vérifier et relier les sources précliniques PDAC afin qu’une future hypothèse de combinaison puisse être explicitement corroborée, contredite ou laissée indéterminée ?

## Objets admis

| Objet | Exigences minimales | Statut à défaut |
| --- | --- | --- |
| Source de données | URL/DOI, version, licence, description d’accès et contenu. | Non admissible. |
| Variable | Nom, unité, type, transformation et rôle analytique. | Non admissible. |
| Hypothèse | Question, signal source, mécanisme, contradiction et test de falsification. | Brouillon non actif. |
| Paramètre de modèle | Source ou distribution explicitée, unité et domaine. | Inconnu ; non utilisable comme fait. |
| Benchmark | Séparation de calibration/évaluation, entités indépendantes et métrique pré-spécifiée. | Démonstration interne seulement. |

## Règles de non-fuite

Les variables de survie, réponse ou toxicité futures ne peuvent pas être transformées en axe temporel, en contrôles ou en prédicteurs. Les identifiants de patient, échantillon, lot et expérience servent à l’appariement et à la séparation des ensembles, jamais à l’apprentissage d’un signal biologique.

Une analyse ne peut pas utiliser un même modèle expérimental, une même combinaison ou une même série de mesures à la fois pour choisir les paramètres et pour les évaluer. Toute sélection après inspection est déclarée exploratoire.

## Validation et sortie

Le jalon est réussi lorsqu’un lecteur indépendant peut répondre, pour chaque objet : d’où vient-il, qu’est-ce qu’il mesure, quelle transformation lui a été appliquée, quelle question il peut traiter, et quel résultat l’infirmerait.

Les seules sorties admises sont : `admissible`, `à compléter`, `exploratoire`, `corroboration limitée`, `contredit` ou `indéterminé`.
