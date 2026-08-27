# Statut du projet

| Élément | État au 27 août 2026 |
| --- | --- |
| Périmètre | Recherche préclinique PDAC, non clinique. |
| Source RNA-seq importée | Sous-ensemble ouvert `ORGANOID-PANCREATIC` GDC ; 55 TSV locaux hors de Git. |
| Intégrité, schéma et QC RNA-seq | Vérifiés : 55/55 MD5 et tailles ; schéma homogène ; QC numérique conforme. |
| Matrice technique RNA-seq | Locale : 60 660 `gene_id` × 55 `file_id`, `unstranded` seulement ; exclue de Git. |
| Axe expérimental GDC admissible | Aucun identifié dans les métadonnées ouvertes examinées ; aucun pseudo-temps créé. |
| v3 / F1′ / F2″ sur le sous-ensemble GDC | Non exécutés comme dynamique. |
| Préconditions v3 conservé | Au moins 50 points en mode `fast`, 80 en `stable`, 100 en `robust` avec paramètres par défaut ; contrôle numérique à ordre réel requis. |
| Candidat externe à axe réel | `GSE262627` : série circadienne authentique mais 7 temps par système, donc non compatible avec v3 inchangé. |
| Candidat externe présélectionné | `OrganoIDNetData` : imagerie PDAC avec heures documentées ; présélection limitée à l’inventaire metadata-only de l’archive. |
| Téléchargement OrganoIDNetData | Non effectué. |
| Analyse d’image, flux morphologiques ou exécution v3 | Non effectuées. |
| Modules transcriptomiques | Aucune variable active ; les six modules restent inactifs. |
| Données contrôlées / patient individuelles | Non téléchargées, non versionnées et interdites dans le dépôt. |
| Hypothèses de combinaison et simulations | Aucune active ou exécutée. |
| v3 et module F1′/F2″ | Conservés séparément comme références historiques non modifiées. |
| Prochain jalon conditionnel | Inventaire Zenodo metadata-only d’OrganoIDNetData après autorisation utilisateur explicite. |

## Décision de portée

La recherche distingue maintenant deux voies non interchangeables. La première est la transcriptomique transversale GDC, qui ne reçoit pas un ordre artificiel. La seconde cherche des mesures précliniques réellement ordonnées susceptibles d’évaluer votre pipeline. `OrganoIDNetData` est seulement une piste documentaire : l’archive d’images, les masques et les scripts tiers ne sont ni téléchargés, ni exécutés, ni analysés. Toute future exécution de v3 resterait exploratoire, hors contexte clinique et soumise à validation indépendante.
