# Dossier controllers/ – Contrôleurs métier API Threed

Ce dossier contient les contrôleurs principaux JS & Python pour l’API Threed.

## Structure modulaire professionnelle
- `threed_controller.js` / `threed_controller.py` : logique métier, RGPD, audit, accessibilité, hooks, edge cases
- `threed_controller.test.js` / `threed_controller.test.py` : tests unitaires et d’intégration synchronisés JS/Python
- `__init__.js` / `__init__.py` : points d’entrée modulaires, exposant explicitement les méthodes du contrôleur
- `__init__.test.js` / `__init__.test.py` : tests d’intégration des points d’entrée

## Bonnes pratiques & conformité
- Séparer la logique métier, les hooks, l’audit, la RGPD, l’accessibilité
- Synchronisation JS/Python : toute logique métier doit exister dans les deux langages
- Documentation et typage de chaque helper et test
- Intégration à la CI/CD et à l’audit global (tests automatiques, auditabilité, logs)
- Aucun code métier dans les points d’entrée : tout doit passer par les helpers ou contrôleurs

## Exemples d’utilisation

### JS
```js
const { getById, create, update, delete: del } = require('./threed_controller');
const entity = await getById(1);
const created = await create({ name: 'Test', status: 'active', label: 'Test' });
```

### Python
```python
from .threed_controller import get_threed, create_threed
entity = get_threed(1)
created = create_threed({'name': 'Test', 'status': 'active', 'label': 'Test'})
```

## Tests & CI/CD
- Chaque méthode est testée unitairement et en intégration (voir fichiers `.test.js` et `.test.py`)
- Les tests sont synchronisés JS/Python et intégrés à la CI/CD
- Toute modification déclenche l’audit automatique

## Audit & extension
- Ce module est auditable, extensible, et conforme aux exigences métier Threed
- Pour toute extension, ajouter le contrôleur dans `threed_controller.js`/`.py` et l’exposer dans `__init__`
- Voir guides RGPD, audit, conformité dans le dossier `guides/` du projet

---
Pour toute question, voir le README principal du module ou contacter l’équipe métier Threed.
