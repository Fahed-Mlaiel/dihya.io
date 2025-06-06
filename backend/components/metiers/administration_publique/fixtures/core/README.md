# core

Ce dossier contient la logique métier principale des fixtures :
- `fixtures.js` / `fixtures.py` : logique métier principale
- `fixtures.test.js` / `fixtures_mock_test.py` : tests unitaires associés

Bonnes pratiques :
- Garder ce dossier centré sur le cœur métier (pas de helpers, mocks, services ici)
- Ajouter un README par logique complexe si besoin

## Structure avancée
- `models/` : Modèles 3D, assets, utilisateurs (clé en main, synchronisés JS/Python)
- `generators/` : Générateurs de fixtures, tests, edge cases, CI/CD
- `samples/` : Exemples ultra avancés, edge cases, tests, audit, RGPD, accessibilité
- Points d'entrée globaux : `__init__.py`, `__init__.js`, `index.js`

## Bonnes pratiques
- Synchroniser la logique métier et les tests entre JS et Python
- Couvrir tous les cas métier, edge cases, conformité RGPD, accessibilité, audit, CI/CD
- Documenter chaque module, sample et point d'entrée

## Exemples d’utilisation

**JavaScript**
```js
const core = require('./index');
core.generateModel('UltraModel', 12, 20);
```

**Python**
```python
from .models import advanced_3d_model
from .generators import generate_model
model = generate_model('UltraModel', 12, 20)
```

> Respecter la logique modulaire, testée, documentée et conforme au cahier des charges Dihya.
