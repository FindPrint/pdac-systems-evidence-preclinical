# Décision 002 — Import contrôlé des quantifications GDC ouvertes

**Date :** 26 août 2026

**État :** Autorisé par l’utilisateur ; transfert en cours au moment de cette décision.

**Portée :** `ORGANOID-PANCREATIC`, quantifications RNA-seq ouvertes inventoriées dans le manifeste publié.

## Décision

L’utilisateur a autorisé l’import des **55** fichiers de quantification RNA-seq ouverts recensés lors de l’inventaire de provenance. L’autorisation couvre le transfert vers `data/raw/GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_20260826/`, répertoire exclu du suivi Git, et la vérification d’intégrité fichier par fichier.

> Cette décision n’autorise ni l’analyse des valeurs de quantification, ni la normalisation, ni le filtrage de gènes, ni la construction de modules transcriptomiques, ni une comparaison biologique, ni la sélection d’une cible, d’un médicament ou d’une combinaison.

## Barrières d’exécution

| Contrôle | Exigence de passage |
| --- | --- |
| Manifestes autorisés | Exactement 55 lignes et identifiants UUID GDC distincts. |
| Périmètre | Chaque ligne doit être `open`, `Gene Expression Quantification`, `TSV`, `RNA-Seq`, `STAR - Counts`. |
| Endpoint | Exclusivement `https://api.gdc.cancer.gov/data/{file_id}` pour les identifiants du manifeste. |
| Écriture | Fichier temporaire puis renommage atomique seulement après vérification. |
| Intégrité | Taille déclarée et MD5 GDC doivent coïncider pour chaque fichier. |
| Traçabilité | Reçu local JSON, SHA-256 local par fichier et total de transfert. |
| Écart | Arrêt du processus ; reçu partiel ; aucune analyse ultérieure. |

## Limites inchangées

Les données brutes demeurent locales et ignorées par Git. Seuls le script, la décision, les métadonnées publiques déjà inventoriées et le reçu d’import non sensible seront publiés dans le dépôt privé. L’état du programme reste **préclinique et exploratoire** ; il n’apporte aucune indication clinique, aucun traitement et aucune promesse de sécurité ou d’efficacité.
