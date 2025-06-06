# helpers – Helpers IA Threed (ultra avancé)

Ce dossier est prévu pour accueillir des fonctions utilitaires, helpers ou extensions internes au module IA Threed.

## Structure
- `ai_helper.js` / `ai_helper.py` : helpers IA principaux (synchronisés JS/Python, audit, validation, clé en main)
- `ai_helper.test.js` / `ai_helper.test.py` : tests unitaires ultra avancés, CI/CD ready
- `__init__.js` / `__init__.py` : points d’entrée modulaires (import JS/Python, découverte automatique)
- `__init__.test.js` / `__init__.test.py` : tests d’import des points d’entrée (JS & Python)
- `README.md` : documentation métier, structure, conformité, exemples d’usage

## Exemples d’utilisation

**JavaScript**
```js
const helpers = require('./__init__');
const res = helpers.normalizeText('input');
```

**Python**
```python
from .ai_helper import normalize_text
res = normalize_text('input')
```

## Bonnes pratiques
- Un helper = une fonction ou classe réutilisable, documentée, testée
- Tous les points d’entrée sont testés automatiquement (JS & Python)
- Synchronisation JS/Python assurée
- Prêt pour CI/CD, audit et documentation automatique
- Respect strict de la logique métier et du cahier des charges
