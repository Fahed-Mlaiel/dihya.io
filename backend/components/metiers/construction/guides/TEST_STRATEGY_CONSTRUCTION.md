# Stratégie de Test Construction

Stratégie de test complète pour le métier Construction.

## Types de tests
- Tests unitaires (Python, JS)
- Tests d’intégration (API, plugins, RGPD, audit)
- Tests E2E (scénarios métier, accessibilité, sécurité)
- Tests de sécurité (OWASP, penetration tests)
- Tests RGPD (export, anonymisation, suppression)
- Tests plugins (activation, désactivation, hooks)

## CI/CD
- Exécution automatique des tests à chaque build (voir Makefile, docker-compose.yml)
- Génération de rapports (pytest, jest, coverage)
- Badges de conformité (README, CI/CD)

## Bonnes pratiques
- Couverture > 90% (unitaires + intégration)
- Tests multilingues (fr, en, ar, ber)
- Fixtures et mocks pour chaque scénario

## Outils
- pytest, unittest, jest, supertest, axe, pa11y
