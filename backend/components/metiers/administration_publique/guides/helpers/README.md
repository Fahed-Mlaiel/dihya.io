# guides/helpers – Helpers et utilitaires pour guides Threed

Ce dossier regroupe tous les helpers, fonctions utilitaires, et validateurs utilisés dans les guides professionnels du module Threed (3D).

## Contenu
- helpers_accessibility.js / .py : helpers pour l’accessibilité
- helpers_plugins.js / .py : helpers pour les plugins
- helpers_services.js / .py : helpers pour les services
- helpers_utils.js / .py : helpers pour les utilitaires
- helpers_views.js / .py : helpers pour les vues

## Bonnes pratiques
- Centraliser toute logique utilitaire ou de validation ici.
- Les helpers doivent être testés et documentés.

## Exemple d’import
```js
const { validateGuide } = require('./helpers_accessibility');
```
