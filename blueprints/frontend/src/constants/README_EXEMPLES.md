# Exemples métiers – Constants

- `routes.js` : Toutes les routes de l’application
- `regex.js` : Regex globales (email, mot de passe…)
- `actions.js` : Clés d’action globales
- `messages.js` : Messages d’erreur/validation réutilisables

## Exemple d’utilisation
```js
import { ROUTE_LOGIN } from './routes';
import { ERROR_INVALID_EMAIL } from './messages';

console.log(ROUTE_LOGIN); // '/login'
console.log(ERROR_INVALID_EMAIL); // 'Adresse email invalide.'
```
