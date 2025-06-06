# Services – Threed

Ce module regroupe tous les services du domaine 3D, avec une structure ultra professionnelle, modulaire, testée et prête pour CI/CD, audit et documentation automatique.

## Structure du dossier

- `index.js` : Point d'entrée principal JS, centralise l'accès à tous les sous-modules (core, fallback, helpers).
- `index.test.js` : Test d'import du point d'entrée JS.
- `index.test.py` : Test d'import du point d'entrée Python.
- `__init__.js` / `__init__.py` : Points d'entrée pour la découverte automatique (JS/Python).
- `__init__.test.js` / `__init__.test.py` : Tests d'import des points d'entrée.
- `core/` : Services principaux (api, controllers, helpers, impl, samples, etc.).
- `fallback/` : Services fallback (clé en main, synchronisés JS/Python, ultra testés).
- `helpers/` : Services utilitaires et helpers métier.

## Exemples d'utilisation

**JavaScript**
```js
const services = require('./index');
const api = services.ApiService;
const ctrl = services.ServicesController;
const helper = services.ServicesHelper;
const impl = services.ServiceThreed;
const sample = services.SampleService;
```

**Python**
```python
from backend.components.metiers.threed.services.core.api import ApiService
from backend.components.metiers.threed.services.core.controllers import ServicesController
from backend.components.metiers.threed.services.core.helpers import ServicesHelper
from backend.components.metiers.threed.services.core.impl import ServiceThreed
from backend.components.metiers.threed.services.core.samples import SampleService
```

## Bonnes pratiques
- Tous les points d'entrée sont testés (JS & Python).
- Synchronisation JS/Python assurée.
- Prêt pour CI/CD, audit et documentation automatique.
- Respect strict de la logique métier et du cahier des charges.

## CI/CD & Documentation
- Les tests sont automatiquement détectés et exécutés.
- La documentation est générée à partir de ce README et des docstrings.

## Conformité
- Structure modulaire, sans doublons, 100% testée, prête pour audit.
- Respect strict des conventions du projet `threed`.
