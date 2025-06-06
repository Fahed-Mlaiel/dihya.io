# samples – Exemples ultra avancés de helpers et tests IA (utils/ai/samples)

Ce dossier contient des exemples de helpers, de logique IA et de tests ultra avancés pour illustrer les bonnes pratiques, la structure attendue, la conformité CI/CD, l’audit, la synchronisation JS/Python et la logique métier.

## Structure
- `sample_ai_helper.js` / `sample_ai_helper.py` : exemple de helper IA synchronisé JS/Python
- `sample_ai_helper.test.js` / `sample_ai_helper.test.py` : tests unitaires ultra avancés pour les samples
- `__init__.js` / `__init__.py` : points d’entrée modulaires (import JS/Python, découverte automatique)
- `__init__.test.js` / `__init__.test.py` : tests d’import des points d’entrée (JS & Python)
- `README.md` : documentation métier, structure, conformité, exemples d’usage

## Exemples d’utilisation

**JavaScript**
```js
const samples = require('./__init__');
const res = samples.sampleAiHelper('input');
```

**Python**
```python
from .sample_ai_helper import sample_ai_helper
res = sample_ai_helper('input')
```

## Bonnes pratiques
- Synchroniser les exemples entre JS et Python.
- Couvrir les cas critiques, l’audit, la conformité, la traçabilité, la CI/CD.
- Utiliser ces samples comme base pour l’audit, la documentation automatique et la formation.
- Respect strict du cahier des charges et de la logique métier.
