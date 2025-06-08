# Politiques d’accès – Documentation avancée

Ce dossier regroupe toutes les politiques d’accès (FR/EN), la logique métier, les scripts JS/Python, et la documentation professionnelle.

## Structure
- `POLICY_ACCESS_FR.md` : Politique d’accès (FR)
- `POLICY_ACCESS_EN.md` : Access Policy (EN)
- `policies.js` : Fonctions métier, helpers et exports JS pour la gestion des accès
- `policies.py` : Fonctions métier, helpers et exports Python pour la gestion des accès
- `__init__.js` : Point d’entrée JS du module d’accès
- `__init__.py` : Point d’entrée Python du module d’accès

## Utilisation JS
```js
import { getAccessPolicy, setAccessPolicy } from './policies.js';
```

## Utilisation Python
```python
from .policies import get_access_policy, set_access_policy
```

---

> Structure modulaire, claire, conforme au cahier des charges et à la logique métier.
