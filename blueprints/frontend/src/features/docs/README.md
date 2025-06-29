# Feature : Documentation (docs)

Ce dossier gère la documentation utilisateur et développeur intégrée (pages docs, guides, openapi, etc.).

## Composants
- DocPage.jsx : page de documentation
- OpenAPIViewer.jsx : visualisation interactive d’API
- GuideIntegration.jsx : page guide d’intégration

## Cas d’usage
- Affichage de guides, FAQ, docs API, schémas
- Intégration OpenAPI (openapi.yaml)
- Affichage de la documentation utilisateur
- Visualisation interactive de l’OpenAPI
- Guides d’intégration avancés

## Flux utilisateur
1. L’utilisateur accède à la page docs
2. Parcourt guides, API, schémas

## Exemples d’intégration
```jsx
import DocPage from './DocPage';
<DocPage section="onboarding" />
```

## Schéma d’architecture
[DocPage] → [GuideIntegration] → [OpenAPIViewer]

## À faire
- Ajouter des exemples de guides, schémas, intégration live
- Ajouter des hooks/services pour la navigation dans la doc
