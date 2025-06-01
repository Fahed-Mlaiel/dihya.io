# Dihya Coding – Stratégie de test (FR)

## Introduction
Tout le code doit être entièrement testé (unitaires, intégration, e2e) avec fixtures structurées, mocks et logs d’audit. Les tests couvrent tous les rôles (admin, user, invité) et toutes les langues supportées.

## Types de tests
- Unitaire : fonctions, modèles, plugins
- Intégration : API, BDD, plugins, i18n, sécurité
- E2E : parcours utilisateur (web, mobile, API)
- Sécurité : JWT, CORS, WAF, anti-DDOS, RBAC
- Accessibilité : WCAG 2.2, ARIA

## Lancer les tests
```bash
make test
```

## Couverture
- Minimum : 95%
- Modules critiques : 100%

## Fixtures & Audit
- Utiliser `tests/fixtures/`
- Tous les logs sont auditables/exportables (RGPD)

---
© 2025 Dihya Coding. Tous droits réservés.
