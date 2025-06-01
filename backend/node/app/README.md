# Dihya Backend Node App

Ce dossier contient l'application backend Node.js du projet Dihya, conçue pour la gestion avancée de projets IA, VR, AR, etc.

## Fonctionnalités principales
- API RESTful & GraphQL
- Sécurité maximale (CORS, JWT, WAF, anti-DDOS, audit, validation)
- Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Multitenancy, gestion des rôles (admin, user, invité)
- Intégration IA (LLaMA, Mixtral, Mistral, fallback open source)
- SEO backend (robots.txt, sitemap, logs structurés)
- Génération automatique de projets (web, mobile, IA, etc.)
- Système de plugins extensible (API/CLI)
- Conformité RGPD, auditabilité, anonymisation, export
- Tests complets (unitaires, intégration, e2e)
- Déploiement GitHub Actions, Docker, K8s, fallback local
- 100% compatible Codespaces/Linux/CI

## Structure
- `routes/` : routes métiers (agriculture, arts, assurance, ...)
- `templates/` : templates métiers, plugins, modules
- `README.md` : ce fichier

## Démarrage rapide
```bash
npm install
npm run start
```

## Documentation
Chaque fichier contient une documentation intégrée (docstring, type hints, exemples, i18n, sécurité, SEO, etc.).

## Contribution
Voir [CONTRIBUTING.md](../../../../CONTRIBUTING.md)

## Licence
Voir [LICENSE](../../../../LICENSE)
