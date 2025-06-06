<!-- filepath: /workspaces/dihya.io/backend/components/metiers/threed/api/validators/README.md -->
# Dossier validators/ – Validateurs métier API Threed

Ce dossier contient les validateurs JS & Python pour l’API Threed et leurs tests.

## Structure modulaire professionnelle
- `validators.js` / `validators.py` : validation métier, RGPD, accessibilité, audit, edge cases
- `validators.test.js` / `validators.test.py` : tests unitaires et d’intégration
- `__init__.js` / `__init__.py` : points d’entrée modulaires
- `__init__.test.js` / `__init__.test.py` : tests d’intégration des points d’entrée

## Bonnes pratiques & conformité
- Synchroniser la logique validateurs JS/Python
- Validation auditable, extensible, auditabilité, logs
- Intégration à la CI/CD et à l’audit global
- Aucun code métier dans les points d’entrée : tout doit passer par les helpers

## Exemples d’utilisation

### JS
```js
const { validate3dEntity } = require('./validators');
validate3dEntity({ name: 'Test', status: 'active' });
```

### Python
```python
from .validators import validate_3d_entity
validate_3d_entity({'name': 'Test', 'status': 'active'})
```

## Tests & CI/CD
- Chaque validateur est testé unitairement et en intégration
- Les tests sont synchronisés JS/Python et intégrés à la CI/CD
- Toute modification déclenche l’audit automatique

---
Pour toute question, voir le README principal du module ou contacter l’équipe métier Threed.
