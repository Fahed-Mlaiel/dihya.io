# Plugins – Structure avancée

Ce module est organisé pour une évolutivité et une conformité maximale :

- `core/` : logique métier principale (pluginManager.js, pluginManager.py, sample_plugin.js, sample_plugin.py, tests, README)
- `helpers/` : helpers plugins (exemple, tests, README)
- `fallback/` : fallback plugins (gestion d’échec, tests, README, structure tests)
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
  pluginManager.js
  pluginManager.py
  pluginManager.test.js
  pluginManager.test.py
  sample_plugin.js
  sample_plugin.py
  sample_plugin.test.js
  sample_plugin.test.py
helpers/
  plugins_helper.js
  plugins_helper.py
  plugins_helper.test.js
  plugins_helper.test.py
fallback/
  fallback.js
  fallback.py
  tests/
    fallback.test.js
    fallback.test.py
```

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
const pluginManager = require('./core/pluginManager');
pluginManager.register('test', () => 'ok');
console.log(pluginManager.run('test'));
```

**Python**
```python
from core.pluginManager import PluginManager
pm = PluginManager()
pm.register('test', lambda: 'ok')
print(pm.run('test'))
```

---

> Ajoutez vos propres exemples, cas métiers et tests dans `samples/` pour accélérer l’intégration, la validation et l’audit du module plugins.

Pour toute extension, créez un sous-dossier dédié (ex : `adapters/`, `formats/`, etc.) selon la logique métier.
