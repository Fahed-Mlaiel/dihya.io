# Dossier models (fixtures/core/models)

Ce dossier regroupe toutes les fixtures statiques ultra avancées pour le module Threed, en Python et JavaScript. Il répond à la logique métier 3D et au cahier des charges Dihya.

## Structure
- `fixtures.js` : Modèles, assets, utilisateurs, scènes (JavaScript)
- `fixtures.py` : Modèles, assets, utilisateurs, scènes (Python)
- `sample_fixture.js` : Exemple de fixture minimaliste (JavaScript)
- `sample_fixture.py` : Exemple de fixture minimaliste (Python)
- `__init__.js` / `__init__.py` : Points d'entrée pour import direct des fixtures

## Exemples d'utilisation

### JavaScript
```js
const { sample3DModel, assets, users, sample } = require('./models');
```

### Python
```python
from .models import sample_3d_asset, advanced_3d_model, asset_texture, user_admin
```

## Conformité
- Respecte la logique métier 3D avancée
- Compatible avec les outils de test et d'intégration continue
- Prêt pour l'audit et la documentation automatique
