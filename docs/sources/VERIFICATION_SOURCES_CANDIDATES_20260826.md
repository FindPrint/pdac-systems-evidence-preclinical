# Vérification des sources candidates — 26 août 2026

> Cette note vérifie les métadonnées et l’accès avant toute importation. Elle ne constitue pas une analyse de données et ne promeut aucune cible ni combinaison.

## Candidat A — ORGANOID-PANCREATIC (GDC)

| Critère | Constat vérifié | Décision provisoire |
| --- | --- | --- |
| Origine | Projet `ORGANOID-PANCREATIC`, intitulé « Pancreas Cancer Organoid Profiling », hébergé par le GDC/NCI. [1] | Provenance institutionnelle établie. |
| Taille déclarée | 70 cas et 966 fichiers dans la version affichée au 26 août 2026. [1] | Cohorte définie, à figer au moment de l’import. |
| Modalités | RNA-seq pour 49 cas ; WGS pour 22 ; WXS pour 69, parmi les comptes GDC affichés. [1] | Les modalités doivent rester séparées. |
| Accès | Le GDC signale des données contrôlées nécessitant dbGaP ; l’AWS Open Data Registry indique que les quantifications d’expression RNA-seq sont ouvertes alors que lectures alignées, mutations et jonctions restent contrôlées. [1] [2] | Candidat admissible uniquement pour le sous-ensemble ouvert de quantifications RNA-seq, après inventaire précis des fichiers. |
| Contrôles | La notice AWS décrit des organoïdes pancréatiques normaux et cancéreux, avec tissu apparié lorsque disponible. [2] | Potentiel de contrôle préclinique ; appariement à vérifier fichier par fichier. |
| Limite | Les données GDC sont provisoires et les pipelines évoluent selon les notes de release. [1] | Version de release et manifeste obligatoires. |

## Candidat B — SYNERGxDB

Le portail public se présente comme une ressource d’exploration de combinaisons synergiques pour la découverte de biomarqueurs. [3] Lors de la vérification du 26 août 2026, son compteur public retournait des valeurs nulles ; le contenu, la version, la licence et l’accès programmatique ne sont donc pas assez stables pour servir de première source sans vérification supplémentaire.

**Décision provisoire :** benchmark secondaire non retenu pour le démarrage.

## Conclusion de sélection provisoire

Le projet `ORGANOID-PANCREATIC`, limité aux quantifications RNA-seq réellement ouvertes, est le meilleur candidat pour un **premier jalon de caractérisation préclinique**. Il ne fournit pas nécessairement une réponse de combinaison ou un endpoint de sécurité ; ces éléments ne seront donc pas inférés ni remplacés par une simulation.

## Références

[1] [GDC Data Portal — ORGANOID-PANCREATIC](https://portal.gdc.cancer.gov/projects/ORGANOID-PANCREATIC)

[2] [AWS Open Data Registry — Pancreatic Cancer Organoid Profiling](https://registry.opendata.aws/organoid-pancreatic/)

[3] [SYNERGxDB](https://synergxdb.ca/)
