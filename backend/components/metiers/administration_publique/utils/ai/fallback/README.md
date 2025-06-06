# core – Logique métier fallback IA ultra avancée

Ce dossier contient la logique métier principale et les tests pour le fallback IA du module Threed :
- `ai_fallback.js` / `ai_fallback.py` : logique métier fallback IA (synchronisée JS/Python, audit, validation, clé en main)
- `ai_fallback.test.js` / `ai_fallback.test.py` : tests unitaires ultra avancés, CI/CD ready
- `__init__.js` / `__init__.py` : points d’entrée modulaires (import JS/Python, découverte automatique)
- `__init__.test.js` / `__init__.test.py` : tests d’import des points d’entrée (JS & Python)
- `README.md` : documentation métier, structure, conformité, exemples d’usage

## Exemples d’utilisation

**JavaScript**
```js
const { aiFallback } = require('./__init__');
aiFallback('input');
```

**Python**
```python
from .ai_fallback import ai_fallback
ai_fallback('input')
```

## Bonnes pratiques
- Garder ce dossier centré sur le cœur métier IA (pas de helpers/fallback ici)
- Tous les points d’entrée sont testés automatiquement (JS & Python)
- Synchronisation JS/Python assurée
- Prêt pour CI/CD, audit et documentation automatique
- Respect strict de la logique métier et du cahier des charges
