# Tests d'intégration pour le secteur Arts

Ce dossier contient les tests d'intégration pour les fonctionnalités liées aux arts dans la plateforme Dihya Coding.

## Objectifs
- Vérifier l'intégration des modules IA, VR, AR pour les arts.
- Tester la sécurité (CORS, JWT, WAF, anti-DDOS).
- Assurer la conformité RGPD et l'auditabilité.
- Valider l'internationalisation (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es).
- Couvrir les cas d'usage métier (gestion d'œuvres, IA créative, etc.).

## Structure des tests
- Tests unitaires, d'intégration, e2e.
- Utilisation de fixtures et mocks pour les services IA.
- Vérification des logs structurés et de la conformité SEO backend.

## Exécution
```bash
npm run test:integration -- --sector=arts
```

## Multilingue
- Tous les messages d'erreur et logs sont testés en multilingue.

## Sécurité
- Tests d'injection, brute force, XSS, CSRF, etc.

## Extensibilité
- Ajout facile de nouveaux cas via plugins ou API.

---

# Integration Tests for Arts Sector

This folder contains integration tests for arts-related features in the Dihya Coding platform.

## Goals
- Validate integration of AI, VR, AR modules for arts.
- Test security (CORS, JWT, WAF, anti-DDOS).
- Ensure GDPR compliance and auditability.
- Validate internationalization (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es).
- Cover business use cases (artwork management, creative AI, etc.).

## Test Structure
- Unit, integration, and e2e tests.
- Use of fixtures and mocks for AI services.
- Check structured logs and backend SEO compliance.

## Run
```bash
npm run test:integration -- --sector=arts
```

## Multilingual
- All error messages and logs are tested in multiple languages.

## Security
- Tests for injection, brute force, XSS, CSRF, etc.

## Extensibility
- Easily add new cases via plugins or API.
