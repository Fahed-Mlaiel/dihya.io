# Tests d'intégration : Médias

Ce dossier contient les tests d'intégration pour les routes et services liés à la gestion avancée des médias (images, vidéos, audio, streaming, IA, VR/AR, etc.) dans Dihya.

## Objectifs
- Vérifier l'intégration complète des APIs médias (upload, transformation, IA, VR/AR, sécurité, RGPD, multilingue, SEO, accessibilité, logs, plugins, etc.).
- Couvrir tous les cas d'usage métier (admin, user, invité, multi-tenant).
- Tester la conformité RGPD, la sécurité (CORS, JWT, WAF, anti-DDOS), l'auditabilité, la performance, et l'extensibilité (plugins, IA fallback).

## Structure des tests
- **Unitaires** : Mock des services médias, validation des schémas, sécurité, i18n.
- **Intégration** : Endpoints REST/GraphQL, upload/download, transformation IA, fallback LLaMA/Mixtral/Mistral, logs, SEO, accessibilité.
- **E2E** : Scénarios réels multi-utilisateurs, multi-langues, multi-tenant, plugins dynamiques.

## Exécution
```bash
npm run test:integration medias
```

## Multilingue
- Tous les messages, logs et erreurs sont testés en : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Exemples de tests
- Upload sécurisé (JWT, CORS, RGPD)
- Transformation IA (fallback open source)
- Accessibilité (sous-titres, descriptions, multilingue)
- SEO (balises, logs structurés, sitemap)
- Plugins dynamiques (ajout/suppression à chaud)

## Bonnes pratiques
- 100% coverage, pas de faux positifs, robustesse CI/CD, compatibilité Codespaces/Linux.
- Documentation intégrée, type hints, docstrings, logs structurés, anonymisation RGPD.

---

# Integration Tests: Media

This folder contains advanced integration tests for all media-related routes and services (images, video, audio, streaming, AI, VR/AR, etc.) in Dihya.

## Goals
- Full coverage of media APIs (upload, transformation, AI, VR/AR, security, GDPR, multilingual, SEO, accessibility, logs, plugins, etc.).
- All business use cases (admin, user, guest, multi-tenant).
- Test GDPR compliance, security (CORS, JWT, WAF, anti-DDOS), auditability, performance, extensibility (plugins, AI fallback).

## Test Structure
- **Unit**: Media service mocks, schema validation, security, i18n.
- **Integration**: REST/GraphQL endpoints, upload/download, AI transformation, fallback LLaMA/Mixtral/Mistral, logs, SEO, accessibility.
- **E2E**: Real scenarios, multi-user, multi-language, multi-tenant, dynamic plugins.

## Run
```bash
npm run test:integration medias
```

## Multilingual
- All messages, logs, and errors tested in: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Test Examples
- Secure upload (JWT, CORS, GDPR)
- AI transformation (open source fallback)
- Accessibility (subtitles, descriptions, multilingual)
- SEO (tags, structured logs, sitemap)
- Dynamic plugins (hot add/remove)

## Best Practices
- 100% coverage, no false positives, robust CI/CD, Codespaces/Linux compatible.
- Integrated documentation, type hints, docstrings, structured logs, GDPR anonymization.
