# i18n Samples

Ce dossier contient des exemples d’utilisation, helpers, et cas métiers pour le module i18n.

## Objectif
- Illustrer l’utilisation des helpers et fonctions i18n (JS & Python)
- Fournir des cas d’usage concrets pour l’intégration, le test et la documentation
- Servir de base à l’enrichissement métier, à la formation et à l’audit

## Structure recommandée
- `sample_i18n_helper.js` / `sample_i18n_helper.py` : helpers d’exemple
- `sample_i18n_helper.test.js` / `sample_i18n_helper.test.py` : tests associés
- `__init__.js` / `__init__.py` : points d’entrée
- `__init__.test.js` / `__init__.test.py` : tests d’import

## Exemples d’utilisation
```js
const { sampleI18n } = require('./sample_i18n_helper');
sampleI18n('fr', 'Bonjour');
```

```python
from .sample_i18n_helper import sample_i18n
sample_i18n('fr', 'Bonjour')
```
