# Statut du projet

| Élément | État au 26 août 2026 |
| --- | --- |
| Périmètre | Recherche préclinique PDAC, non clinique. |
| Source importée | Sous-ensemble ouvert `ORGANOID-PANCREATIC` de quantifications RNA-seq GDC. |
| Quantifications locales | 55 TSV, uniquement dans `data/raw/` exclu de Git. |
| Intégrité de transfert | 55/55 tailles et MD5 GDC vérifiés indépendamment ; aucun fichier partiel ni non déclaré. |
| Schéma technique | Vérifié sur 55/55 : préambule GENCODE v36, 9 colonnes, 60 664 lignes de données et même séquence de `gene_id`. |
| Contrôle qualité numérique | Conforme sur 55/55 : aucun `gene_id` manquant ou dupliqué ; aucun champ de gène manquant ; aucune anomalie de syntaxe, finitude, signe ou intégralité sur les colonnes contrôlées. |
| Lignes techniques de synthèse | 4 par fichier, soit 220 au total ; contrôlées séparément, non assimilées à des gènes. |
| Matrice technique locale | Construite : 60 660 `gene_id` × 55 `file_id`, à partir de `unstranded` seulement ; sorties exclues de Git. |
| Vérification de matrice | Dimensions, ordre des `gene_id`, correspondance fichier/colonne et SHA-256 vérifiés. |
| Variables et modules transcriptomiques | Aucune variable active ; les six modules restent inactifs. |
| Données patient individuelles | Interdites dans le dépôt. |
| Données contrôlées | Non téléchargées et non versionnées. |
| Normalisation, filtrage, statistiques ou comparaison biologique | Non effectués. |
| Modèles de simulation | Aucun modèle importé ou exécuté. |
| Hypothèses de combinaison | Aucune active. |
| Code de l’archive `tlog28` | Lu statiquement seulement ; non copié dans ce dépôt. |
| v3 et module F1′/F2″ | Conservés séparément comme références historiques. |
| Prochain jalon conditionnel | Pré-spécifier une préparation analytique de qualité, puis demander une autorisation distincte avant toute exécution. |

## Décision de portée

La matrice locale est un objet technique reproductible de comptes `unstranded`, non une conclusion scientifique. Son existence n’autorise pas l’analyse statistique, la normalisation, l’annotation biologique, la sélection de gènes ou l’activation des modules. Les données brutes et les fichiers de matrice restent hors de Git ; le dépôt privé conserve uniquement les scripts, décisions, métadonnées et reçus non sensibles.
