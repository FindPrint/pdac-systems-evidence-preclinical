# Statut du projet

| Élément | État au 26 août 2026 |
| --- | --- |
| Périmètre | Recherche préclinique PDAC, non clinique. |
| Source importée | Sous-ensemble ouvert `ORGANOID-PANCREATIC` de quantifications RNA-seq GDC. |
| Quantifications locales | 55 TSV, uniquement dans `data/raw/` exclu de Git. |
| Intégrité | 55/55 tailles et MD5 GDC vérifiés indépendamment ; aucun fichier partiel ni non déclaré. |
| Données patient individuelles | Interdites dans le dépôt. |
| Données contrôlées | Non téléchargées et non versionnées. |
| Analyse de contenu RNA-seq | Non effectuée. |
| Normalisation, filtrage, modules transcriptomiques | Non effectués ; les six modules restent inactifs. |
| Modèles de simulation | Aucun modèle importé ou exécuté. |
| Hypothèses de combinaison | Aucune active. |
| Code de l’archive `tlog28` | Lu statiquement seulement ; non copié dans ce dépôt. |
| v3 et module F1′/F2″ | Conservés séparément comme références historiques. |
| Prochain jalon conditionnel | Inspection du schéma des TSV seulement après autorisation utilisateur distincte. |

## Décision de portée

L’import a été autorisé exclusivement à des fins de conservation locale et de contrôle d’intégrité. Le dépôt ne doit accueillir une analyse qu’après validation explicite de l’étape suivante, conformément aux règles de non-fuite définies dans `protocols/PROTOCOL_000_REGISTRE_EVIDENCE_PRECLINIQUE.md`. Les données brutes restent hors de Git ; le dépôt privé ne contient que les scripts, décisions, métadonnées et reçus non sensibles.
