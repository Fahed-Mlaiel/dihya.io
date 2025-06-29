# README_SCHEMA.md – Theme

## Schéma d’architecture (ASCII)
```
[ThemeProvider] → [themes.json, palette.js, branding.js, themeUtils.js] → [UI Components]
```

## Conventions
- Un thème = un fichier dédié (themes.json)
- Branding centralisé (branding.js, Branding.md)
- Palette de couleurs (palette.js)
- Helpers dynamiques (themeUtils.js)

## Exemples d’intégration
```js
import { ThemeProvider } from './ThemeProvider';
import { palette } from './palette';
import { branding } from './branding';
import { getThemeFromPreference } from './themeUtils';
```

## Cas métier réels
- Thème dark/light, branding custom, accessibilité couleurs, adaptation runtime
