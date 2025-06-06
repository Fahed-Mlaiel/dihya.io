# mocks

Ce dossier regroupe tous les mocks ultra avancés pour le module Threed (JS & Python).

## Structure
- `core/` : mocks principaux (fixtures_mock.py, fixtures.mock.js)
- `samples/` : fixtures d'exemple pour les mocks (sample_fixture.py, sample_fixture.js)
- `tests/` : tous les tests unitaires JS & Python
- `__init__.py` / `__init__.js` : points d'entrée globaux pour import direct
- `index.js` : point d'entrée principal JS (fusion core et samples)
- `index.test.js` / `index.test.py` : tests d'intégration pour l'index

## Exemples d'utilisation

### Python
```python
from .core import ...
from .samples import ...
```

### JavaScript
```js
const mocks = require('./index');
const mock = mocks.fixtures_mock;
const sample = mocks.sample;
```

## Conformité
- Respecte la logique métier 3D avancée
- Compatible avec les outils de test et d'intégration continue
- Prêt pour l'audit et la documentation automatique
