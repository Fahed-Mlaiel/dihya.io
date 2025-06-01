# Tests d'intégration pour le secteur Journalisme

Ce dossier contient les tests d'intégration avancés pour les routes, modèles et plugins liés à la gestion de projets journalistiques dans Dihya.

## Structure
- `test_journalisme_django.py` : tests d'intégration Django (CRUD, sécurité, i18n, multitenancy, plugins, audit, SEO, RGPD, etc.)
- Fixtures et mocks pour données journalistiques.

## Exécution

```bash
pytest --ds=dihya.settings --tb=short -v Dihya/backend/django/tests/integration/journalisme/
```

## Multilingue
- Documentation et assertions en français, anglais, arabe, amazigh, allemand, chinois, japonais, coréen, néerlandais, hébreu, persan, hindi, espagnol.

## Sécurité
- JWT, CORS, WAF, anti-DDOS, audit log, anonymisation RGPD.

## Extensibilité
- Ajout de nouveaux tests via plugins ou API.

---

# Integration tests for the Journalism sector

This folder contains advanced integration tests for routes, models, and plugins related to journalism project management in Dihya.

(See above for details in French)
