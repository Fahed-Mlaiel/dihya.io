# Tests d'intégration : Sécurité

Ce dossier contient les tests d'intégration pour les routes et services de sécurité (authentification, autorisation, CORS, JWT, WAF, anti-DDOS, plugins, RGPD, logs, etc.) dans Dihya.

## Objectifs
- Vérifier l'intégration complète des APIs sécurité (auth, rôles, logs, plugins, RGPD, SEO, accessibilité, etc.).
- Couvrir tous les cas d'usage (admin, user, invité, multi-tenant).
- Tester la conformité RGPD, la sécurité (CORS, JWT, WAF, anti-DDOS), l'auditabilité, la performance, l'extensibilité (plugins, IA fallback).

## Structure des tests
- **Unitaires** : Mock des services sécurité, validation schémas, sécurité, i18n.
- **Intégration** : Endpoints REST/GraphQL, gestion auth/rôles, logs, SEO, accessibilité.
- **E2E** : Scénarios réels multi-utilisateurs, multi-langues, multi-tenant, plugins dynamiques.

## Exécution
```bash
npm run test:integration securite
```

## Multilingue
- Tous les messages, logs et erreurs sont testés en : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Exemples de tests
- Authentification/autorisation (JWT, CORS, RGPD)
- RGPD (anonymisation, logs, export)
- Accessibilité (contrastes, descriptions, multilingue)
- SEO (balises, logs structurés, sitemap)
- Plugins dynamiques (ajout/suppression à chaud)

## Bonnes pratiques
- 100% coverage, pas de faux positifs, robustesse CI/CD, compatibilité Codespaces/Linux.
- Documentation intégrée, type hints, docstrings, logs structurés, anonymisation RGPD.

---

# Integration Tests: Security

This folder contains advanced integration tests for all security-related routes and services (authentication, authorization, CORS, JWT, WAF, anti-DDOS, plugins, GDPR, logs, etc.) in Dihya.

## Goals
- Full coverage of security APIs (auth, roles, logs, plugins, GDPR, SEO, accessibility, etc.).
- All use cases (admin, user, guest, multi-tenant).
- Test GDPR compliance, security (CORS, JWT, WAF, anti-DDOS), auditability, performance, extensibility (plugins, AI fallback).

## Test Structure
- **Unit**: Security service mocks, schema validation, security, i18n.
- **Integration**: REST/GraphQL endpoints, auth/role management, logs, SEO, accessibility.
- **E2E**: Real scenarios, multi-user, multi-language, multi-tenant, dynamic plugins.

## Run
```bash
npm run test:integration securite
```

## Multilingual
- All messages, logs, and errors tested in: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Test Examples
- Authentication/authorization (JWT, CORS, GDPR)
- GDPR (anonymization, logs, export)
- Accessibility (contrast, descriptions, multilingual)
- SEO (tags, structured logs, sitemap)
- Dynamic plugins (hot add/remove)

## Best Practices
- 100% coverage, no false positives, robust CI/CD, Codespaces/Linux compatible.
- Integrated documentation, type hints, docstrings, structured logs, GDPR anonymization.
