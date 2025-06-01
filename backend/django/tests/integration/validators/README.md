# Validators – Tests d'intégration

Ce dossier contient les tests d'intégration pour les validateurs backend Dihya (validation de schémas, sécurité, RGPD, i18n, plugins, etc.).

## Objectifs
- Vérifier la robustesse, la sécurité et la conformité RGPD des validateurs.
- Tester la compatibilité multi-langues et multi-tenants.
- Couvrir 100% des endpoints REST et GraphQL liés aux validateurs.

## Structure
- Tests automatisés (unitaires, intégration, e2e, mocks, fixtures).

## Exécution
```bash
pytest --tb=short -v
```

## Documentation
Chaque test est documenté (docstring, type hints) et suit les standards Dihya (sécurité, accessibilité, audit, SEO, i18n).

---

# Validators – Integration Tests (EN)

This folder contains all integration tests for Dihya's backend validators. See above for details.
