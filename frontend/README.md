# Dihya Frontend – README

## Description
Frontend React ultra-avancé : sécurité, i18n, SEO, accessibilité, multitenancy, plugins, RGPD, audit, tests, CI/CD, déploiement Docker/K8s/GitHub Actions, etc.

## Fonctionnalités principales
- App React sécurisée, i18n dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Authentification JWT, gestion des rôles, multitenancy
- Plugins dynamiques, fallback IA open source
- RGPD, auditabilité, anonymisation, export
- SEO (robots.txt, sitemap.xml, manifest, logs structurés)
- Tests complets (unitaires, intégration, e2e, accessibilité)
- Déploiement Docker, K8s, GitHub Actions, fallback local
- 100% compatible Codespaces, Linux, CI

## Structure du projet
- `src/` : code source React
- `public/` : assets, SEO, manifest
- `tests/` : tests unitaires, intégration, e2e

## Installation & lancement
```bash
cd frontend
npm install
npm run test
npm start
```

## Déploiement Docker
```bash
docker build -t dihya-frontend .
docker run -p 3000:3000 dihya-frontend
```

## Déploiement CI/CD
- Voir `.github/workflows/` et `docker-compose.yml`

## Contribution
- Voir `CONTRIBUTING.md`

---
*Document généré automatiquement, à adapter selon le contexte.*
