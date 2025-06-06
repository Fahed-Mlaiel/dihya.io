# README – docs (guides/core/samples/docs)

Ce dossier contient des exemples ultra avancés de documentation, guides, accessibilité, audit, RGPD, CI/CD, synchronisés JS/Python pour le module guides/core.

- Exemples synchronisés JS/Python
- Edge cases, conformité, audit, accessibilité
- Points d'entrée unifiés (`__init__.py`, `__init__.js`, `index.js`)
- Tests d'import pour chaque point d'entrée

## Exemples d'utilisation

### Python
```python
from .sample_guide_doc import sample_guide_doc
```

### JavaScript
```js
const { sampleGuideDoc } = require('./sample_guide_doc');
```
