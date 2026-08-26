# Statut du projet

| Élément | État au 26 août 2026 |
| --- | --- |
| Périmètre | Recherche préclinique PDAC, non clinique. |
| Source importée | Sous-ensemble ouvert `ORGANOID-PANCREATIC` de quantifications RNA-seq GDC. |
| Quantifications locales | 55 TSV, uniquement dans `data/raw/` exclu de Git. |
| Intégrité de transfert | 55/55 tailles et MD5 GDC vérifiés indépendamment ; aucun fichier partiel ni non déclaré. |
| Schéma technique | Vérifié sur 55/55 : préambule GENCODE v36, 9 colonnes, 60 664 lignes de données et même séquence de `gene_id`. |
| Données patient individuelles | Interdites dans le dépôt. |
| Données contrôlées | Non téléchargées et non versionnées. |
| Valeurs RNA-seq | Ni extraites, ni converties, ni résumées, ni comparées. |
| Contrôle qualité des valeurs | Non effectué. |
| Normalisation, filtrage, modules transcriptomiques | Non effectués ; les six modules restent inactifs. |
| Modèles de simulation | Aucun modèle importé ou exécuté. |
| Hypothèses de combinaison | Aucune active. |
| Code de l’archive `tlog28` | Lu statiquement seulement ; non copié dans ce dépôt. |
| v3 et module F1′/F2″ | Conservés séparément comme références historiques. |
| Prochain jalon conditionnel | Contrôle qualité non biologique des valeurs seulement après autorisation utilisateur distincte. |

## Décision de portée

L’import et l’inspection de schéma ont été autorisés exclusivement à des fins de conservation, de provenance et de structure technique. Toute lecture numérique des quantifications, même pour un contrôle qualité non biologique, exige une nouvelle autorisation explicite. Les données brutes restent hors de Git ; le dépôt privé ne contient que les scripts, décisions, métadonnées et reçus non sensibles.
