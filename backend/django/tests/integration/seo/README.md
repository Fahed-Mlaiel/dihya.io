# SEO – Tests d'intégration

Ce dossier contient les tests d'intégration pour toutes les fonctionnalités SEO du backend Dihya : génération de sitemap dynamique, robots.txt, logs structurés, balises meta, accessibilité, internationalisation, etc.

## Objectifs
- Vérifier l’optimisation SEO sur toutes les routes REST/GraphQL.
- Tester la génération dynamique des fichiers SEO (robots.txt, sitemap.xml).
- Valider la compatibilité multi-langues et multi-tenants.
- Couvrir la conformité RGPD et l’auditabilité des logs SEO.

## Structure
- `test_seo_django.py` : tests automatisés (unitaires, intégration, e2e, mocks, fixtures).

## Exécution
```bash
pytest --tb=short -v test_seo_django.py
```

## Documentation
Chaque test est documenté (docstring, type hints) et suit les standards Dihya (SEO, accessibilité, audit, i18n).

---

# SEO – Integration Tests (EN)

This folder contains all integration tests for Dihya's backend SEO features. See above for details.
