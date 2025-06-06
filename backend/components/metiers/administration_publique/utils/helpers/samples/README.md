# Helpers Samples

Ce dossier contient des exemples d’utilisation, helpers, et cas métiers pour le module helpers.

## Objectif
- Illustrer l’utilisation des helpers (JS & Python)
- Fournir des cas d’usage concrets pour l’intégration, le test et la documentation
- Servir de base à l’enrichissement métier, à la formation et à l’audit

## Structure recommandée
- `sample_helper.js` / `sample_helper.py` : helpers d’exemple
- `sample_helper.test.js` / `sample_helper.test.py` : tests associés
- `__init__.js` / `__init__.py` : points d’entrée
- `__init__.test.js` / `__init__.test.py` : tests d’import

## Exemples d’utilisation
```js
const { sampleHelper } = require('./sample_helper');
sampleHelper('exemple');
```

```python
from .sample_helper import sample_helper
sample_helper('exemple')
```
