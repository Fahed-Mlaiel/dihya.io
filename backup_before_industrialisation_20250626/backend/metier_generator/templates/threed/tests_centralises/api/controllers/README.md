# Contrôleurs API threed

Ce module centralise la logique métier des contrôleurs pour l’API threed, en Node.js et Python.

## Fonctionnalités clés
- Gestion avancée des assets (CRUD, validation, transformation)
- Sécurité et contrôle d’accès par rôle
- Orchestration des appels métiers (asynchrone, transactionnel)
- Gestion des erreurs et des logs (audit, monitoring)

## Exemples d’utilisation

### Python
```python
from . import test_controllers
# Utilisez les fonctions de test pour valider vos contrôleurs métier
```

### Node.js
```js
const controllers = require('./controllers');
// Utilisez les fonctions de test pour valider vos contrôleurs métier
```

## Tests inclus
- test_controllers.py : tests unitaires avancés pour chaque endpoint métier
- test_controllers.js : tests Jest pour la logique Node.js

## Bonnes pratiques
- Ajoutez vos propres contrôleurs métier dans ce dossier
- Couvrez chaque cas d’usage métier par un test dédié
