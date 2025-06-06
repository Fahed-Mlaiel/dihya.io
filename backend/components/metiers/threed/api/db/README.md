<!-- filepath: /workspaces/dihya.io/backend/components/metiers/threed/api/db/README.md -->
# Dossier db/ – Accès données & mock DB API Threed

Ce dossier contient les modules d’accès aux données (mock DB) JS & Python et leurs tests.

## Structure modulaire professionnelle
- `db.js` / `db.py` : accès données, mock DB, helpers CRUD synchronisés JS/Python
- `db.test.js` / `db.test.py` : tests unitaires et d’intégration
- `__init__.js` / `__init__.py` : points d’entrée modulaires
- `__init__.test.js` / `__init__.test.py` : tests d’intégration des points d’entrée

## Bonnes pratiques & conformité
- Synchroniser la logique d’accès données JS/Python
- Mock DB conforme aux besoins métier, auditabilité, logs
- Intégration à la CI/CD et à l’audit global
- Aucun code métier dans les points d’entrée : tout doit passer par les helpers

## Exemples d’utilisation

### JS
```js
const db = require('./db');
const entity = db.findById('threed', 1);
```

### Python
```python
from .db import db_find_by_id
entity = db_find_by_id('threed', 1)
```

## Tests & CI/CD
- Chaque helper est testé unitairement et en intégration
- Les tests sont synchronisés JS/Python et intégrés à la CI/CD
- Toute modification déclenche l’audit automatique

---
Pour toute question, voir le README principal du module ou contacter l’équipe métier Threed.
