# Journalisme – Template Dihya Coding

## Présentation
Ce template permet de générer des projets de journalisme numérique (web, mobile, IA, VR, AR) avec sécurité, multilingue, conformité RGPD, extensibilité, et intégration IA souveraine.

## Fonctionnalités principales
- Génération de routes RESTful et GraphQL pour la gestion de contenus journalistiques
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
3. Lancez les tests avec `test_journalisme.js`.

## Exemples d’API
- POST `/api/journalisme/article` (création d’article, validation, audit, i18n)
- GET `/api/journalisme/articles` (filtrage, pagination, rôles, SEO)

## Multilingue
Toutes les routes, messages et logs sont internationalisés.

## Sécurité
Voir `policy.md` pour les règles détaillées.

## Déploiement
Compatible Docker, K8s, GitHub Actions, fallback local.

---

# Journalism – Dihya Coding Template

## Overview
This template enables the creation of advanced digital journalism projects (web, mobile, AI, VR, AR) with security, multilingual support, GDPR compliance, extensibility, and sovereign AI integration.

## Main Features
- RESTful & GraphQL routes for journalism content management
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
3. Run tests with `test_journalisme.js`.

## API Examples
- POST `/api/journalisme/article` (create article, validation, audit, i18n)
- GET `/api/journalisme/articles` (filter, pagination, roles, SEO)

## Multilingual
All routes, messages, and logs are internationalized.

## Security
See `policy.md` for detailed rules.

## Deployment
Compatible with Docker, K8s, GitHub Actions, local fallback.
