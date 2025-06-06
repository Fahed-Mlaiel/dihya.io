# router/README.md – Documentation du sous-module router (clé en main)

## Description
Ce dossier contient le routeur ultra avancé pour le module Threed, compatible FastAPI (Python) et Express (Node.js). Il respecte la logique métier, la structure modulaire et le cahier des charges Dihya.

- `router.py` : Routeur FastAPI pour l'API 3D (Python)
- `router.js` : Routeur Express pour l'API 3D (JavaScript)
- `__init__.py` / `__init__.js` : Points d'entrée pour import automatique
- `__init__.test.py` / `__init__.test.js` : Tests d'import des points d'entrée

## Exemples d'utilisation

### Python (FastAPI)
```python
from backend.components.metiers.threed.views.router import router
app.include_router(router)
```

### JavaScript (Express)
```js
const router = require('./router');
app.use(router);
```

## Conformité
- Respecte la logique métier avancée
- Prêt pour CI/CD, audit, documentation automatique
- Compatible multi-stack (Python/JS)
