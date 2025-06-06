# samples – Exemples ultra avancés pour guides/core

Ce dossier regroupe des exemples clé en main pour la documentation, l’accessibilité, l’audit, la conformité RGPD, la CI/CD et l’extension métier, synchronisés JS/Python.

- Synchronisation JS/Python
- Audit, RGPD, accessibilité, edge cases, CI/CD
- Tests ultra avancés pour chaque sample
- Points d'entrée unifiés (`__init__.py`, `__init__.js`, `index.js`)
- **Sous-dossiers structurés** :
  - `docs/` : exemples de guides/documentation, accessibilité, audit, RGPD, CI/CD
  - `samples/` : cas métiers avancés, edge cases, synchronisation JS/Python, extension

## Exemples d’utilisation

### JavaScript
```js
const docs = require('./docs');
const samples = require('./samples');
const { sampleGuideDoc } = docs;
const { sampleAccessibilityCase } = samples;
```

### Python
```python
from .docs import sample_guide_doc
from .samples import sample_accessibility_case
```

## Bonnes pratiques
- Utiliser les points d'entrée pour importer tous les samples de façon modulaire
- Ajouter des tests pour chaque nouveau sample ou edge case
- Maintenir la synchronisation JS/Python et la conformité RGPD/accessibilité
- Organiser les exemples par sous-dossier métier pour une extension et une maintenance optimale
