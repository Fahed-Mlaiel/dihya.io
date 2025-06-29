# README_SCHEMA.md – Constants

## Schéma d’architecture (ASCII)
```
[routes.js] [regex.js] [actions.js] [messages.js]
      |         |           |           |
 [Composants] [Pages] [Features] [Services]
```

- routes.js : Toutes les routes de l’app
- regex.js : Regex globales
- actions.js : Clés d’action globales
- messages.js : Messages d’erreur/validation

## Conventions
- Un fichier par type de constante
- Centralisation, documentation, réutilisabilité
