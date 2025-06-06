# guides/core/plugins/guides

Ce dossier contient les guides ultra avancés sur les plugins pour le module Threed (JS & Python).

- `guide_plugins.py` : Guide métier Python (fonction, best practices, intégration, conformité)
- `guide_plugins.js` : Guide métier JS (fonction, best practices, intégration, conformité)
- `guide_plugins.test.py` / `guide_plugins.test.js` : Tests unitaires avancés

## Exemples d’utilisation

### Python
```python
from .guide_plugins import get_plugins_guide
guide = get_plugins_guide()
```

### JavaScript
```js
const { getPluginsGuide } = require('./guide_plugins');
const guide = getPluginsGuide();
```

## Conformité
- Respecte la logique métier 3D avancée
- Compatible documentation automatique, tests, audit
- Prêt pour CI/CD et industrialisation
