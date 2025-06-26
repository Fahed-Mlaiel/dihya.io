# i18n threed

## Fonctionnement clé en main
- Toutes les langues sont stockées dans ce dossier sous forme de fichiers `.json`.
- Les helpers Python (`locales.py`) et JS (`locales.js`) chargent dynamiquement toutes les langues présentes.
- Pour ajouter une langue : créer un fichier `xx.json` (ex : `pt.json` pour portugais) avec les clés métier.
- Utilisez `list_languages()` pour obtenir la liste des langues disponibles.
- Les fonctions `translate(key, lang)` permettent d’obtenir la traduction d’une clé dans la langue voulue.

## Exemple Python
```python
from .locales import translate, list_languages
print(list_languages())
print(translate('hello', 'de'))
```

## Exemple JS
```js
const { translate, listLanguages } = require('./locales');
console.log(listLanguages());
console.log(translate('hello', 'tr'));
```

# Tests centralisés i18n threed

Ce dossier contient les tests pour la couche i18n (Python & JS).
- Ultra avancé, clé en main.
