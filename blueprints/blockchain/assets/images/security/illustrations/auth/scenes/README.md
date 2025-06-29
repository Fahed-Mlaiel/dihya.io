# Auth Scenes

Ce dossier regroupe toutes les scènes SVG illustrant des situations d’authentification et de sécurité : login, 2FA, reset password, OAuth login, etc.

## Fichiers inclus
- `login_scene.svg` : Scène de connexion
- `2fa_scene.svg` : Scène d’authentification à deux facteurs
- `password_reset_scene.svg` : Scène de réinitialisation de mot de passe
- `oauth_login_scene.svg` : Scène de connexion OAuth

## Bonnes pratiques Lead Dev
- Utiliser ces scènes dans les pages d’onboarding, guides utilisateurs, documentation, etc.
- Préférer SVG pour la qualité et la personnalisation
- Centraliser les imports via `index.js`

## Exemple d’intégration (React)
```jsx
import { LoginScene, TwoFAScene } from './index.js';

function AuthScenes() {
  return <>
    <img src={LoginScene} alt="Login Scene" />
    <img src={TwoFAScene} alt="2FA Scene" />
  </>;
}
```

## Contact
Pour toute nouvelle scène, respecter la charte graphique et valider avec le Lead Dev.
