# Tests d'intégration pour le secteur Agriculture

Ce dossier contient les tests d'intégration pour les fonctionnalités liées à l'agriculture dans la plateforme Dihya Coding.

## Objectifs
- Vérifier l'intégration des modules IA, VR, AR pour l'agriculture.
- Tester la sécurité (CORS, JWT, WAF, anti-DDOS).
- Assurer la conformité RGPD et l'auditabilité.
- Valider l'internationalisation (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es).
- Couvrir les cas d'usage métier (gestion de cultures, prévisions IA, etc.).

## Structure des tests
- Tests unitaires, d'intégration, e2e.
- Utilisation de fixtures et mocks pour les services IA.
- Vérification des logs structurés et de la conformité SEO backend.

## Exécution
```bash
npm run test:integration -- --sector=agriculture
```

## Multilingue
- Tous les messages d'erreur et logs sont testés en multilingue.

## Sécurité
- Tests d'injection, brute force, XSS, CSRF, etc.

## Extensibilité
- Ajout facile de nouveaux cas via plugins ou API.

---

# Integration Tests for Agriculture Sector

This folder contains integration tests for agriculture-related features in the Dihya Coding platform.

## Goals
- Validate integration of AI, VR, AR modules for agriculture.
- Test security (CORS, JWT, WAF, anti-DDOS).
- Ensure GDPR compliance and auditability.
- Validate internationalization (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es).
- Cover business use cases (crop management, AI forecasts, etc.).

## Test Structure
- Unit, integration, and e2e tests.
- Use of fixtures and mocks for AI services.
- Check structured logs and backend SEO compliance.

## Run
```bash
npm run test:integration -- --sector=agriculture
```

## Multilingual
- All error messages and logs are tested in multiple languages.

## Security
- Tests for injection, brute force, XSS, CSRF, etc.

## Extensibility
- Easily add new cases via plugins or API.
