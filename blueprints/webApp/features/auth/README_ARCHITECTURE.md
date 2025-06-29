# Architecture – Auth

## Schéma d’architecture (ASCII)
```
[LoginForm] [RegisterForm] [ForgotPassword]
      |           |               |
 [useAuth]   [apiService]   [userService]
```

- **LoginForm** : Connexion utilisateur
- **RegisterForm** : Inscription
- **ForgotPassword** : Récupération de mot de passe
- **AuthProvider** : Fournit le contexte d’authentification
