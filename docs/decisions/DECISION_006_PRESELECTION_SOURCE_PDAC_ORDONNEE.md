# Décision 006 — Présélection limitée d’une source PDAC ordonnée

**Date :** 27 août 2026

**Statut :** présélection pour inventaire de manifestes uniquement ; téléchargement et analyse non autorisés par cette décision.

## Décision

`OrganoIDNetData` (Zenodo DOI `10.5281/zenodo.10643410`) est présélectionné comme candidat à un inventaire de métadonnées et de structure d’archive. La présélection repose sur un ordre expérimental documenté : acquisition d’images d’organoïdes PDAC toutes les quatre heures jusqu’à 100 heures. [1] [2]

Cette décision ne présélectionne pas une cible, un médicament, un groupe de traitement, une conclusion biologique ou une intervention. Elle ne sélectionne pas non plus une trajectoire utilisable : cette question reste ouverte jusqu’à vérification du manifeste de l’archive.

## Raisons de la présélection

| Critère | État |
| --- | --- |
| PDAC préclinique | Oui : organoïdes PDAC humains et murins. |
| Axe réel mesuré | Oui : heures d’acquisition documentées. |
| Données ouvertes | Oui : enregistrement Zenodo ouvert sous CC BY 4.0. |
| Métadonnées visibles sans téléchargement | Partiellement : structure et noms accessibles par aperçu web. |
| Trajectoire par système vérifiée | Non encore. |
| Longueur compatible v3 inchangé | Non démontrée ; la cadence publiée suggère environ 26 positions au plus sur 100 h. |
| Flux prêts pour v3 | Non : ils devront être définis depuis images et masques réels, après autorisation. |

## Conditions d’un futur inventaire metadata-only

Le prochain jalon éventuel peut seulement interroger l’API publique Zenodo pour obtenir les métadonnées de l’enregistrement : version, licence, nom de l’archive, taille, MD5 et liens de prévisualisation. Il peut aussi consigner la structure de l’aperçu public sans télécharger l’archive ZIP de 4,6 GB.

Il doit s’arrêter si les métadonnées ne permettent pas de distinguer données brutes, masques, augmentations et sorties de modèles, ou si elles ne permettent pas de relier de manière traçable un champ de vue à un instant et à un système. Le résultat possible est « indéterminé / données de structure insuffisantes ».

## Interdictions maintenues

Ne pas télécharger l’archive, ne pas extraire les images, ne pas lancer les scripts tiers, ne pas analyser les pixels, ne pas créer de flux, ne pas exécuter v3, ne pas adapter F1′/F2″, ne pas choisir de contrôle, de seuil, de traitement ou de combinaison.

## Références

[1] [OrganoIDNetData — Zenodo](https://zenodo.org/records/10643410)

[2] [Kulkarni et al., Scientific Data, 2024](https://www.nature.com/articles/s41597-024-03631-3)
