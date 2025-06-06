# samples – Exemples ultra avancés pour helpers (fixtures/helpers/samples)

Ce dossier regroupe des exemples clé en main pour la génération, la manipulation, la validation et l’audit de fixtures 3D, synchronisés JS/Python, avec edge cases, conformité RGPD, accessibilité, audit, CI/CD.

- Synchronisation JS/Python
- Audit, RGPD, accessibilité, edge cases, CI/CD
- Tests ultra avancés pour chaque sample
- Points d'entrée unifiés (`__init__.py`, `__init__.js`, `index.js`)

## Exemples d’utilisation

### JavaScript
```js
const samples = require('./samples');
const { sampleHelperFixture } = samples;
```

### Python
```python
from .samples import sample_helper_fixture
```

## Bonnes pratiques
- Utiliser les points d'entrée pour importer tous les samples de façon modulaire
- Ajouter des tests pour chaque nouveau sample ou edge case
- Maintenir la synchronisation JS/Python et la conformité RGPD/accessibilité
