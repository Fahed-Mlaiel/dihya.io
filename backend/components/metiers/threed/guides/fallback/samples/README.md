# samples – Exemples ultra avancés pour guides/fallback

Ce dossier regroupe des exemples clé en main pour la documentation, l’accessibilité, l’audit, la conformité RGPD, la CI/CD et l’extension métier, synchronisés JS/Python.

- Synchronisation JS/Python
- Audit, RGPD, accessibilité, edge cases, CI/CD
- Tests ultra avancés pour chaque sample
- Points d'entrée unifiés (`__init__.py`, `__init__.js`, `index.js`)

## Exemples d’utilisation

### JavaScript
```js
const samples = require('./samples');
const { sampleFallbackCase } = samples;
```

### Python
```python
from .samples import sample_fallback_case
```

## Bonnes pratiques
- Utiliser les points d'entrée pour importer tous les samples de façon modulaire
- Ajouter des tests pour chaque nouveau sample ou edge case
- Maintenir la synchronisation JS/Python et la conformité RGPD/accessibilité
