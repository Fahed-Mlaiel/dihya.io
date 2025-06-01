# Services à la personne – Tests d'intégration

Ce dossier contient les tests d'intégration pour les routes et services liés aux services à la personne (aide, accompagnement, gestion des rôles, multitenancy, sécurité, RGPD, etc.).

## Objectifs
- Vérifier la gestion des rôles (admin, user, invité) et le multitenancy.
- Tester la conformité RGPD, l’auditabilité et la traçabilité.
- Couvrir 100% des endpoints REST et GraphQL liés aux services à la personne.
- Assurer la compatibilité multi-langues (fr, en, ar, tzm, de, zh, ja, ko, nl, he, fa, hi, es).

## Structure
- `test_services_personne_django.py` : tests automatisés (unitaires, intégration, e2e, mocks, fixtures).

## Exécution
```bash
pytest --tb=short -v test_services_personne_django.py
```

## Documentation
Chaque test est documenté (docstring, type hints) et suit les standards Dihya (sécurité, accessibilité, audit, SEO, i18n).

---

# Personal Services – Integration Tests (EN)

This folder contains all integration tests for Dihya's personal services features. See above for details.
