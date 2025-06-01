# Tests d'intégration pour le secteur Santé

Ce dossier contient les tests d'intégration pour les fonctionnalités santé dans la plateforme Dihya Coding.

## Objectifs
- Vérifier l'intégration des modules IA, VR, AR pour la santé.
- Tester la sécurité (CORS, JWT, WAF, anti-DDOS).
- Assurer la conformité RGPD et l'auditabilité.
- Valider l'internationalisation (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es).
- Couvrir les cas d'usage métier (gestion de dossiers patients, IA diagnostic, etc.).

## Structure des tests
- Tests unitaires, d'intégration, e2e.
- Utilisation de fixtures et mocks pour les services IA et santé.
- Vérification des logs structurés et de la conformité SEO backend.

## Exécution
```bash
npm run test:integration -- --sector=health
```

## Multilingue
- Tous les messages d'erreur et logs sont testés en multilingue.

## Sécurité
- Tests d'injection, brute force, XSS, CSRF, etc.

## Extensibilité
- Ajout facile de nouveaux cas via plugins ou API.

---

# Integration Tests for Health Sector

This folder contains integration tests for health-related features in the Dihya Coding platform.

## Goals
- Validate integration of AI, VR, AR modules for health.
- Test security (CORS, JWT, WAF, anti-DDOS).
- Ensure GDPR compliance and auditability.
- Validate internationalization (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es).
- Cover business use cases (patient record management, diagnostic AI, etc.).

## Test Structure
- Unit, integration, and e2e tests.
- Use of fixtures and mocks for AI and health services.
- Check structured logs and backend SEO compliance.

## Run
```bash
npm run test:integration -- --sector=health
```

## Multilingual
- All error messages and logs are tested in multiple languages.

## Security
- Tests for injection, brute force, XSS, CSRF, etc.

## Extensibility
- Easily add new cases via plugins or API.
