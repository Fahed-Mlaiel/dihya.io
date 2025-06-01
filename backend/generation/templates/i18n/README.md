# I18N Template

## Description
Ce template fournit une base pour l’internationalisation dynamique (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es) dans tous les modules générés.

## Fonctionnalités
- Détection automatique de la langue.
- Chargement dynamique des ressources.
- Support multitenancy et rôles.
- Personnalisation facile.

## Utilisation
```js
const i18n = require('./template');
const resources = i18n.load('fr');
```

## Extension
- Ajouter de nouvelles langues en éditant le fichier de ressources.

## Licence
MIT
