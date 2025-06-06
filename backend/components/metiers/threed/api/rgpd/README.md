<!-- filepath: /workspaces/dihya.io/backend/components/metiers/threed/api/rgpd/README.md -->
# Dossier rgpd/ – RGPD métier API Threed

Ce dossier contient les modules RGPD JS & Python et leurs tests.

## Structure modulaire professionnelle
- `rgpd.js` / `rgpd.py` : anonymisation, conformité RGPD, helpers synchronisés JS/Python
- `rgpd.test.js` / `rgpd.test.py` : tests unitaires et d’intégration
- `__init__.js` / `__init__.py` : points d’entrée modulaires
- `__init__.test.js` / `__init__.test.py` : tests d’intégration des points d’entrée

## Bonnes pratiques & conformité
- Synchroniser la logique RGPD JS/Python
- RGPD audité, extensible, auditabilité, logs
- Intégration à la CI/CD et à l’audit global
- Aucun code métier dans les points d’entrée : tout doit passer par les helpers

## Exemples d’utilisation

### JS
```js
const { rgpdSanitize } = require('./rgpd');
const entity = rgpdSanitize({ name: 'Test', email: 'test@dihya.io' });
```

### Python
```python
from .rgpd import rgpd_sanitize
entity = rgpd_sanitize({'name': 'Test', 'email': 'test@dihya.io'})
```

## Tests & CI/CD
- Chaque helper RGPD est testé unitairement et en intégration
- Les tests sont synchronisés JS/Python et intégrés à la CI/CD
- Toute modification déclenche l’audit automatique

---
Pour toute question, voir le README principal du module ou contacter l’équipe métier Threed.
