# README_SCHEMA.md – Locales

## Schéma d’architecture (ASCII)
```
[i18n.js] → [locales/fr.json, en.json, ...] → [useTranslation]
```

## Conventions
- Un fichier .json et .js par langue/dialecte
- Structure métier complète (titres, menus, notifications, onboarding, marketplace, plugins, sécurité, etc.)
- Ajout de nouvelles langues documenté

## Exemple d’intégration
```js
import fr from './fr.json';
```
