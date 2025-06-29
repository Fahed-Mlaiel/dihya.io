# Auth – Feature métier

Ce dossier gère toute l’authentification utilisateur (login, inscription, mot de passe oublié, provider, etc.).

## Composants
- LoginForm.jsx
- RegisterForm.jsx
- ForgotPassword.jsx
- AuthProvider.js

## Cas d’usage
- Connexion sécurisée (JWT, RBAC)
- Inscription utilisateur
- Récupération de mot de passe
- Authentification multilingue

## Flux utilisateur
1. L’utilisateur accède à LoginForm
2. S’authentifie via useAuth (hook)
3. Accède au dashboard si succès

## Exemples d’intégration
```jsx
import { useAuth } from '../../hooks/useAuth';
import LoginForm from './LoginForm';
```

## Schéma d’architecture
[LoginForm] → [useAuth] → [apiService] → [userService]
