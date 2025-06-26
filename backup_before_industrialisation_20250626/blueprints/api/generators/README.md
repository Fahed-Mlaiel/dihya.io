# API Generators Blueprints

Blueprints ultra avancés pour la génération automatique de code API (routes, contrôleurs, documentation) en JS et Python.

## Fonctionnalités incluses
- Génération de routes et contrôleurs à partir de modèles YAML/JSON
- Génération de documentation OpenAPI
- Exemples d'intégration Node.js et Python

## Exemples d'intégration

### Node.js
```js
const { backendApi } = require('../backendApi');
const app = backendApi({ metier: 'Inventaire', dependances: {}, pluginsConfig: {}, rgpdEnabled: true });
```

### Python
```python
from ..backendApi import createBackendApi
app = createBackendApi(metier="Inventaire", models=..., services=...)
```

## Bonnes pratiques
- Utilisez les générateurs pour accélérer la création de nouvelles APIs
- Gardez vos modèles à jour pour une documentation fiable
