# Pagination API threed

Gestion de la pagination des résultats via middleware (Node.js & Python).

## Fonctionnalités clés
- Pagination offset/limit et cursor
- Support des filtres dynamiques
- Gestion des erreurs de pagination
- Intégration avec ORM/ODM (SQL, MongoDB, etc.)

## Tests disponibles
- `test_pagination.py` : Tests unitaires Python pour la pagination (logique métier réelle)
- `test_pagination.test.js` : Tests unitaires Node.js/Jest pour la pagination

## Exemples d’utilisation

### Python
```python
from . import test_pagination
# Utilisez les fonctions de test pour valider la pagination métier
```

### Node.js
```js
const pagination = require('./pagination');
// Utilisez les fonctions de test pour valider la pagination métier
```

## Bonnes pratiques
- Ajoutez des cas limites (empty, out of range, etc.)
- Testez la pagination sur de gros volumes de données
