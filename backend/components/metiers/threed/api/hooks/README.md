<!-- filepath: /workspaces/dihya.io/backend/components/metiers/threed/api/hooks/README.md -->
# Dossier hooks/ – Hooks métier API Threed

Ce dossier contient les hooks JS & Python et leurs tests.

## Structure modulaire professionnelle
- `hooks.js` / `hooks.py` : hooks avant/après action, audit, RGPD, accessibilité
- `hooks.test.js` / `hooks.test.py` : tests unitaires et d’intégration
- `__init__.js` / `__init__.py` : points d’entrée modulaires
- `__init__.test.js` / `__init__.test.py` : tests d’intégration des points d’entrée

## Bonnes pratiques & conformité
- Synchroniser la logique hooks JS/Python
- Hooks audités, extensibles, auditabilité, logs
- Intégration à la CI/CD et à l’audit global
- Aucun code métier dans les points d’entrée : tout doit passer par les helpers

## Exemples d’utilisation

### JS
```js
const { beforeAction, afterAction } = require('./hooks');
beforeAction('read', { id: 1 });
```

### Python
```python
from .hooks import before_action, after_action
before_action('read', {'id': 1})
```

## Tests & CI/CD
- Chaque hook est testé unitairement et en intégration
- Les tests sont synchronisés JS/Python et intégrés à la CI/CD
- Toute modification déclenche l’audit automatique

---
Pour toute question, voir le README principal du module ou contacter l’équipe métier Threed.
