# Loisirs – Template Dihya Coding

## Présentation
Ce template permet de générer des projets de loisirs (gestion d’activités, événements, IA, VR, AR, multilingue, RGPD, plugins, etc.) avec sécurité maximale et extensibilité.

## Fonctionnalités principales
- Routes RESTful & GraphQL pour la gestion des loisirs
- Sécurité avancée (CORS, JWT, WAF, anti-DDOS, audit)
- Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Multitenancy, gestion des rôles (admin, user, invité)
- Intégration IA fallback (LLaMA, Mixtral, Mistral)
- SEO backend (robots, sitemap, logs structurés)
- Système de plugins
- Conformité RGPD, auditabilité, anonymisation
- Tests complets (unit, integration, e2e)

## Utilisation
1. Personnalisez `template.js` selon vos besoins métier.
2. Définissez vos politiques dans `policy.md`.
3. Lancez les tests avec `test_loisirs.js`.

## Exemples d’API
- POST `/api/loisirs/activite` (création d’activité, validation, audit, i18n)
- GET `/api/loisirs/activites` (filtrage, pagination, rôles, SEO)

## Multilingue
Toutes les routes, messages et logs sont internationalisés.

## Sécurité
Voir `policy.md` pour les règles détaillées.

## Déploiement
Compatible Docker, K8s, GitHub Actions, fallback local.

---

# Leisure – Dihya Coding Template

## Overview
This template enables the creation of advanced leisure projects (activity management, events, AI, VR, AR, multilingual, GDPR, plugins, etc.) with maximum security and extensibility.

## Main Features
- RESTful & GraphQL routes for leisure management
- Advanced security (CORS, JWT, WAF, anti-DDOS, audit)
- Dynamic i18n (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Multitenancy, role management (admin, user, guest)
- Sovereign AI fallback (LLaMA, Mixtral, Mistral)
- Backend SEO (robots, sitemap, structured logs)
- Plugin system
- GDPR compliance, auditability, anonymization
- Full test coverage (unit, integration, e2e)

## Usage
1. Customize `template.js` for your business needs.
2. Define policies in `policy.md`.
3. Run tests with `test_loisirs.js`.

## API Examples
- POST `/api/loisirs/activite` (create activity, validation, audit, i18n)
- GET `/api/loisirs/activites` (filter, pagination, roles, SEO)

## Multilingual
All routes, messages, and logs are internationalized.

## Security
See `policy.md` for detailed rules.

## Deployment
Compatible with Docker, K8s, GitHub Actions, local fallback.
