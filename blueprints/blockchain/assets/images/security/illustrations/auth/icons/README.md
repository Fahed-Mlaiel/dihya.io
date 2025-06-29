# Auth Icons

Ce dossier regroupe toutes les icônes SVG liées à l’authentification et à la sécurité : login, 2FA, accès sécurisé, reset password, OAuth login, etc.

## Fichiers inclus
- `login.svg` : Icône de connexion
- `2fa.svg` : Icône d’authentification à deux facteurs
- `secure_access.svg` : Icône d’accès sécurisé
- `password_reset.svg` : Icône de réinitialisation de mot de passe
- `oauth_login.svg` : Icône de connexion OAuth

## Bonnes pratiques Lead Dev
- Utiliser ces icônes dans les formulaires, onboarding, pages de sécurité, documentation, etc.
- Préférer SVG pour la qualité et la personnalisation
- Centraliser les imports via `index.js`

## Exemple d’intégration (React)
```jsx
import { Login, TwoFA } from './index.js';

function AuthIcons() {
  return <>
    <img src={Login} alt="Login" />
    <img src={TwoFA} alt="2FA" />
  </>;
}
```

## Contact
Pour toute nouvelle icône, respecter la charte graphique et valider avec le Lead Dev.
