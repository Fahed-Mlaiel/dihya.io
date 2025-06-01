# Tests d'intégration backend Dihya

Ce dossier regroupe les tests d'intégration avancés couvrant toutes les routes, modules, plugins et services du backend Dihya.

## Objectifs
- Sécurité maximale (CORS, JWT, WAF, anti-DDOS, validation)
- Internationalisation dynamique (fr, en, ar, ...)
- Multitenancy, gestion des rôles (admin, user, invité)
- Intégration IA (LLaMA, Mixtral, fallback)
- RGPD, auditabilité, anonymisation
- SEO backend (robots, sitemap, logs structurés)

## Structure
- Un dossier par secteur métier
- Fichiers de tests REST/GraphQL, fixtures, mocks, plugins

## Exécution
```bash
pytest --tb=short --maxfail=1
```

---

# Dihya backend integration tests

This folder contains advanced integration tests for all backend routes, modules, plugins, and services.

## Goals
- Maximum security (CORS, JWT, WAF, anti-DDOS, validation)
- Dynamic i18n (fr, en, ar, ...)
- Multitenancy, roles (admin, user, guest)
- AI integration (LLaMA, Mixtral, fallback)
- GDPR, auditability, anonymization
- Backend SEO (robots, sitemap, structured logs)

## Structure
- One folder per business sector
- REST/GraphQL test files, fixtures, mocks, plugins

## Run
```bash
pytest --tb=short --maxfail=1
```
