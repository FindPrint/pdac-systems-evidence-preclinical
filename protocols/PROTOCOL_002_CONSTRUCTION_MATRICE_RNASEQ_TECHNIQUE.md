# PROTOCOL_002 — Construction technique d’une matrice RNA-seq GDC

## Statut et objet

**Statut :** pré-spécifié ; non exécuté.
**Objet :** définir à l’avance la seule construction technique d’une matrice de comptes bruts pour les 55 fichiers ouverts `STAR - Counts` du projet GDC `ORGANOID-PANCREATIC`.

Ce protocole ne construit aucun fichier et ne produit aucune analyse biologique. Il s’appuie sur les reçus de provenance, d’import, de schéma et de contrôle qualité déjà publiés. Toute exécution ultérieure exigera une autorisation utilisateur séparée.

## Entrées immuables et préconditions

| Élément | Exigence |
| --- | --- |
| Source | Les 55 TSV de `data/raw/GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_20260826/` uniquement. |
| Manifestes | `GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_MANIFEST.tsv`, SHA-256 `f713edebf0f8afb20305b1472d480564e45ac31ce79e28350d7dde6ae496220b`. |
| Provenance et import | Les reçus GDC doivent attester 55/55 MD5 et tailles conformes. |
| Schéma | Même préambule GENCODE v36, même en-tête de 9 colonnes et même ordre de `gene_id` pour les 55 fichiers. |
| Contrôle numérique | 55/55 fichiers au statut technique `pass`. |
| Destination autorisée | `data/processed/`, exclu de Git. |

L’exécution doit s’arrêter si une de ces préconditions n’est pas satisfaite. Aucun fichier partiellement produit ne doit être accepté comme résultat.

## Choix technique gelé

La colonne d’entrée est **`unstranded`**, et seulement `unstranded`. La documentation GDC indique que les lectures RNA-seq sont traitées comme non orientées pour favoriser l’harmonisation, et que les sorties STAR Counts comprennent des comptes par gène ainsi que des transformations FPKM, FPKM-UQ et TPM. [1]

Le choix de `unstranded` prépare donc une matrice de **comptes bruts par gène**. Les colonnes `tpm_unstranded`, `fpkm_unstranded` et `fpkm_uq_unstranded` ne seront ni mélangées à cette matrice ni choisies a posteriori. Elles resteront dans les fichiers bruts originaux. Toute transformation ou normalisation future nécessitera un protocole, une autorisation et une validation distincts.

| Dimension | Convention pré-spécifiée |
| --- | --- |
| Lignes | `gene_id` tel qu’écrit par GDC, sans suppression de suffixe, renommage ou conversion d’identifiant. |
| Colonnes | Les 55 `file_id` GDC du manifeste, un fichier par colonne ; aucune agrégation par cas. |
| Valeur de cellule | La valeur textuelle `unstranded`, recopiée telle quelle. |
| Identifiant de jointure | `gene_id` exact et son ordre publié ; `file_id` exact pour les colonnes. |
| Lignes exclues | Seulement `N_unmapped`, `N_multimapping`, `N_noFeature`, `N_ambiguous`. |
| Motif d’exclusion | Lignes techniques de synthèse, contrôlées séparément au jalon QC ; pas des gènes. |
| Dimensions attendues | 60 660 lignes de gènes × 55 colonnes, après retrait des quatre lignes techniques de chacun des fichiers. |
| Format prévu | TSV compressé par gzip, avec `gene_id` en première colonne, encodage UTF-8 et fin de ligne LF. |

Les 55 fichiers représentent 49 cas distincts dans le manifeste. La matrice reste donc une matrice de **fichiers de quantification** et non une matrice de cas ; cette décision évite une agrégation ou un choix d’appariement non pré-spécifié.

## Contrôles obligatoires lors d’une future exécution

La future exécution devra seulement extraire les valeurs de la colonne `unstranded` après le gel des conventions ci-dessus, puis contrôler les propriétés suivantes.

| Contrôle | Critère de passage | Sortie autorisée |
| --- | --- | --- |
| Ensemble d’entrée | Les 55 noms locaux égalent les 55 noms du manifeste. | Statut booléen et compte. |
| Intégrité | Chaque MD5 local correspond au manifeste. | Statut booléen et compte. |
| Préambule et en-tête | Identiques au schéma gelé. | Statut booléen. |
| Lignes techniques | Les quatre identifiants exclus sont présents exactement une fois par fichier. | Compte et statut. |
| Ordre des gènes | Vecteur de `gene_id` hors lignes techniques identique dans les 55 fichiers. | SHA-256 par vecteur et statut. |
| Dimensions | Exactement 60 660 × 55. | Dimensions et statut. |
| Cellules de compte | Uniquement les valeurs déjà validées comme entiers non négatifs. | Compte d’écarts, sans résumé d’expression. |
| Répertoire de sortie | N’est pas suivi par Git. | Statut booléen. |
| Reproductibilité | SHA-256 de la matrice et de la table de correspondance. | Empreintes. |

Un écart arrête la construction, produit un reçu de tentative partielle sans valeur d’expression, et interdit toute analyse ultérieure jusqu’à résolution documentée.

## Objets prévus mais non produits

Une exécution autorisée pourrait écrire localement les objets suivants, tous exclus de Git : une matrice `gene_id × file_id` de comptes `unstranded`, une table minimale de correspondance `file_id → file_name → case_id` issue du manifeste, et un reçu d’intégrité. Aucune de ces sorties n’existe au statut de ce protocole.

## Interdictions

Cette pré-spécification, et toute construction technique qui l’appliquerait, interdisent les opérations suivantes : normalisation, filtrage de gènes, retrait de zéros, sélection de gènes variables, correction de batch, statistiques descriptives d’expression, test différentiel, clustering, projection, apprentissage des six modules `TX_MODULE_01`–`TX_MODULE_06`, annotation de voies, comparaison normal/cancer, pseudo-temps, CSD, simulation, sélection de cibles ou de médicaments, et toute conclusion clinique ou thérapeutique.

## Référence

[1] [GDC — mRNA Analysis Pipeline](https://docs.gdc.cancer.gov/Data/Bioinformatics_Pipelines/Expression_mRNA_Pipeline/)
