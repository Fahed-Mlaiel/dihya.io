# Dihya Backend Assets – Exemples d’intégration

## Python
```python
from backend.assets.main import load_asset, load_model, load_config

# Charger un asset générique
asset = load_asset('branding/logo-backend.svg')

# Charger un modèle IA
model = load_model('mixtral-8x7b')

# Charger une configuration JSON
config = load_config('default.json')
```

## Node.js
```js
const { loadAsset, loadModel, loadConfig } = require('./index');

// Charger un asset générique
const asset = loadAsset('branding/logo-backend.svg');

// Charger un modèle IA
const model = loadModel('mixtral-8x7b');

// Charger une configuration JSON
const config = loadConfig('default.json');
```

## REST/GraphQL
- Les assets critiques sont exposés via des endpoints sécurisés (voir backend/ai/views.py, schemas.py).
- Les plugins peuvent enrichir dynamiquement les assets exposés.

## CI/CD
- Les scripts de test valident l’intégrité, la conformité RGPD, la multilingue, l’accessibilité (voir TESTS.md).
- Les assets sont automatiquement audités et versionnés à chaque push.

## Multitenancy
- Les assets sont prêts pour l’intégration dans des workflows multi-tenant (labels multilingues, audit, plugins).

## Plugins
- Voir PLUGINS.md pour l’API plugins et les hooks d’extension.
