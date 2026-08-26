# Reçu de schéma — ORGANOID-PANCREATIC, quantifications RNA-seq ouvertes

## Conclusion structurale

L’inspection descriptive autorisée est **conforme et homogène** sur les 55 TSV RNA-seq importés. Elle a porté sur le préambule, l’en-tête, la largeur tabulaire, le nombre de lignes de données, la présence de l’identifiant primaire et les empreintes de séquence d’identifiants. Aucune valeur de quantification n’a été stockée, convertie, résumée ou comparée.

| Propriété contrôlée | Résultat |
| --- | --- |
| Fichiers inspectés | 55 sur 55 |
| Préambule par fichier | Une ligne : `# gene-model: GENCODE v36` |
| En-tête distinct | 1 sur 55 |
| Colonnes | 9 sur 55 |
| Lignes de données | 60 664 sur 55 |
| Identifiant primaire | `gene_id` sur 55 fichiers |
| Empreinte de séquence d’identifiants | Une seule empreinte sur 55 fichiers |
| Largeur tabulaire interne | Conforme dans tous les fichiers |
| Écart manifeste/local | Aucun |

L’en-tête partagé est :

```text
gene_id, gene_name, gene_type, unstranded, stranded_first, stranded_second,
tpm_unstranded, fpkm_unstranded, fpkm_uq_unstranded
```

## Correspondance documentaire

Le schéma constaté correspond à la description du workflow GDC `STAR - Counts` : comptes par gène issus de STAR, augmentés de transformations FPKM, FPKM-UQ et TPM, avec annotation par symbole et biotype, fournis sous forme tabulée. La documentation GDC précise aussi l’usage de GENCODE v36 pour cette annotation. [1]

> Cette correspondance est une vérification de structure et de libellés. Elle ne valide pas les valeurs de comptage, les conventions de calcul au niveau de chaque ligne, ni l’adéquation d’une colonne à une question biologique donnée.

## Limites maintenues

Les résultats suivants n’ont **pas** été produits : statistiques descriptives de valeur, contrôles de valeurs manquantes ou négatives, filtrage, normalisation, contrôle de batch, analyses différentielle ou de variance, clustering, attribution normal/cancer, modules transcriptomiques, mécanismes ou hypothèses thérapeutiques.

L’identité de l’ordre des `gene_id` est établie par une empreinte SHA-256 identique. Cette propriété facilite une future construction de matrice reproductible, mais ne remplace pas un contrôle de l’unicité des gènes, de la validité numérique ou de la comparabilité biologique.

Le reçu machine détaillé, sans valeurs de quantification, est conservé dans `data/external-links/GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_SCHEMA_RECEIPT.json`. Les TSV bruts restent locaux et exclus de Git.

## Références

[1] [GDC — mRNA Analysis Pipeline](https://docs.gdc.cancer.gov/Data/Bioinformatics_Pipelines/Expression_mRNA_Pipeline/)
