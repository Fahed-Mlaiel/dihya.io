# Logger Samples

Ce dossier contient des exemples d’utilisation, helpers, et cas métiers pour le module logger (synchronisé JS/Python, clé en main).

## Objectif
- Illustrer l’utilisation des helpers et fonctions logger (JS & Python)
- Fournir des cas d’usage concrets pour l’intégration, le test et la documentation
- Servir de base à l’enrichissement métier, à la formation et à l’audit

## Structure recommandée
- `sample_logger_helper.js` / `sample_logger_helper.py` : helpers d’exemple
- `sample_logger_helper.test.js` / `sample_logger_helper.test.py` : tests associés
- `__init__.js` / `__init__.py` : points d’entrée
- `__init__.test.js` / `__init__.test.py` : tests d’import

## Exemples d’utilisation
```js
const { sampleLoggerHelper } = require('./sample_logger_helper');
sampleLoggerHelper('clé en main');
```

```python
from .sample_logger_helper import sample_logger_helper
sample_logger_helper('clé en main')
```
