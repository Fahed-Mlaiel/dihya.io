<!-- filepath: /workspaces/dihya.io/backend/components/metiers/threed/api/middlewares/README.md -->
# Dossier middlewares/ – Middlewares API Threed

Ce dossier contient tous les middlewares JS & Python (RGPD, audit, accessibilité, etc.) et leurs tests.

## Structure modulaire professionnelle
- `middlewares.js` / `middlewares.py` : middlewares RGPD, audit, accessibilité, hooks
- `middlewares.test.js` / `middlewares.test.py` : tests unitaires et d’intégration
- `__init__.js` / `__init__.py` : points d’entrée modulaires
- `__init__.test.js` / `__init__.test.py` : tests d’intégration des points d’entrée

## Bonnes pratiques & conformité
- Synchroniser la logique middlewares JS/Python
- Middlewares audités, extensibles, auditabilité, logs
- Intégration à la CI/CD et à l’audit global
- Aucun code métier dans les points d’entrée : tout doit passer par les helpers

## Exemples d’utilisation

### JS
```js
const { auditRequest, rgpdMiddleware, accessibilityMiddleware } = require('./middlewares');
app.use(rgpdMiddleware);
app.use(accessibilityMiddleware);
app.use(auditRequest);
```

### Python
```python
from .middlewares import audit_request, rgpd_middleware, accessibility_middleware
# Utilisation comme décorateurs ou middlewares FastAPI
```

## Tests & CI/CD
- Chaque middleware est testé unitairement et en intégration
- Les tests sont synchronisés JS/Python et intégrés à la CI/CD
- Toute modification déclenche l’audit automatique

---
Pour toute question, voir le README principal du module ou contacter l’équipe métier Threed.
