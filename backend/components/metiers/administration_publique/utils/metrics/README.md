# Metrics – Structure avancée

Ce module est organisé pour une évolutivité et une conformité maximale :

- `core/` : logique métier principale (metrics.js, metrics.py, tests, README)
- `helpers/` : helpers metrics (exemple, tests, README)
- `fallback/` : fallback metrics (gestion d’échec, tests, README, structure tests)
- `README.md` : documentation générale
- Fichiers d'organisation/init : `__init__.js`, `__init__.py`, `index.js`, `index.test.js`, `index.test.py`, `__init__.test.js`, `__init__.test.py`

## Bonnes pratiques
- Un helper = une fonction réutilisable, testée, documentée
- Un fallback = une solution de secours robuste, testée
- Le core = la logique métier principale, testée
- Ajoutez des tests d'intégration dans chaque sous-dossier si besoin
- Respectez la conformité, la traçabilité et la logique métier

## Exemple de structure

```
core/
  metrics.js
  metrics.py
  metrics.test.js
  metrics.test.py
helpers/
  metrics_helper.js
  metrics_helper.py
  metrics_helper.test.js
  metrics_helper.test.py
fallback/
  fallback.js
  fallback.py
  tests/
    fallback.test.js
    fallback.test.py
```

---

Pour toute extension, créez un sous-dossier dédié (ex : `adapters/`, `formats/`, etc.) selon la logique métier.

---

## Dossier `samples/`

Le dossier `samples/` contient :
- `sample_usage.js` : exemple d’utilisation JS du module metrics (calcul de moyenne, etc.)
- `sample_usage.py` : exemple d’utilisation Python
- `sample_metrics_data.json` : jeu de données d’exemple
- Un README détaillé avec structure, exemples, bonnes pratiques

### Utilisation rapide

**JS**
```js
const metrics = require('./core/metrics');
const data = require('./samples/sample_metrics_data.json').metrics;
console.log(metrics.calculerMoyenne(data));
```

**Python**
```python
from .core import metrics
import json
with open('samples/sample_metrics_data.json') as f:
    data = json.load(f)["metrics"]
print(metrics.calculer_moyenne(data))
```

---

> Ajoutez vos propres exemples ou cas métiers dans `samples/` pour accélérer l’intégration et la validation du module metrics.
