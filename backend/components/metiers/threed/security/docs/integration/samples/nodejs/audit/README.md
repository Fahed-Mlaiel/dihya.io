# Exemples d’intégration Audit Node.js

Ce dossier contient des exemples ultra avancés, clé en main, pour l’intégration du module Audit côté Node.js et Python.

## Structure
- `__init__.js` : Point d’entrée JS pour les samples Audit
- `__init__.py` : Point d’entrée Python pour les samples Audit
- `sample_audit_nodejs.js` : Exemple d’intégration Audit Node.js (usage, import, export, logique métier)
- `sample_audit_python.py` : Exemple d’intégration Audit Python (interopérabilité, logique métier)

## Utilisation Node.js
```js
import { runAuditSample } from './sample_audit_nodejs.js';
runAuditSample();
```

## Utilisation Python
```python
from .sample_audit_python import run_audit_sample
run_audit_sample()
```

---

> Ajoutez ici vos propres scénarios d’intégration avancée pour l’Audit métier.
