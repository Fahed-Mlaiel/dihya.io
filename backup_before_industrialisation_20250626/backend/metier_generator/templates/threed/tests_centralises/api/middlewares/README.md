# Middlewares API threed

Ce module regroupe les middlewares avancés pour la couche API threed (logger, sécurité, validation, etc.).

## Fonctionnalités clés
- Logging structuré (JSON, rotation, audit)
- Sécurité (authentification, autorisation, CORS)
- Validation des requêtes et réponses
- Gestion centralisée des erreurs

## Exemples d’utilisation

### Python
```python
from . import test_api_middlewares
# Utilisez les fonctions de test pour valider vos middlewares métier
```

### Node.js
```js
const middlewares = require('./middlewares');
// Utilisez les fonctions de test pour valider vos middlewares métier
```

## Tests inclus
- test_api_middlewares.py : tests unitaires avancés pour chaque middleware Python
- test_api_middlewares.js : tests Jest pour la logique Node.js

## Bonnes pratiques
- Ajoutez vos propres middlewares métier dans ce dossier
- Couvrez chaque cas d’usage critique par un test dédié
