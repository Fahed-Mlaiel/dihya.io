# Audit Samples

Ce dossier contient des exemples d’utilisation, helpers, et cas métiers pour le module d’audit.

## Objectif
- Illustrer l’utilisation des helpers et fonctions d’audit (JS & Python)
- Fournir des cas d’usage concrets pour l’intégration, le test et la documentation
- Servir de base à l’enrichissement métier, à la formation et à l’audit

## Structure recommandée
- `sample_audit_helper.js` / `sample_audit_helper.py` : helpers d’exemple
- `sample_audit_helper.test.js` / `sample_audit_helper.test.py` : tests associés
- `__init__.js` / `__init__.py` : points d’entrée
- `__init__.test.js` / `__init__.test.py` : tests d’import

## Exemples d’utilisation
```js
const { sampleAuditLog } = require('./sample_audit_helper');
sampleAuditLog('user123', 'LOGIN');
```

```python
from .sample_audit_helper import sample_audit_log
sample_audit_log('user123', 'LOGIN')
```
