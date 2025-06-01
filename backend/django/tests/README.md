# Tests Django Dihya

Ce dossier contient tous les tests pour l’API Dihya (unitaires, intégration, e2e, mocks, fixtures, multitenancy, sécurité, RGPD, accessibilité, SEO, plugins, internationalisation, IA fallback, etc.).

## Structure
- `integration/` : tests d’intégration par domaine métier
- `unit/` : tests unitaires (voir dossier parent)
- `e2e/` : tests end-to-end (voir dossier parent)

## Bonnes pratiques
- Couverture maximale, pas de faux positifs
- Utilisation de fixtures, mocks, factories
- Tests multilingues (fr, en, ar, ...)
- Sécurité, accessibilité, performance, RGPD
- Compatible CI/CD, Docker, Codespaces

## Lancer les tests
```bash
pytest --cov --tb=short
```

## Ajout de tests
Ajoutez vos tests dans le dossier métier correspondant. Respectez la structure et la nomenclature.

---

# Dihya Django Tests (EN)

This folder contains all tests for the Dihya API (unit, integration, e2e, mocks, fixtures, multitenancy, security, GDPR, accessibility, SEO, plugins, i18n, AI fallback, etc.).

## Structure
- `integration/`: integration tests by business domain
- `unit/`: unit tests (see parent folder)
- `e2e/`: end-to-end tests (see parent folder)

## Best practices
- Maximum coverage, no false positives
- Use fixtures, mocks, factories
- Multilingual tests (fr, en, ar, ...)
- Security, accessibility, performance, GDPR
- CI/CD, Docker, Codespaces compatible

## Run tests
```bash
pytest --cov --tb=short
```

## Add tests
Add your tests in the relevant business folder. Follow structure and naming conventions.
