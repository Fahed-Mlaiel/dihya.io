# Transport – Tests d'intégration

Ce dossier contient les tests d'intégration pour toutes les fonctionnalités transport de Dihya (gestion de trajets, réservations, sécurité, RGPD, i18n, plugins, etc.).

## Objectifs
- Vérifier la conformité RGPD, l’auditabilité et la traçabilité.
- Tester la gestion des rôles (admin, user, invité) et le multitenancy.
- Couvrir 100% des endpoints REST et GraphQL liés au transport.
- Assurer la compatibilité multi-langues (fr, en, ar, tzm, de, zh, ja, ko, nl, he, fa, hi, es).

## Structure
- Tests automatisés (unitaires, intégration, e2e, mocks, fixtures).

## Exécution
```bash
pytest --tb=short -v
```

## Documentation
Chaque test est documenté (docstring, type hints) et suit les standards Dihya (sécurité, accessibilité, audit, SEO, i18n).

---

# Transport – Integration Tests (EN)

This folder contains all integration tests for Dihya's transport features. See above for details.
