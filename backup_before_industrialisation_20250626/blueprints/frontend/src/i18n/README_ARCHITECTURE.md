# Architecture du module i18n

Ce document décrit l’architecture, les conventions, les schémas et les exemples d’intégration du module d’internationalisation (i18n).

## Schéma d’architecture

```ascii
/i18n
  ├── i18n.js
  ├── autoTranslate.js
  ├── dialectSupport.js
  ├── localeUtils.js
  ├── index.js
  ├── locales/
      ├── fr.json, en.json, ar.json, ...
```

## Conventions
- Tous les scripts sont typés, documentés, testés.
- Les fichiers de langue sont dans `locales/` (un fichier par langue/dialecte).
- Les helpers (autoTranslate, dialectSupport, localeUtils) sont exportés via `index.js`.

## Exemples d’intégration

```js
import { t, setLanguage } from './i18n';
const label = t('welcome');
setLanguage('ar');
```

## Cas d’usage
- Affichage multilingue, détection automatique, traduction dynamique, support des dialectes, automatisation des traductions.
