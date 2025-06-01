# Tests d'intégration : Tourisme

Ce dossier contient les tests d'intégration pour les routes et services tourisme (gestion offres, IA, plugins, RGPD, multilingue, logs, accessibilité, etc.) dans Dihya.

## Objectifs
- Vérifier l'intégration complète des APIs tourisme (offres, IA, logs, plugins, RGPD, SEO, accessibilité, etc.).
- Couvrir tous les cas d'usage (admin, user, invité, multi-tenant).
- Tester la conformité RGPD, la sécurité (CORS, JWT, WAF, anti-DDOS), l'auditabilité, la performance, l'extensibilité (plugins, IA fallback).

## Structure des tests
- **Unitaires** : Mock des services tourisme, validation schémas, sécurité, i18n.
- **Intégration** : Endpoints REST/GraphQL, gestion offres, logs, SEO, accessibilité.
- **E2E** : Scénarios réels multi-utilisateurs, multi-langues, multi-tenant, plugins dynamiques.

## Exécution
```bash
npm run test:integration tourisme
```

## Multilingue
- Tous les messages, logs et erreurs sont testés en : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Exemples de tests
- Gestion offres tourisme (CRUD, RGPD)
- RGPD (anonymisation, logs, export)
- Accessibilité (contrastes, descriptions, multilingue)
- SEO (balises, logs structurés, sitemap)
- Plugins dynamiques (ajout/suppression à chaud)

## Bonnes pratiques
- 100% coverage, pas de faux positifs, robustesse CI/CD, compatibilité Codespaces/Linux.
- Documentation intégrée, type hints, docstrings, logs structurés, anonymisation RGPD.

---

# Integration Tests: Tourism

This folder contains advanced integration tests for all tourism-related routes and services (offer management, AI, plugins, GDPR, multilingual, logs, accessibility, etc.) in Dihya.

## Goals
- Full coverage of tourism APIs (offer management, AI, logs, plugins, GDPR, SEO, accessibility, etc.).
- All use cases (admin, user, guest, multi-tenant).
- Test GDPR compliance, security (CORS, JWT, WAF, anti-DDOS), auditability, performance, extensibility (plugins, AI fallback).

## Test Structure
- **Unit**: Tourism service mocks, schema validation, security, i18n.
- **Integration**: REST/GraphQL endpoints, offer management, logs, SEO, accessibility.
- **E2E**: Real scenarios, multi-user, multi-language, multi-tenant, dynamic plugins.

## Run
```bash
npm run test:integration tourisme
```

## Multilingual
- All messages, logs, and errors tested in: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Test Examples
- Tourism offer management (CRUD, GDPR)
- GDPR (anonymization, logs, export)
- Accessibility (contrast, descriptions, multilingual)
- SEO (tags, structured logs, sitemap)
- Dynamic plugins (hot add/remove)

## Best Practices
- 100% coverage, no false positives, robust CI/CD, Codespaces/Linux compatible.
- Integrated documentation, type hints, docstrings, structured logs, GDPR anonymization.
