# Documentation API threed

Ce module documente toutes les routes, contrôleurs, schémas de données et intégrations pour l’API métier threed.

## Contenu
- Spécification OpenAPI/Swagger
- Exemples de payloads JSON
- Description des contrôleurs et middlewares
- Guide d’intégration (Python & Node.js)

## Exemples d’utilisation

### Python
```python
from . import test_api_docs
# Utilisez les fonctions de test pour valider la documentation métier
```

### Node.js
```js
const docs = require('./docs');
// Utilisez les fonctions de test pour valider la documentation métier
```

## Tests inclus
- test_api_docs.py : tests unitaires avancés pour la documentation Python
- test_api_docs.js : tests Jest pour la documentation Node.js

## Bonnes pratiques
- Tenez la documentation à jour à chaque évolution métier
- Ajoutez des exemples d’intégration réels
