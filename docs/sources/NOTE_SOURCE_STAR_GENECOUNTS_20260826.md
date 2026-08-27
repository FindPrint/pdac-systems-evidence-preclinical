# Note de source — STAR GeneCounts et lignes techniques

Le 26 août 2026, la documentation STAR v2.7.8a a été consultée à l’URL ci-dessous afin de contextualiser les identifiants techniques `N_unmapped`, `N_multimapping`, `N_noFeature` et `N_ambiguous` observés uniformément lors du contrôle qualité.

La page de contenu du manuel repère la section « Counting number of reads per gene » à la page 18. L’afficheur PDF n’a toutefois pas exposé le texte de cette page de manière exploitable dans cette session. Cette note ne tire donc **aucune conclusion documentaire détaillée** à partir de l’afficheur seul.

L’interprétation opérationnelle retenue au prochain contrôle sera limitée au constat local : ces quatre identifiants sont présents, dans le même ordre, quatre fois par fichier ; ils ne sont pas des identifiants GENCODE ordinaires et portent des champs de transformation vides. Ils seront traités comme des lignes techniques séparées, avec conservation de leur contrôle de syntaxe des colonnes de compte, sans correction ni suppression.

## Référence

[STAR manual 2.7.8a — Alexander Dobin](https://gensoft.pasteur.fr/docs/STAR/2.7.8a/STARmanual.pdf)
