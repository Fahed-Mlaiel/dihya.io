# README_SCHEMA.md – API

## Schéma d’architecture (ASCII)
```
[apiClient.js]
     |         \
[userApi.js] [projectApi.js] [authApi.js]
     |                |
[Composants]   [Pages]
```

- apiClient.js : Client HTTP centralisé
- userApi.js : API utilisateurs
- projectApi.js : API projets
- authApi.js : API authentification

## Conventions
- Un fichier par domaine métier
- Gestion centralisée des erreurs et du token
- Réutilisabilité, typage, documentation
