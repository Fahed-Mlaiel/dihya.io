# Exporter Samples

Ce dossier contient des exemples d’utilisation, helpers, et cas métiers pour le module d’exporter.

## Objectif
- Illustrer l’utilisation des helpers et fonctions d’export (JS & Python)
- Fournir des cas d’usage concrets pour l’intégration, le test et la documentation
- Servir de base à l’enrichissement métier, à la formation et à l’audit

## Structure recommandée
- `sample_exporter_helper.js` / `sample_exporter_helper.py` : helpers d’exemple
- `sample_exporter_helper.test.js` / `sample_exporter_helper.test.py` : tests associés
- `__init__.js` / `__init__.py` : points d’entrée
- `__init__.test.js` / `__init__.test.py` : tests d’import

## Exemples d’utilisation
```js
const { sampleExport } = require('./sample_exporter_helper');
sampleExport({id: 1, name: 'Test'});
```

```python
from .sample_exporter_helper import sample_export
sample_export({'id': 1, 'name': 'Test'})
```
