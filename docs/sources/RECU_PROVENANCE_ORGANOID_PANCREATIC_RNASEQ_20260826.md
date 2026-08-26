# Reçu de provenance — ORGANOID-PANCREATIC, quantifications RNA-seq ouvertes

## Portée exacte

Ce reçu couvre seulement les **métadonnées** interrogées auprès de l’API GDC le 26 août 2026. Il ne contient aucune matrice RNA-seq, aucune valeur de gène, aucun téléchargement de quantification et aucune analyse biologique.

| Élément | Valeur figée |
| --- | --- |
| Projet GDC | `ORGANOID-PANCREATIC` |
| Requête | `access=open`, `data_type=Gene Expression Quantification`, `experimental_strategy=RNA-Seq` |
| API interrogée | `https://api.gdc.cancer.gov/files` |
| Fichiers retournés | 55 |
| Cas distincts dans le manifeste | 49 |
| Taille cumulée déclarée | 232 648 892 octets |
| Format | 55 TSV |
| Workflow | 55 `STAR - Counts` |
| Type d’échantillon retourné | 55 `Next Generation Cancer Model` |
| Empreintes MD5 distinctes | 55 |
| SHA-256 de la réponse API brute | `01b6300bc3f1f88942c22b3bb9338305b2f8b995355158cc69868bb6118696de` |
| SHA-256 du manifeste TSV | `211563929d12aa4d782de66ae39f766526b25ec9f9c061e70cdb0dd86bab4975` |

Le manifeste détaillé, avec `file_id`, nom, MD5, taille, cas, identifiant de soumission, workflow et horodatages GDC, est conservé sous `data/external-links/GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_MANIFEST.tsv`.

## Schéma documenté

Chaque fichier inventorié est un fichier `augmented_star_gene_counts.tsv` produit par le workflow `STAR - Counts`. La documentation GDC indique que les fichiers STAR Counts comprennent les comptes par gène et des transformations associées, dont FPKM, FPKM-UQ et TPM, accompagnées d’annotations de gène ; les fichiers sont tabulés. [1]

Aucune convention de normalisation ne sera choisie avant la prochaine phase. Le premier contrôle d’import devra confirmer, dans les fichiers réellement reçus, le schéma publié, l’identifiant de gène, les colonnes de compte et toute incompatibilité entre release et documentation.

## Accès et limites

La requête filtre explicitement `access=open`. La notice AWS distingue les quantifications d’expression RNA-seq ouvertes des lectures alignées, WGS/WXS, mutations et quantifications de jonctions, qui sont sous accès contrôlé. [2] Cette séparation est conservée : le programme n’essaiera pas d’accéder aux catégories contrôlées.

La notice AWS décrit une collection comprenant des organoïdes pancréatiques normaux et cancéreux. [2] Cependant, le manifeste ouvert interrogé retourne uniquement le type d’échantillon générique `Next Generation Cancer Model`. Il ne permet donc **pas**, à lui seul, d’étiqueter chaque fichier comme normal ou cancéreux, ni d’établir un appariement. Toute affirmation à ce sujet reste interdite jusqu’à obtention de métadonnées ouvertes, explicites et appariables.

## État de l’analyse

| Action | État |
| --- | --- |
| Inventaire des métadonnées | Terminé. |
| Manifestes et empreintes | Terminés. |
| Téléchargement des 55 TSV | Non effectué. |
| Vérification de contenu des TSV | Non effectuée. |
| Transformation, modules transcriptomiques ou flux | Non effectués. |
| Comparaison normal/cancer | Non effectuée. |
| Endpoint pharmacologique, toxicité ou combinaison | Absent. |

## Prochaine autorisation requise

Une autorisation distincte est nécessaire avant de télécharger les 55 quantifications ouvertes dans un répertoire `data/raw/` exclu de Git. L’import devra vérifier chaque MD5 officiel, générer un manifeste local, et s’arrêter au moindre écart. Il ne constituera toujours pas une analyse biologique.

## Références

[1] [GDC — mRNA Analysis Pipeline](https://docs.gdc.cancer.gov/Data/Bioinformatics_Pipelines/Expression_mRNA_Pipeline/)

[2] [AWS Open Data Registry — Pancreatic Cancer Organoid Profiling](https://registry.opendata.aws/organoid-pancreatic/)
