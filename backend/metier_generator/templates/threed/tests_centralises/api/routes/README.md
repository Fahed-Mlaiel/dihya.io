# Routes API threed

Ce module définit les routes REST pour le métier threed, en Node.js et Python. Utilisez ces routes pour exposer les opérations CRUD et l’intégration métier.

## Fonctionnalités clés
- Définition des endpoints RESTful (GET, POST, PUT, DELETE)
- Sécurité et validation des routes
- Documentation automatique (Swagger/OpenAPI)
- Gestion des versions d’API

## Exemples d’utilisation

### Python
```python
from . import test_routes
# Utilisez les fonctions de test pour valider vos routes métier
```

### Node.js
```js
const routes = require('./routes');
// Utilisez les fonctions de test pour valider vos routes métier
```

## Tests inclus
- test_routes.py : tests unitaires avancés pour chaque endpoint Python
- test_routes.js : tests Jest pour la logique Node.js

## Bonnes pratiques
- Ajoutez vos propres routes métier dans ce dossier
- Couvrez chaque cas d’usage métier par un test dédié
