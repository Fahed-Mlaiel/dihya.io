# services/core

Ce dossier contient les services principaux pour la gestion avancée des fixtures Threed (JS & Python).

- `services_environnement.py` : Services Python pour l'environnement de fixtures
- `services_environnement.js` : Services JS pour l'environnement de fixtures
- `__init__.py` / `__init__.js` : Points d'entrée pour import direct
- `services_environnement.test.py` / `services_environnement.test.js` : Tests unitaires
- `__init__.test.py` / `__init__.test.js` : Tests d'import et de structure

## Exemples d'utilisation

### Python
```python
from .services_environnement import ...
```

### JavaScript
```js
const services = require('./services_environnement');
```

## Conformité
- Respecte la logique métier 3D avancée
- Compatible avec les outils de test et d'intégration continue
- Prêt pour l'audit et la documentation automatique
