# Politiques RGPD – Documentation avancée

Ce dossier regroupe toutes les politiques RGPD (FR/EN), la logique métier, les scripts JS/Python, et la documentation professionnelle.

## Structure
- `POLICY_RGPD_FR.md` : Politique RGPD (FR)
- `POLICY_RGPD_EN.md` : RGPD Policy (EN)
- `policies.js` : Fonctions métier, helpers et exports JS pour la gestion RGPD
- `policies.py` : Fonctions métier, helpers et exports Python pour la gestion RGPD
- `__init__.js` : Point d’entrée JS du module RGPD
- `__init__.py` : Point d’entrée Python du module RGPD

## Utilisation JS
```js
import { getRgpdPolicy, setRgpdPolicy } from './policies.js';
```

## Utilisation Python
```python
from .policies import get_rgpd_policy, set_rgpd_policy
```

---

> Structure modulaire, claire, conforme au cahier des charges et à la logique métier.
