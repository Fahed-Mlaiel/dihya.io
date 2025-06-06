# fixtures (racine)

Ce dossier regroupe toutes les fixtures ultra avancées pour le module Threed (JS & Python), organisées par logique métier et selon le cahier des charges Dihya.

## Structure (mise à jour 2025)
- `core/` : modèles, générateurs, samples, tests (structure ultra modulaire)
- `helpers/` : helpers, validators, samples, tests (organisation claire par rôle, synchronisation JS/Python, conformité RGPD, accessibilité, audit, CI/CD)
- `mocks/` : mocks principaux, samples, tests (pour la simulation et le test avancé)
- `services/` : services métiers pour l'environnement de fixtures (core, tests)
- `__init__.py` / `__init__.js` : points d'entrée globaux pour import direct (fusion core/helpers)
- `index.js` / `index.py` : points d'entrée principaux (fusionne tous les sous-modules)
- `index.test.js` / `index.test.py` : tests d'intégration globaux (JS & Python)
- `README_ADVANCED.md` / `README_UNITTESTS.md` : documentation avancée et guide de tests

## Exemples d'utilisation (synchronisés)

### Python
```python
from .core import ...
from .helpers import ...
from .mocks import ...
from .services import ...
```

### JavaScript
```js
const fixtures = require('./index');
const model = fixtures.sample3DModel;
const helper = fixtures.getModelById;
const mock = fixtures.fixtures_mock;
const service = fixtures.getEnvironnement;
```

## Conformité & bonnes pratiques
- Respecte la logique métier 3D avancée et le cahier des charges Dihya
- Compatible avec les outils de test, CI/CD, audit et documentation automatique
- Structure modulaire, évolutive, prête pour l’industrialisation
- Synchronisation stricte JS/Python, conformité RGPD/accessibilité, auditabilité
