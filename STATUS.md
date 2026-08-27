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
| Données patient individuelles | Interdites dans le dépôt. |
| Données contrôlées | Non téléchargées et non versionnées. |
| Normalisation, filtrage, matrices ou modules transcriptomiques | Non effectués ; les six modules restent inactifs. |
| Modèles de simulation | Aucun modèle importé ou exécuté. |
| Hypothèses de combinaison | Aucune active. |
| Code de l’archive `tlog28` | Lu statiquement seulement ; non copié dans ce dépôt. |
| v3 et module F1′/F2″ | Conservés séparément comme références historiques. |
| Prochain jalon conditionnel | Pré-spécifier, puis faire autoriser, une préparation de matrice technique non biologique. |

## Décision de portée

Les contrôles exécutés établissent seulement la provenance, l’intégrité, le schéma et la validité numérique élémentaire des fichiers. Ils ne démontrent pas une qualité biologique, une comparabilité d’échantillons, ni un résultat scientifique. Toute préparation de matrice ou lecture statistique ultérieure nécessite une autorisation explicite distincte. Les données brutes restent hors de Git ; le dépôt privé ne contient que les scripts, décisions, métadonnées et reçus non sensibles.
