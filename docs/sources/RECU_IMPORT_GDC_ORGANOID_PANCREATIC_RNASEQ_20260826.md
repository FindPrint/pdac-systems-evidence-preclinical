# Reçu d’import — ORGANOID-PANCREATIC, quantifications RNA-seq ouvertes

## Résultat du transfert

L’import autorisé du sous-ensemble ouvert GDC `ORGANOID-PANCREATIC` est **terminé et intégralement vérifié**. Il a été exécuté depuis le manifeste de provenance publié, sans interpréter, transformer, normaliser ou agréger le contenu des fichiers TSV.

| Élément | Résultat |
| --- | --- |
| Début du transfert (UTC) | `2026-08-26T20:32:20.195726+00:00` |
| Fin du transfert (UTC) | `2026-08-26T20:53:23.994085+00:00` |
| Fichiers attendus | 55 |
| Fichiers téléchargés et vérifiés | 55 |
| Taille déclarée par GDC | 232 648 892 octets |
| Taille locale observée | 232 648 892 octets |
| MD5 GDC conformes | 55 sur 55 |
| SHA-256 local par fichier | Consigné dans le reçu JSON |
| Fichiers partiels | 0 |
| Fichiers locaux non déclarés | 0 |
| Résultat global | `complete` ; `all_md5_verified=true` |

Les TSV bruts sont confinés dans `data/raw/GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_20260826/`, chemin exclu du suivi Git. Le reçu détaillé non sensible est `data/external-links/GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_IMPORT_RECEIPT.json`. Il associe chaque identifiant GDC au MD5 attendu et observé, à la taille attendue et observée, ainsi qu’au SHA-256 local.

## Méthode de contrôle

L’importeur a refusé toute ligne ne respectant pas simultanément les contraintes suivantes : `access=open`, `data_type=Gene Expression Quantification`, `data_format=TSV`, `experimental_strategy=RNA-Seq`, et workflow `STAR - Counts`. Il a téléchargé chaque identifiant de fichier du manifeste via l’API GDC, écrit un fichier temporaire, puis vérifié taille et MD5 avant renommage atomique.

Une seconde vérification indépendante a reconstruit un fichier de contrôle MD5 à partir du manifeste publié. Elle a confirmé l’identité des 55 noms de fichiers locaux avec les 55 noms attendus, l’absence de fichier `.part`, et le succès de **55 contrôles MD5 sur 55**.

## Limites maintenues

> Ce reçu établit la provenance et l’intégrité des fichiers locaux. Il ne constitue ni un contrôle qualité biologique, ni une caractérisation de l’expression, ni une comparaison normal/cancer, ni une hypothèse mécanistique ou thérapeutique.

Aucun TSV n’a été ouvert pour inspection de schéma pendant cette étape. Aucun module transcriptomique n’est activé. Aucun gène, médicament, combinaison, seuil, pseudo-temps, modèle de simulation ou résultat préclinique n’a été produit.

La prochaine étape, si elle est autorisée séparément, se limitera à une **inspection descriptive du schéma** : en-tête, nombre de colonnes, identifiants de gènes, conventions de quantification, cohérence entre les 55 fichiers et documentation GDC. Elle n’inclura ni tests biologiques, ni différentiel d’expression, ni clustering ou attribution de phénotype.
