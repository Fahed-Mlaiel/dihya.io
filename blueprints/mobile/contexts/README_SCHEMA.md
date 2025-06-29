# README_SCHEMA.md – Contexts

## Schéma d’architecture (ASCII)
```
[AuthContext.js] [ThemeContext.js] [LangContext.js]
        |             |             |
   [Composants]   [Pages]   [Features]
```

- AuthContext.js : Authentification globale
- ThemeContext.js : Thème global
- LangContext.js : Langue globale

## Conventions
- Un fichier par contexte global
- Fournir un Provider et un hook d’accès
- Documentation, exemples, schémas
