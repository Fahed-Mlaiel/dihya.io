# Exemples métiers – Contexts

- `AuthContext.js` : Gestion globale de l’authentification
- `ThemeContext.js` : Gestion du thème (dark/light)
- `LangContext.js` : Gestion de la langue (i18n)

## Exemple d’utilisation
```js
import { useAuth } from './AuthContext';
const { user, login, logout } = useAuth();

import { useTheme } from './ThemeContext';
const { theme, toggleTheme } = useTheme();
```
