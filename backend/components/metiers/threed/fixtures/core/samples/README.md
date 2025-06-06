# samples – Exemples ultra avancés pour fixtures/core

Ce dossier regroupe des exemples clé en main pour la génération de fixtures 3D (modèles, utilisateurs, edge cases, conformité RGPD, accessibilité, audit, CI/CD, internationalisation).

- Synchronisation JS/Python
- Audit, RGPD, accessibilité, edge cases, CI/CD
- Tests ultra avancés pour chaque sample
- Points d'entrée unifiés (`__init__.py`, `__init__.js`, `index.js`)
- Tests d'import pour chaque point d'entrée (`__init__.test.js`, `index.test.js`)

## Exemples d'utilisation

### JavaScript
```js
const samples = require('./__init__');
const { sampleModels, sampleUsers } = samples;
```

### Python
```python
from .models import sample_models
from .users import sample_users
```

## Bonnes pratiques
- Utiliser les points d'entrée pour importer tous les samples de façon modulaire
- Ajouter des tests pour chaque nouveau sample ou edge case
- Maintenir la synchronisation JS/Python et la conformité RGPD/accessibilité
