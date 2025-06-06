# core – Module IA principal (utils/ai/core)

Ce dossier contient la logique métier principale du module AI pour Threed :
- `ai_core.js` / `ai_core.py` : logique métier IA principale (synchronisée JS/Python, audit, validation, clé en main)
- `ai_core.test.js` / `ai_core.test.py` : tests unitaires ultra avancés, CI/CD ready
- `__init__.js` / `__init__.py` : points d’entrée modulaires (import JS/Python, découverte automatique)
- `__init__.test.js` / `__init__.test.py` : tests d’import des points d’entrée (JS & Python)
- `README.md` : documentation métier, structure, conformité, exemples d’usage

## Exemples d’utilisation

**JavaScript**
```js
const ai = require('./__init__');
ai.process('input');
```

**Python**
```python
from .ai_core import *
process('input')
```

## Bonnes pratiques
- Garder ce dossier centré sur le cœur métier IA (pas de helpers/fallback ici)
- Tous les points d’entrée sont testés automatiquement (JS & Python)
- Synchronisation JS/Python assurée
- Prêt pour CI/CD, audit et documentation automatique
- Respect strict de la logique métier et du cahier des charges
