# README_INTEGRATION.md – Assets webApp

## Intégration des assets dans le webApp

### 1. Import centralisé
```js
import { assets } from './assets/index.js';
```

### 2. Utilisation dans un composant React
```jsx
<img src={assets.images['onboarding-ar']} alt="Onboarding (arabe)" />
```

### 3. Ajout d’un nouvel asset
- Placer le fichier dans le bon dossier (`fonts`, `icons`, `images`)
- Mettre à jour l’`index.js` et la documentation
- Ajouter la clé dans `i18n.assets.json` si multilingue

### 4. Accessibilité
- Toujours renseigner l’attribut `alt` ou `aria-label`

### 5. Versionnage
- Incrémenter le nom du fichier si modification majeure (ex: icon-marketplace-v2.svg)

## Bonnes pratiques
- Respecter la structure, conventions et checklist LeadDev
- Documenter toute modification dans le CHANGELOG

Dernière mise à jour : 19/06/2025
