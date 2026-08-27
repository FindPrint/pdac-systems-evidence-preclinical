# Reçu d’inventaire — axes expérimentaux ouverts GDC

## Question et conclusion

L’inventaire a recherché un axe expérimental **directement mesuré** pouvant éventuellement ordonner les 55 profils RNA-seq GDC. La réponse est : **aucun axe admissible n’a été identifié dans les métadonnées ouvertes examinées**.

Cette conclusion ne signifie pas qu’aucune information expérimentale n’existe ailleurs dans l’étude. Elle signifie seulement qu’aucun temps, passage, cycle, dose, concentration, condition graduée, coordonnée spatiale ou autre progression mesurée n’apparaît dans la réponse de métadonnées ouverte gelée pour ces 55 fichiers, avec une définition permettant de l’utiliser comme ordre.

## Inventaire structurel

L’inventaire automatique de la réponse GDC a trouvé 18 chemins de champs, présents sur les 55 fichiers. Il n’a enregistré aucune valeur individuelle de métadonnée ni aucune valeur RNA-seq.

| Groupe de champs trouvé | Couverture | Décision comme axe |
| --- | --- | --- |
| `file_id`, `file_name`, `id`, `md5sum`, `file_size` | 55/55 | Exclu : identifiants, contrôle d’intégrité ou propriété de fichier. |
| `access`, `data_format`, `data_type`, `experimental_strategy`, `analysis.workflow_type` | 55/55 | Exclu : provenance et technique de traitement, pas progression expérimentale. |
| `cases[].case_id`, `cases[].submitter_id` | 55/55 | Exclu : identifiants de cas. |
| `cases[].samples[].sample_type` | 55/55 | Exclu : étiquette catégorielle, pas ordre ni répétition mesurée. |
| `created_datetime`, `updated_datetime` | 55/55 | Exclu : dates de métadonnées de fichier sans définition d’acquisition expérimentale. |

Aucun champ dont le nom indique `time`, `passage`, `duration`, `cycle`, `dose`, `concentration`, `treatment`, `condition`, `stage`, `spatial`, `coordinate`, `serial` ou `sequence` n’est présent dans cette réponse de 55 fichiers.

## Interprétation méthodologique

Les seules dates trouvées sont `created_datetime` et `updated_datetime`. En l’absence d’une définition source les reliant à l’acquisition expérimentale ou à l’évolution d’un même organoïde, elles satisfont les exclusions pré-spécifiées de la Décision 005. Les utiliser pour classer les fichiers créerait un ordre administratif, non un ordre biologique mesuré.

La documentation GDC distingue les champs disponibles des différents endpoints, et les pages publiques de la collection décrivent des organoïdes pancréatiques profilés par RNA-seq, WGS et WXS. Elles ne fournissent pas, dans les pages examinées, une série temporelle ou de passages attribuable à chaque fichier RNA-seq ouvert. [1] [2] [3]

> Il est donc possible de faire fonctionner un code sur un ordre conventionnel, mais il n’est pas justifié de qualifier ses dérivées, CSD ou seuils de dynamique biologique pour ce sous-ensemble précis. Aucun ordre de ce type n’a été créé ici.

## Conséquence pour v3 et F1′/F2″

L’inventaire n’autorise pas l’exécution interprétable de v3 ou du module F1′/F2″ comme analyse dynamique sur les 55 fichiers actuels. Il autorise seulement à conclure que ce sous-ensemble est, avec les métadonnées ouvertes examinées, **transversal pour cette question**.

Les voies futures sont distinctes : obtenir ou trouver une série PDAC avec ordre expérimental documenté pour une application dynamique, ou utiliser les 55 profils transversaux dans une méthode explicitement transversale après autorisation séparée. Ni l’une ni l’autre n’est réalisée par ce reçu.

## Références

[1] [GDC Data Portal — ORGANOID-PANCREATIC](https://portal.gdc.cancer.gov/projects/ORGANOID-PANCREATIC)

[2] [AWS Open Data Registry — Pancreatic Cancer Organoid Profiling](https://registry.opendata.aws/organoid-pancreatic/)

[3] [GDC API — Appendix A: Available Fields](https://docs.gdc.cancer.gov/API/Users_Guide/Appendix_A_Available_Fields/)
