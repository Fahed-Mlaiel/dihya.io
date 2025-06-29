# API

Ce dossier regroupe tous les appels API, clients HTTP, endpoints, etc. pour l’application frontend.

## Conventions Lead Dev
- Un fichier par domaine métier (userApi.js, projectApi.js, authApi.js, etc.)
- Utilisation d’un client HTTP centralisé (apiClient.js)
- Gestion du token, des headers, des erreurs dans un seul endroit
- Documentation, exemples, schémas, badges fournis

## Structure type
```
api/
  apiClient.js
  userApi.js
  projectApi.js
  authApi.js
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
