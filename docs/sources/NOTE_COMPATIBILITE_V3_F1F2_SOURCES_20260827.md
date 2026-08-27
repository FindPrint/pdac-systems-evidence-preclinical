# Note de compatibilité — pipeline v3 et module F1′/F2″

## Objet

Cette note résume la lecture statique de la copie conservée de `pipeline_autonomev3_propre.py` et du module dérivatif `analyser_derivatives_csd_post_pre.py`. Elle ne modifie ni n’exécute ces fichiers.

## Préconditions v3 observées

| Composant | Précondition observée | Conséquence pour la recherche de sources |
| --- | --- | --- |
| Entrée v3 | CSV avec une colonne de contrôle numérique et une ou plusieurs colonnes de flux numériques. | Une matrice gène × échantillon doit être transformée, sous protocole distinct, en observations ordonnées × flux. |
| Ordre utilisé | Le contrôle est converti en rang de progression par `rankdata`. | Le contrôle doit être une mesure à ordre réel ; un rang administratif reste exclu. |
| Garde-fou de longueur | `run_pipeline` exige au minimum 50 points en mode `fast`, 80 en mode `stable` et 100 en mode `robust`, selon la configuration par défaut. | Une série à 7 instants ne peut pas alimenter v3 inchangé comme unité temporelle individuelle. |
| Fenêtre par défaut | 80 (`fast`), 150 (`robust`) ou 80 (`stable`). | Les très petites séries ne doivent pas recevoir de réglage réduit a posteriori pour forcer une sortie. |
| Flux | Sans mapping explicite, v3 sélectionne jusqu’à 50 colonnes numériques disponibles. | La définition des flux doit être gelée avant une future exécution. |
| Seuil | Le code effectue un scan de seuil, avec optimisation Monte Carlo configurable. | Toute sortie resterait exploratoire et devrait être validée hors échantillon. |

La copie v3 rappelle elle-même que son seuil optimisé reste exploratoire sans données temporellement indépendantes ou bootstrap par blocs.

## Préconditions du module F1′/F2″ observées

Le module dérivatif séparé est spécifique aux dix exécutions historiques Apamea : chemins locaux, contrôles `M`, `E`, `Flip`, `Cluster`, `LocalVar` et structure de sorties sont codés en dur. Il lit les seuils publiés par ces exécutions puis calcule des résumés de dérivées et corrélations descriptives. Il n’est donc **pas réutilisable directement** sur un nouveau jeu PDAC sans refactorisation explicitement versionnée, qui nécessiterait un protocole distinct et une autorisation préalable.

## Conséquence pour GSE262627

GSE262627 est une vraie série temporelle préclinique ouverte : six organoïdes PDAC et quatre lignées cellulaires ont été échantillonnés à sept temps (0 à 24 h, toutes les 4 h). [1] [2] Cela satisfait l’exigence d’axe mesuré mais pas la longueur minimale v3 par système (`7 < 50`). La mise en commun de systèmes différents augmenterait artificiellement le nombre de lignes, mais ne créerait pas une série unique répétée et ne sera pas utilisée pour contourner le garde-fou.

Ce candidat reste utile comme **référence de design longitudinal authentique** et pourrait éventuellement alimenter une adaptation future explicitement distincte de v3. Il n’est pas présélectionné pour une exécution inchangée de v3.

## Références

[1] [GEO GSE262627](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE262627)

[2] [Sharma et al., JCI Insight, 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11141942/)
