# README_SCHEMA.md – Assets mobile

## Schéma d’architecture des assets

```ascii
assets/
  fonts/
    kabyle-font-v1.woff2
    ...
  icons/
    icon-marketplace-fr.svg
    icon-marketplace-ar.svg
    ...
  images/
    onboarding-ar.png
    onboarding-fr.png
    ...
  i18n.assets.json
  index.js
  assets.config.js
  ONBOARDING.md
  CHANGELOG.md
  RELEASE_NOTES.md
  BACKLOG.md
  DECISIONS_PRODUIT.md
  README.md
  STRUCTURE.md
```

## Exemple d’intégration
```js
import { assets } from './assets/index.js';
<img src={assets.icons['icon-marketplace-fr']} alt="Marketplace (FR)" />
```

## Conventions
- Un asset = un fichier, nom explicite, versionné si modifié
- Documentation et exemples dans chaque sous-dossier

Dernière mise à jour : 19/06/2025
