# Inventaire de conservation et de suppression proposée

> Aucun fichier, dépôt Git ou asset de release n’a été supprimé dans cette étape. Ce document distingue la conservation locale vérifiée, les sauvegardes distantes historiques et les candidats à une suppression qui nécessitent une confirmation de périmètre.

## Conservation locale vérifiée

| Élément | Chemin | Vérification |
| --- | --- | --- |
| Pipeline v3 original | `/home/ubuntu/conservation_v3_f1f2/pipeline_autonomev3_propre.py` | Copie de `/home/ubuntu/upload/pipeline_autonomev3_propre.py`, empreinte enregistrée dans `VERIFICATION_CONSERVATION_SHA256.txt`. |
| Archive module dérivatif CSD F1′/F2″ | `/home/ubuntu/conservation_v3_f1f2/livraison_module_derivatif_csd_apamea.tar.gz` | SHA-256 externe : `ae7059af95889e2ec067ab6ae41b5117adf697829331db0ffe7c39210442eaa`. |
| Module F1′/F2″ extrait | `/home/ubuntu/conservation_v3_f1f2/livraison_module_derivatif_csd_apamea/` | Tous les fichiers déclarés par le `SHA256SUMS.txt` interne sont vérifiés `OK`. |
| Preuve de vérification | `/home/ubuntu/conservation_v3_f1f2/VERIFICATION_CONSERVATION_SHA256.txt` | Conserve les empreintes v3, archive et contrôles internes. |

## Sauvegardes distantes historiques à préserver

Le dépôt privé Apamea et ses releases contiennent les résultats précédemment publiés, dont le module F1′/F2″, les validations et les archives. Ces éléments ne seront pas modifiés ni supprimés par défaut, car ils constituent une sauvegarde scientifique versionnée déjà vérifiée.

La release privée `v2026.08.26` contient notamment :

- `livraison_module_derivatif_csd_apamea.tar.gz` ;
- `livraison_v3_enrichi_localvar_f1f2.tar.gz` ;
- `livraison_ablations_unitaires_f1f2_localvar.tar.gz` ;
- des archives de contrôle, d’ablation, de validation thermique et de topologie.

## Candidats de suppression locale — en attente d’accord

| Groupe | Exemples de chemins | Risque si supprimé | Recommandation |
| --- | --- | --- | --- |
| Examen statique de `tlog28` | `/home/ubuntu/review_tlog28/`, `/home/ubuntu/upload/tlog28.zip` | Perte du paquet reçu et de l’audit statique local ; aucune perte distante connue. | Supprimable après votre confirmation. |
| Documents de faisabilité oncologique précédents | fichiers `CADRE_SECURITE_*`, `PROTOCOLE_PILOTE_*`, `REVUE_STATIQUE_*`, `PROPOSITION_*` à la racine. | Perte des notes locales ; le dépôt pancréatique contient une partie des documents. | Supprimable seulement si vous voulez un redémarrage local strict. |
| Projet exploratoire pancréatique initial | `/home/ubuntu/pancreatic-cancer-open-data-reproducibility/` et son dépôt GitHub privé associé. | Perte locale et/ou distante d’un cadre de sécurité, de sources et de protocole déjà versionnés. | **Ne pas supprimer sans instruction explicite sur le dépôt privé.** |
| Résultats locaux Apamea | dossiers d’audits, consolidations, archives et scripts à `/home/ubuntu/`. | Perte d’artefacts locaux ; les principales étapes sont archivées dans releases privées. | Garder jusqu’à une liste explicite de dossiers à purger. |
| Dépôt privé Apamea | `FindPrint/apamea-artificial-spin-ice-multiflux` et releases. | Perte d’historique scientifique publié, de manifestes et de sauvegardes. | Conserver par défaut. |

## Décision à confirmer

Avant toute suppression, il faut préciser laquelle de ces trois portées vous voulez :

1. **Nettoyage d’examen seulement** : supprimer `tlog28.zip` et `review_tlog28`, en gardant Apamea, les dépôts privés et les documents récents ;
2. **Redémarrage local strict** : conserver seulement `conservation_v3_f1f2/` localement et supprimer les autres artefacts locaux identifiés, sans supprimer aucun dépôt/release GitHub privé ;
3. **Purge étendue** : vous fournissez une liste explicite de dépôts GitHub privés et de dossiers locaux à supprimer. Cette option nécessite une confirmation séparée, car elle est irréversible pour les données locales et peut détruire l’historique distant.
