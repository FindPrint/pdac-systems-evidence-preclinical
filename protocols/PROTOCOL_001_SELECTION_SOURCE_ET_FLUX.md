# PROTOCOL_001 — Sélection de la première source et des premiers flux

## But

Sélectionner un premier jeu de données préclinique PDAC et un contrat de flux sans privilégier un médicament, un gène, une voie ou une combinaison. Cette sélection ne déclenche ni téléchargement de données, ni analyse de réponse, ni choix d’intervention.

## Critères d’éligibilité de la source

| Critère | Exigence | Statut si absent |
| --- | --- | --- |
| Objet mesuré | Mesure expérimentale clairement décrite : expression, viabilité, dose-réponse, imagerie ou temps réel. | Non admissible. |
| Entité biologique | Modèle déclaré : lignée, organoïde, tissu, contrôle normal ou autre système. | Non admissible. |
| Provenance | DOI/URL officiel, version, licence ou politique d’accès. | À compléter. |
| Données ouvertes | Fichiers nécessaires au jalon accessibles sans données identifiantes ni accès contrôlé. | À compléter ou exclu. |
| Unités et schéma | Variables, unités, transformations et valeurs manquantes documentées. | À compléter. |
| Réplication | Au moins une stratégie d’exclusion possible : modèle, lot, étude ou combinaison. | Exploratoire uniquement. |
| Contrôles | Contrôles tumoraux/non tumoraux ou leur absence explicitement déclarée. | Limite obligatoire. |
| Risque de fuite | Aucun endpoint futur transformé en flux, pseudo-temps ou contrôle. | Non admissible. |

## Critères de conception des flux initiaux

Les flux initiaux doivent correspondre à des familles de mesure distinctes. Un score ne peut pas être présenté comme une nouvelle mesure indépendante de celle qui le compose.

| Famille | Exemple de type de flux autorisé | Rôle initial | Exclusion explicite |
| --- | --- | --- | --- |
| Mesure omique | Valeur d’expression ou module appris sur ensemble d’entraînement. | Caractériser un état de modèle. | Signature choisie après inspection du résultat. |
| Réponse expérimentale | Viabilité, AUC, CSS ou dose-réponse documentée. | Endpoint de benchmark. | Recommandation thérapeutique. |
| Interaction | Bliss, HSA, Loewe ou ZIP, avec définition nommée. | Vérifier une interaction mesurée. | Preuve de sécurité ou de causalité. |
| Tissu/contrôle | Échantillon non tumoral, contrôle de culture ou mesure de dommage. | Évaluer la sélectivité préclinique. | Garantie d’innocuité humaine. |
| Qualité | Lot, passage, temps de culture, plateforme, profondeur. | Stratifier et diagnostiquer. | Flux thérapeutique. |
| Temps réel | Jour, cycle, passage ou exposition effectivement mesurés. | Analyse dynamique éventuelle. | Rang de survie ou label clinique futur. |

## Règle de minimalisme

Le premier contrat ne contient que les flux nécessaires pour vérifier que la source est correctement décrite. Une famille supplémentaire exige une fiche de variable, une provenance, un rôle analytique et une analyse de redondance.

## Décision à venir

La première décision doit comparer des sources candidates selon ce protocole, puis retenir un rôle de départ clair : soit une **source de caractérisation PDAC** sans conclusion thérapeutique, soit un **benchmark de réponse de combinaisons** sans prétention PDAC générale. Les deux rôles ne doivent pas être fusionnés sans appariement expérimental documenté.
