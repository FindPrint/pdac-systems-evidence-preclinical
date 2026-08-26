# Sources précliniques PDAC vérifiées — fondation du redémarrage

> Ces sources servent à concevoir une recherche préclinique et à distinguer données ouvertes, données contrôlées, observations expérimentales et simulations. Elles ne valident aucun traitement ni aucune décision clinique.

## Modèles organoïdes pancréatiques

| Source | Contenu vérifié | Utilisation possible | Limites et précautions |
| --- | --- | --- | --- |
| Pancreatic Cancer Organoid Profiling — AWS Open Data Registry / GDC | Collection d’organoïdes pancréatiques normaux et cancéreux dérivés de patients, avec WGS, WXS et RNA-seq ainsi que tissu tumoral/normal apparié lorsque disponible. Les quantifications d’expression RNA-seq sont ouvertes ; lectures alignées, mutations et jonctions sont sous accès contrôlé. [1] | Source ouverte candidate pour un premier graphe de données organoïdes : transcriptome, origine, version GDC et cohorte. | Aucun fichier sous accès contrôlé ne doit être téléchargé ni placé dans Git. L’expression ouverte ne constitue pas à elle seule une réponse médicamenteuse. |
| Grossman et al. — HOPE trial | Étude prospective de faisabilité de PDO PDAC ; la sensibilité des organoïdes a été comparée aux réponses cliniques. L’étude décrit explicitement les limites de faisabilité, de délai, de coût et de passage en clinique. [2] | Référence méthodologique pour séparer la mesure de réponse d’organoïde, le délai de production, la faisabilité de culture et toute interprétation clinique. | Le papier ne justifie pas qu’un programme computationnel recommande un traitement ; il met au contraire en évidence la nécessité d’essais prospectifs. |

## Bases de combinaisons et de synergie

| Source | Contenu vérifié | Utilisation possible | Limites et précautions |
| --- | --- | --- | --- |
| SYNERGxDB | Base présentant 9 jeux, 15 tissus, 149 lignées, 1 946 composés, 22 149 combinaisons, 528 055 expériences et 6 572 285 mesures. [3] | Source externe de benchmarking et de contradictions pour des hypothèses de synergie ; les effets peuvent être étudiés par lignée et combinaison. | La présence d’une combinaison ne prouve ni pertinence PDAC ni sécurité humaine. Vérifier versions, licences et données par étude avant téléchargement. |
| Therapeutics Data Commons — DrugComb/DrugSyn | DrugComb agrège 129 médicaments sur 59 lignées et 297 098 paires cellule–combinaison ; plusieurs métriques de synergie sont explicitement distinctes : Bliss, HSA, Loewe, ZIP et CSS. [4] | Benchmark préclinique de généralisation hors lignée et hors combinaison, avec la métrique de synergie maintenue comme une mesure expérimentale et non une décision. | Le jeu NCI-60 n’est pas spécifique au PDAC. Toute analyse PDAC doit séparer lignes PDAC, autres tissus et extrapolation. |

## Conséquence pour le nouveau projet

Le nouveau projet peut démarrer de façon plus robuste qu’un pseudo-temps clinique :

1. utiliser des sources organoïdes et de synergie comme couches **précliniques distinctes** ;
2. traiter une réponse ou une synergie mesurée comme une observation, avec métrique explicitement nommée ;
3. réserver le modèle de système dynamique à la génération de scénarios et à la conception de tests de falsification ;
4. imposer une validation hors lignée, hors combinaison et, lorsque possible, hors laboratoire ;
5. ne jamais traduire un score de synergie, une simulation ou un signal omique en traitement ou posologie pour un patient.

## Références

[1] [AWS Open Data Registry — Pancreatic Cancer Organoid Profiling](https://registry.opendata.aws/organoid-pancreatic/)

[2] [Grossman et al. — Organoid Sensitivity Correlates with Therapeutic Response in Patients with Pancreatic Cancer, *Clinical Cancer Research* (2022)](https://doi.org/10.1158/1078-0432.CCR-20-4116)

[3] [SYNERGxDB](https://synergxdb.ca/)

[4] [Therapeutics Data Commons — Drug Synergy Prediction](https://tdcommons.ai/multi_pred_tasks/drugsyn/)
