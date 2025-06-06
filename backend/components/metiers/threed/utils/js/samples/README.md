# JS Samples

Ce dossier contient des exemples d’utilisation, helpers, et cas métiers pour le module JS (synchronisé JS/Python, clé en main).

## Objectif
- Illustrer l’utilisation des helpers et fonctions JS (JS & Python)
- Fournir des cas d’usage concrets pour l’intégration, le test et la documentation
- Servir de base à l’enrichissement métier, à la formation et à l’audit

## Structure recommandée
- `sample_js_helper.js` / `sample_js_helper.py` : helpers d’exemple
- `sample_js_helper.test.js` / `sample_js_helper.test.py` : tests associés
- `__init__.js` / `__init__.py` : points d’entrée
- `__init__.test.js` / `__init__.test.py` : tests d’import

## Exemples d’utilisation
```js
const { sampleJsHelper } = require('./sample_js_helper');
sampleJsHelper('clé en main');
```

```python
from .sample_js_helper import sample_js_helper
sample_js_helper('clé en main')
```
