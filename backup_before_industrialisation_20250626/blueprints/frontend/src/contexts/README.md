# Contexts

Ce dossier centralise tous les contextes React globaux de l’application (authentification, thème, langue, etc.).

## Conventions Lead Dev
- Un fichier par contexte global (auth, thème, langue…)
- Fournir un Provider et un hook d’accès pour chaque contexte
- Centralisation stricte, aucune logique métier dispersée
- Documentation, exemples, schémas, badges fournis

## Structure type
```
contexts/
  AuthContext.js
  ThemeContext.js
  LangContext.js
  README.md
  README_EXEMPLES.md
  README_SCHEMA.md
  README_INTEGRATION.md
  README_ARCHITECTURE.md
  contexts.mapping.json
  contexts.meta.json
  contexts.tags.json
  badges.md
```

## Exemples d’intégration
Voir README_EXEMPLES.md et README_INTEGRATION.md

## Schéma d’architecture
Voir README_SCHEMA.md

## Badges
Voir badges.md

---

Ce dossier est prêt pour l’industrialisation, la documentation, la CI/CD, la conformité RGPD, l’accessibilité et la scalabilité.
