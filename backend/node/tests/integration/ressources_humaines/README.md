# Tests d'intégration : Ressources Humaines

Ce dossier contient les tests d'intégration pour les routes et services RH (gestion des utilisateurs, rôles, IA, plugins, RGPD, multilingue, logs, etc.) dans Dihya.

## Objectifs
- Vérifier l'intégration complète des APIs RH (gestion utilisateurs, rôles, IA, logs, plugins, RGPD, SEO, accessibilité, etc.).
- Couvrir tous les cas d'usage (admin, user, invité, multi-tenant).
- Tester la conformité RGPD, la sécurité (CORS, JWT, WAF, anti-DDOS), l'auditabilité, la performance, l'extensibilité (plugins, IA fallback).

## Structure des tests
- **Unitaires** : Mock des services RH, validation schémas, sécurité, i18n.
- **Intégration** : Endpoints REST/GraphQL, gestion utilisateurs, rôles, logs, SEO, accessibilité.
- **E2E** : Scénarios réels multi-utilisateurs, multi-langues, multi-tenant, plugins dynamiques.

## Exécution
```bash
npm run test:integration ressources_humaines
```

## Multilingue
- Tous les messages, logs et erreurs sont testés en : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Exemples de tests
- Gestion utilisateurs (CRUD, rôles, RGPD)
- RGPD (anonymisation, logs, export)
- Accessibilité (contrastes, descriptions, multilingue)
- SEO (balises, logs structurés, sitemap)
- Plugins dynamiques (ajout/suppression à chaud)

## Bonnes pratiques
- 100% coverage, pas de faux positifs, robustesse CI/CD, compatibilité Codespaces/Linux.
- Documentation intégrée, type hints, docstrings, logs structurés, anonymisation RGPD.

---

# Integration Tests: Human Resources

This folder contains advanced integration tests for all HR-related routes and services (user management, roles, AI, plugins, GDPR, multilingual, logs, etc.) in Dihya.

## Goals
- Full coverage of HR APIs (user management, roles, AI, logs, plugins, GDPR, SEO, accessibility, etc.).
- All use cases (admin, user, guest, multi-tenant).
- Test GDPR compliance, security (CORS, JWT, WAF, anti-DDOS), auditability, performance, extensibility (plugins, AI fallback).

## Test Structure
- **Unit**: HR service mocks, schema validation, security, i18n.
- **Integration**: REST/GraphQL endpoints, user management, roles, logs, SEO, accessibility.
- **E2E**: Real scenarios, multi-user, multi-language, multi-tenant, dynamic plugins.

## Run
```bash
npm run test:integration ressources_humaines
```

## Multilingual
- All messages, logs, and errors tested in: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Test Examples
- User management (CRUD, roles, GDPR)
- GDPR (anonymization, logs, export)
- Accessibility (contrast, descriptions, multilingual)
- SEO (tags, structured logs, sitemap)
- Dynamic plugins (hot add/remove)

## Best Practices
- 100% coverage, no false positives, robust CI/CD, Codespaces/Linux compatible.
- Integrated documentation, type hints, docstrings, structured logs, GDPR anonymization.
