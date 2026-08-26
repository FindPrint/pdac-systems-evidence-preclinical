# Architecture proposée — PDAC Systems Evidence & Preclinical Falsification

> **Portée.** Cette architecture vise un programme de recherche préclinique. Ses sorties sont des hypothèses, des résultats de réplication, des analyses de sensibilité et des plans de falsification. Elle ne fournit aucune recommandation de traitement, de dose ou de calendrier pour un patient.

## 1. Objectif opérationnel

Le projet cherche à construire une chaîne de preuves capable d’évaluer simultanément trois dimensions :

| Dimension | Question préclinique | Mesure attendue | Échec à documenter |
| --- | --- | --- | --- |
| Activité anti-tumorale | L’hypothèse diminue-t-elle la croissance ou la viabilité dans plusieurs modèles tumoraux ? | Viabilité, croissance, apoptose, clonogénicité ou lecture équivalente mesurée. | Absence d’effet, effet seulement dans une lignée ou contradiction inter-modèle. |
| Sélectivité/protection | L’effet épargne-t-il relativement des modèles non tumoraux ou des indicateurs de tissu sain dans le même système expérimental ? | Contrôles normaux appariés quand disponibles, fenêtre de sélectivité expérimentale et marqueurs de dommage. | Toxicité comparable ou supérieure dans les contrôles non tumoraux. |
| Durabilité/résistance | Le système récupère-t-il, s’adapte-t-il ou sélectionne-t-il un état résistant après exposition ? | Mesures répétées, reprise de croissance, évolution de signatures ou passages expérimentaux. | Repousse, plasticité ou échappement observé. |

L’objectif n’est pas qu’un seul score soit bon. Une hypothèse doit rester interprétable lorsque ces trois dimensions divergent.

## 2. Types de flux autorisés

Un « flux » devient une variable explicitement typée. Cela conserve l’intuition multi-flux du projet initial tout en empêchant les mélanges conceptuels.

| Type | Exemples admissibles | Rôle | Ne doit jamais être utilisé comme |
| --- | --- | --- | --- |
| Mesure brute | Viabilité, dosage, comptage de cellules, RNA-seq, ctDNA longitudinal, imagerie quantitative. | Observation. | Score de priorité sans transformation documentée. |
| Flux dérivé | Score de signature versionné, pente de croissance, AUC, métrique Bliss/HSA/Loewe/ZIP nommée. | Résumé analytique. | Mesure directe ou preuve causale. |
| Qualité/technique | Lot, plateforme, profondeur, passage d’organoïde, temps de culture. | Contrôle, stratification et diagnostic. | Biomarker thérapeutique. |
| Mécanisme | Interaction gène–voie–médicament avec source. | Hypothèse causale à tester. | Fait démontré sans expérience appropriée. |
| Endpoint expérimental | Viabilité, toxicité, reprise de croissance, intégrité de contrôle normal. | Critère de validation. | Axe pseudo-temporel. |
| Temps réel | Heure, jour, cycle, passage et moment d’exposition réellement mesurés. | Analyse de dynamique éventuelle. | Rang de survie ou score clinique futur. |

## 3. Modules du projet

```text
00_governance/
  safety_scope.md
  data_access_policy.md
  evidence_levels.yaml

01_source_registry/
  sources.tsv
  licenses.tsv
  frozen_versions.tsv
  sha256/

02_data_contracts/
  organoid_schema.json
  synergy_schema.json
  longitudinal_schema.json
  variable_registry.tsv

03_quality_and_cohorting/
  sample_patient_mapping.py
  batch_quality.py
  missingness_report.py
  normal_tumor_pairing.py

04_empirical_analysis/
  cross_model_association.py
  leave_one_model_out.py
  resistance_trajectories.py
  sensitivity_to_preprocessing.py

05_evidence_graph/
  hypotheses/
  mechanisms/
  contradictions/
  experiment_plans/

06_mechanistic_scenarios/
  parameter_registry.tsv
  calibration.py
  uncertainty_propagation.py
  competing_models.py

07_external_falsification/
  held_out_cell_lines.py
  held_out_organoids.py
  held_out_combinations.py
  reporting.py

08_reports_and_archives/
  protocol.md
  negative_results.md
  MANIFEST_SHA256.txt
  release-assets/
```

## 4. Règles de passage entre modules

| Passage | Condition minimale | Sortie si la condition échoue |
| --- | --- | --- |
| Source → analyse | Source, version, licence, unités, échantillons et contraintes documentés. | Donnée non admissible ; pas d’import silencieux. |
| Analyse → hypothèse | Association reproductible dans au moins deux partitions indépendantes ou signal longitudinal avec ordre réel confirmé. | Signal exploratoire seulement. |
| Hypothèse → simulation | Chaîne mécanistique sourcée, alternatives et paramètres inconnus identifiés. | Scénario narratif non calculable. |
| Simulation → benchmark | Paramètres de calibration séparés des données d’évaluation ; incertitude propagée. | Modèle non validé. |
| Benchmark → prochaine expérience | Critères de succès/échec, contrôles tumoraux/non tumoraux et métrique de synergie pré-spécifiés. | Hypothèse incomplète. |

## 5. Le premier jalon recommandé

Le premier jalon s’appelle **« Registre d’évidence préclinique PDAC »**. Il ne télécharge encore aucune grande matrice et ne propose aucune combinaison. Il produit :

1. un contrat de données pour organoïdes, lignées, synergies et séries répétées ;
2. un registre de variables qui interdit la fuite d’endpoint et le pseudo-temps ;
3. un format de fiche d’hypothèse avec mécanisme, contradiction et test de falsification ;
4. un registre de paramètres où chaque constante est soit sourcée, soit une distribution déclarée, soit « inconnue » ;
5. un protocole de benchmark hors lignée, hors combinaison et hors lot ;
6. un rapport de non-usage clinique et de limites.

La première analyse après ce jalon pourra comparer des combinaisons dans des ressources de synergie ou d’organoïdes. Elle devra poser la question restreinte :

> Une hypothèse de combinaison conserve-t-elle une activité mesurée dans des modèles PDAC indépendants tout en évitant une perte relative de sélectivité dans les contrôles précliniques disponibles ?

## 6. Réutilisation responsable de v3 et F1′/F2″

Le pipeline v3 et le module F1′/F2″ sont préservés comme références de méthodes exploratoires. Ils pourront inspirer des diagnostics de stabilité de séries réellement répétées, mais ils ne seront pas portés directement dans le projet PDAC.

| Élément historique | Statut dans le nouveau projet |
| --- | --- |
| Monte Carlo d’exploration de paramètres | Référence méthodologique seulement ; tout échantillonnage doit être seedé, pré-spécifié et ne pas choisir une décision biomédicale. |
| CSD/variance/autocorrélation | Possible uniquement sur mesures longitudinales réelles et suffisamment denses ; toujours signal candidat. |
| F1′ post-seuil / F2″ pré-seuil | Réservé à une étude de séries temporelles expérimentales ; pas de seuil entraîné sur outcome clinique. |
| Cartes de partitions et recouvrements | Remplacées par recouvrements entre lignées, organoïdes, lots et cohortes externes. |
| Tests de bruit | Recréés comme tests de lot, répétition, incertitude de mesure et données manquantes. |

## 7. Critère de maturité du projet

Le projet est considéré « prêt à proposer une expérience préclinique » seulement si :

- la source et les conditions d’utilisation de tous les fichiers sont vérifiées ;
- l’hypothèse reste après exclusion d’un modèle entier ;
- une contradiction ou une absence de réplication est correctement rapportée ;
- les paramètres de simulation n’ont pas été ajustés sur le benchmark réservé ;
- les contrôles de tissu sain ou de sélectivité sont explicitement disponibles, ou leur absence est déclarée comme limite ;
- un protocole de falsification indépendant est formulé ;
- aucune phrase ne propose d’utilisation chez un patient.

Cette architecture est plus ambitieuse que le pipeline actuel parce qu’elle n’optimise pas seulement un signal : elle organise la **preuve positive, l’incertitude et la preuve négative** dans une même structure reproductible.
