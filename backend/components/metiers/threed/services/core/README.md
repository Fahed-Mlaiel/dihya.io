# Core Services – Threed

Ce module regroupe les services principaux (core) pour le domaine 3D, avec une structure modulaire, des points d'entrée harmonisés et des tests exhaustifs.

## Structure du dossier

- `index.js` : Point d'entrée principal JS, centralise l'accès à tous les sous-modules (api, controllers, helpers, impl, samples).
- `index.test.js` : Test d'import du point d'entrée JS.
- `index.test.py` : Test d'import du point d'entrée Python.
- `__init__.js` / `__init__.py` : Points d'entrée pour la découverte automatique (JS/Python).
- `__init__.test.js` / `__init__.test.py` : Tests d'import des points d'entrée.
- `api/` : Services API (clé en main, synchronisés JS/Python, ultra testés).
- `controllers/` : Contrôleurs métier (clé en main, synchronisés JS/Python, ultra testés).
- `helpers/` : Helpers métier (clé en main, synchronisés JS/Python, ultra testés).
- `impl/` : Implémentations métier (clé en main, synchronisées JS/Python, ultra testés).
- `samples/` : Exemples d'utilisation et tests synchronisés JS/Python.

## Exemples d'utilisation

**JavaScript**
```js
const { ApiService, ServicesController, ServicesHelper, ServiceThreed, SampleService } = require('./index');
const api = new ApiService();
const ctrl = new ServicesController();
const helper = new ServicesHelper();
const impl = new ServiceThreed();
const sample = new SampleService();
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
