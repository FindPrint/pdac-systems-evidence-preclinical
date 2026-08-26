# PDAC Systems Evidence & Preclinical Falsification

> **Recherche préclinique uniquement.** Ce dépôt ne produit ni diagnostic, ni recommandation thérapeutique, ni dose, ni calendrier de traitement. Il organise des hypothèses falsifiables sur des systèmes PDAC et leurs validations expérimentales indépendantes.

## Objet du projet

Ce projet construit une infrastructure de preuve pour relier, sans les confondre, des mesures expérimentales, des signatures biologiques, des mécanismes documentés, des scénarios de simulation et des validations hors échantillon. L’objectif est de rechercher des hypothèses précliniques qui examinent conjointement activité anti-tumorale, sélectivité vis-à-vis de contrôles non tumoraux et résistance/durabilité.

Aucune donnée individuelle de patient, donnée sous accès contrôlé, donnée brute volumineuse ou information identifiante ne doit être versionnée. Les ressources externes sont référencées, versionnées et contrôlées par leurs licences.

## État initial

| Domaine | État |
| --- | --- |
| Gouvernance et sécurité | Défini et versionné. |
| Architecture de preuve | Définie et versionnée. |
| Sources précliniques candidates | Vérifiées comme références, non téléchargées. |
| Données expérimentales | Aucune importée. |
| Code de modélisation | Aucun code non audité importé. |
| Hypothèses de combinaison | Aucune active. |
| Sorties cliniques | Explicitement interdites. |

## Principes non négociables

1. Une source doit disposer d’une provenance, d’une version, d’une licence et d’une empreinte avant toute analyse.
2. Les séries longitudinales réelles, les cohortes transversales et les simulations sont des couches distinctes.
3. Une variable de résultat clinique futur ne peut jamais créer un pseudo-temps ni entrer comme prédicteur.
4. Une simulation génère un scénario incertain ; elle ne produit pas une efficacité clinique, une dose ou une recommandation.
5. Une hypothèse doit inclure une contradiction connue et un test pré-spécifié susceptible de l’infirmer.
6. Les résultats négatifs, les réplications manquées et les paramètres non identifiables sont des résultats à conserver.
7. Les étapes importantes font l’objet d’un commit, d’un manifeste SHA-256 et, si des artefacts lourds existent, d’une archive de release vérifiable.

## Premier jalon

Le premier jalon est le **registre d’évidence préclinique**. Il définit les contrats de données, les types de flux, les règles de non-fuite, les fiches d’hypothèse et les plans de falsification. Aucun traitement ni combinaison n’est proposé à ce stade.

Les documents de cadrage sont dans `docs/`; les futurs enregistrements contrôlés seront dans `registry/`; les liens de données admissibles seront dans `data/external-links/`.

## Périmètre historique

Le pipeline v3 original et le module dérivatif CSD F1′/F2″ sont préservés séparément comme références historiques. Ils ne sont ni copiés ni exécutés dans ce dépôt tant qu’un audit de transférabilité spécifique n’a pas été validé.
