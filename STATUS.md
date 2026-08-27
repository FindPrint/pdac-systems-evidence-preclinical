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
| Pré-spécification de matrice | Publiée ; une matrice `unstranded` de 60 660 gènes × 55 fichiers est seulement définie, pas construite. |
| Matrices traitées locales | Aucune. |
| Variables et modules transcriptomiques | Aucune variable active ; les six modules restent inactifs. |
| Données patient individuelles | Interdites dans le dépôt. |
| Données contrôlées | Non téléchargées et non versionnées. |
| Normalisation, filtrage, statistiques ou comparaison biologique | Non effectués. |
| Modèles de simulation | Aucun modèle importé ou exécuté. |
| Hypothèses de combinaison | Aucune active. |
| Code de l’archive `tlog28` | Lu statiquement seulement ; non copié dans ce dépôt. |
| v3 et module F1′/F2″ | Conservés séparément comme références historiques. |
| Prochain jalon conditionnel | Construction technique de la matrice seulement après autorisation utilisateur explicite. |

## Décision de portée

Le protocole `PROTOCOL_002_CONSTRUCTION_MATRICE_RNASEQ_TECHNIQUE.md` gèle une convention technique, sans produire de fichier de matrice. Toute exécution exigera une autorisation distincte ; elle devra s’arrêter au premier écart de provenance, d’intégrité ou d’ordre de gènes. Les données brutes et toute matrice future restent hors de Git. Aucune couche biologique, mécanistique, pharmacologique ou clinique n’est activée par ce jalon.
