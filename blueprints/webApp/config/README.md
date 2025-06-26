# Config

Ce dossier centralise toute la configuration de l’application webApp : branding, variables d’environnement, options globales, etc.

## Conventions Lead Dev
- Un fichier par domaine de config (app, env, branding…)
- Centralisation stricte : aucune valeur dupliquée dans le code
- Sécurité : aucune donnée sensible stockée côté webApp
- Documentation, exemples, schémas, badges fournis

## Structure type
```
config/
  appConfig.js
  envConfig.js
  branding.js
  README.md
  README_EXEMPLES.md
  README_SCHEMA.md
  README_INTEGRATION.md
  README_ARCHITECTURE.md
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
