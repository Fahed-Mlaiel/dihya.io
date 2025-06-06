# Module core/ (routes API Threed) – Ultra avancé

Ce dossier contient les points d’entrée des routes API Threed (Express/JS et FastAPI/Python), la logique de routage, les middlewares critiques, et les tests d’intégration avancés.

## Structure modulaire professionnelle
- `api.js` : routes Express ultra avancées (middlewares, hooks, RGPD, accessibilité, audit, edge cases, synchronisation JS/Python, documentation intégrée)
- `api.py` : routes FastAPI ultra avancées (middlewares, hooks, RGPD, accessibilité, audit, edge cases, synchronisation JS/Python, documentation intégrée)
- `api.test.js` / `api.test.py` : tests d’intégration avancés (edge cases, RGPD, accessibilité, audit, hooks, conformité métier)
- `__init__.js` / `__init__.py` : points d’entrée module, exports explicites

## Bonnes pratiques & conformité
- Synchroniser la logique métier entre JS et Python (toute route ou middleware doit exister dans les deux langages)
- Couvrir tous les cas métier, edge cases, conformité RGPD, accessibilité, audit, hooks, documentation OpenAPI
- Ajouter des tests d’intégration multi-formats (voir fichiers `.test.js` et `.test.py`)
- Documenter chaque route, middleware et edge case
- Intégration à la CI/CD et à l’audit global (tests automatiques, auditabilité, logs)
- Aucun code métier dans les points d’entrée : tout doit passer par les contrôleurs, middlewares ou helpers

## Exemples d’utilisation

### JS (Express)
```js
const express = require('express');
const apiRouter = require('./api/core/api');
const app = express();
app.use('/api', apiRouter);
```

### Python (FastAPI)
```python
from backend.components.metiers.threed.api.core.api import router as api_router
from fastapi import FastAPI
app = FastAPI()
app.include_router(api_router, prefix='/api')
```

## Tests & CI/CD
- Chaque route et middleware est testé en intégration (voir fichiers `.test.js` et `.test.py`)
- Les tests sont synchronisés JS/Python et intégrés à la CI/CD
- Toute modification déclenche l’audit automatique

## Audit & extension
- Ce module est auditable, extensible, et conforme aux exigences métier Threed
- Pour toute extension, ajouter la route ou le middleware dans `api.js`/`.py` et l’exposer dans `__init__`
- Voir guides RGPD, accessibilité, audit, conformité dans le dossier `guides/` du projet

---
Pour toute question, voir le README principal du module ou contacter l’équipe métier Threed.
