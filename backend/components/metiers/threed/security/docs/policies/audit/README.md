# Politiques d’audit – Documentation avancée

Ce dossier regroupe toutes les politiques d’audit (FR/EN), la logique métier, les scripts JS/Python, et la documentation professionnelle.

## Structure
- `POLICY_AUDIT_FR.md` : Politique d’audit (FR)
- `POLICY_AUDIT_EN.md` : Audit Policy (EN)
- `policies.js` : Fonctions métier, helpers et exports JS pour la gestion d’audit
- `policies.py` : Fonctions métier, helpers et exports Python pour la gestion d’audit
- `__init__.js` : Point d’entrée JS du module d’audit
- `__init__.py` : Point d’entrée Python du module d’audit

## Utilisation JS
```js
import { getAuditPolicy, setAuditPolicy } from './policies.js';
```

## Utilisation Python
```python
from .policies import get_audit_policy, set_audit_policy
```

---

> Structure modulaire, claire, conforme au cahier des charges et à la logique métier.
