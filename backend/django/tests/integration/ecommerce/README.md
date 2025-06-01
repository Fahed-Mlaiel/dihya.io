# Tests d'intégration pour le secteur E-commerce

Ce dossier contient les tests d'intégration avancés pour les routes, modèles et plugins liés à la gestion de projets e-commerce dans Dihya.

## Structure
- `test_ecommerce_django.py` : tests d'intégration Django (CRUD, sécurité, i18n, multitenancy, plugins, audit, SEO, RGPD, etc.)
- Fixtures et mocks pour données e-commerce.

## Exécution

```bash
pytest --ds=dihya.settings --tb=short -v Dihya/backend/django/tests/integration/ecommerce/
```

## Multilingue
- Documentation et assertions en français, anglais, arabe, amazigh, allemand, chinois, japonais, coréen, néerlandais, hébreu, persan, hindi, espagnol.

## Sécurité
- JWT, CORS, WAF, anti-DDOS, audit log, anonymisation RGPD.

## Extensibilité
- Ajout de nouveaux tests via plugins ou API.

---

# Integration tests for the E-commerce sector

This folder contains advanced integration tests for routes, models, and plugins related to e-commerce project management in Dihya.

(See above for details in French)
