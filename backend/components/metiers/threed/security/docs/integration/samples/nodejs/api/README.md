# Exemples d’intégration API Node.js

Ce dossier contient des exemples ultra avancés, clé en main, pour l’intégration du module API côté Node.js et Python.

## Structure
- `__init__.js` : Point d’entrée JS pour les samples API
- `__init__.py` : Point d’entrée Python pour les samples API
- `sample_api_nodejs.js` : Exemple d’intégration API Node.js (usage, import, export, logique métier)
- `sample_api_python.py` : Exemple d’intégration API Python (interopérabilité, logique métier)

## Utilisation Node.js
```js
import { runApiSample } from './sample_api_nodejs.js';
runApiSample();
```

## Utilisation Python
```python
from .sample_api_python import run_api_sample
run_api_sample()
```

---

> Ajoutez ici vos propres scénarios d’intégration avancée pour l’API métier.
