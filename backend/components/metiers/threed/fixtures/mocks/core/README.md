# mocks/core

Ce dossier contient les mocks principaux pour le module Threed (JS & Python).

## Structure
- `fixtures_mock.py` : Mocks Python (fonctions/classes de simulation pour les tests 3D)
- `fixtures.mock.js` : Mocks JS (fonctions/classes de simulation pour les tests 3D)
- `__init__.py` / `__init__.js` : Points d'entrée pour import direct
- `__init__.test.py` / `__init__.test.js` : Tests d'import et de structure
- `fixtures_mock.test.py` / `fixtures.mock.test.js` : Tests unitaires pour les mocks principaux

## Exemples d'utilisation

### Python
```python
from .fixtures_mock import ...
```

### JavaScript
```js
const mock = require('./fixtures.mock');
```

## Conformité
- Respecte la logique métier 3D avancée
- Compatible avec les outils de test et d'intégration continue
- Prêt pour l'audit et la documentation automatique
