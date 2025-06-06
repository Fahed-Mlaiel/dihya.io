# Validators – Structure avancée

Ce module est organisé pour une évolutivité et une conformité maximale :

- `core/` : logique métier principale (validators.js, validators.py, tests, README)
- `helpers/` : helpers validators (exemple, tests, README)
- `fallback/` : fallback validators (gestion d’échec, tests, README, structure tests)
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
  validators.js
  validators.py
  validators.test.js
  validators.test.py
helpers/
  validators_helper.js
  validators_helper.py
  validators_helper.test.js
  validators_helper.test.py
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
- Exemples d’utilisation JS/Python pour tous les sous-modules (core, helpers, fallback)
- Tests unitaires avancés synchronisés JS/Python
- Points d’entrée d’organisation (`__init__.js`, `__init__.py`) et leurs tests
- README détaillé avec structure, bonnes pratiques, conformité, extension

### Utilisation rapide

**JS**
```js
const validators = require('./core/validators');
const data = require('./samples/sample_validators_data.json');
console.log(validators.validateEmail(data.email));
```

**Python**
```python
from core import validators
import json
with open('samples/sample_validators_data.json') as f:
    data = json.load(f)
print(validators.validate_email(data['email']))
```

---

> Ajoutez vos propres exemples, cas métiers et tests dans `samples/` pour accélérer l’intégration, la validation et l’audit du module validators.
