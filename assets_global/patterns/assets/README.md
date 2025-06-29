# Assets Patterns – Documentation

Ce dossier contient tous les assets patterns (SVG, PNG, etc.), leurs miniatures, previews, manifestes, modules d’accès et documentation.

## Structure
- `index.js`, `__init__.py` : Points d’entrée JS/Python
- `assets_manifest.json` : Manifest complet des assets
- `preview.json` : Exemples de previews
- `thumbnails/`, `previews/`, `assets/` : Fichiers visuels
- `doc/` : Documentation d’usage et conventions
- `access_module.js`, `access_module.py` : Modules d’accès programmatiques
- `i18n/` : Traductions

## Exemple d’intégration
```js
import { getAsset } from './access_module';
const svg = getAsset('pattern1');
```

Voir la documentation dans `doc/` pour plus de détails.
