# Tests d'intégration : Mobile

Ce dossier contient les tests d'intégration pour les routes et services mobiles (API REST, GraphQL, notifications, sécurité, plugins, IA, multilingue, accessibilité, RGPD, etc.) du projet Dihya.

## Objectifs
- Vérifier l'intégration complète des APIs mobiles (auth, notifications, IA, sécurité, logs, plugins, RGPD, SEO, accessibilité, etc.).
- Couvrir tous les cas d'usage (admin, user, invité, multi-tenant, multi-device).
- Tester la conformité RGPD, la sécurité (CORS, JWT, WAF, anti-DDOS), l'auditabilité, la performance, l'extensibilité (plugins, IA fallback).

## Structure des tests
- **Unitaires** : Mock des services mobiles, validation schémas, sécurité, i18n.
- **Intégration** : Endpoints REST/GraphQL, notifications, fallback IA, logs, SEO, accessibilité.
- **E2E** : Scénarios réels multi-utilisateurs, multi-langues, multi-tenant, plugins dynamiques.

## Exécution
```bash
npm run test:integration mobile
```

## Multilingue
- Tous les messages, logs et erreurs sont testés en : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Exemples de tests
- Authentification sécurisée (JWT, CORS, RGPD)
- Notifications multicanal (push, email, SMS)
- Accessibilité mobile (voice over, contrastes, multilingue)
- SEO mobile (balises, logs structurés, sitemap)
- Plugins dynamiques (ajout/suppression à chaud)

## Bonnes pratiques
- 100% coverage, pas de faux positifs, robustesse CI/CD, compatibilité Codespaces/Linux.
- Documentation intégrée, type hints, docstrings, logs structurés, anonymisation RGPD.

---

# Integration Tests: Mobile

This folder contains advanced integration tests for all mobile-related routes and services (REST API, GraphQL, notifications, security, plugins, AI, multilingual, accessibility, GDPR, etc.) in Dihya.

## Goals
- Full coverage of mobile APIs (auth, notifications, AI, security, logs, plugins, GDPR, SEO, accessibility, etc.).
- All use cases (admin, user, guest, multi-tenant, multi-device).
- Test GDPR compliance, security (CORS, JWT, WAF, anti-DDOS), auditability, performance, extensibility (plugins, AI fallback).

## Test Structure
- **Unit**: Mobile service mocks, schema validation, security, i18n.
- **Integration**: REST/GraphQL endpoints, notifications, AI fallback, logs, SEO, accessibility.
- **E2E**: Real scenarios, multi-user, multi-language, multi-tenant, dynamic plugins.

## Run
```bash
npm run test:integration mobile
```

## Multilingual
- All messages, logs, and errors tested in: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Test Examples
- Secure authentication (JWT, CORS, GDPR)
- Multichannel notifications (push, email, SMS)
- Mobile accessibility (voice over, contrast, multilingual)
- Mobile SEO (tags, structured logs, sitemap)
- Dynamic plugins (hot add/remove)

## Best Practices
- 100% coverage, no false positives, robust CI/CD, Codespaces/Linux compatible.
- Integrated documentation, type hints, docstrings, structured logs, GDPR anonymization.
