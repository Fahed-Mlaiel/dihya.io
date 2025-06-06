# README - Tests Threed

Ce dossier contient tous les tests unitaires, d'intégration, e2e et de conformité pour le module Threed (3D).

## Python
- `test_utils.py` : Tests des utilitaires Python
- `test_api.py` : Tests de l'API Python
- `test_plugins.py` : Tests des plugins Python
- `test_services.py` : Tests des services Python
- `test_templates.py` : Tests des templates Python
- `test_fixtures.py` : Tests des fixtures Python
- `test_accessibility.py` : Tests d'accessibilité (a11y)
- `test_rgpd.py` : Tests RGPD (anonymisation, consentement)
- `test_security.py` : Tests de sécurité (RBAC, injection)
- `test_i18n.py` : Tests d'internationalisation
- `test_guides.py` : Tests de conformité des guides
- `test_legacy.py` : Tests de migration/legacy
- `test_threed.py` : Tests unitaires du modèle 3D

## JavaScript
- `test_utils.js` : Tests des utilitaires JS
- `test_api.js` : Tests de l'API JS
- `test_plugins.js` : Tests des plugins JS
- `test_services.js` : Tests des services JS
- `test_templates.js` : Tests des templates JS
- `test_fixtures.js` : Tests des fixtures JS
- `test_threed.js` : Tests unitaires du modèle 3D JS

## Intégration & e2e
- `index.test.js` : Tests d'intégration globaux JS

## Bonnes pratiques
- 100% de couverture, mocks, fixtures, CI/CD, rapports automatisés
- Respect RGPD, accessibilité, sécurité, souveraineté numérique, i18n, audit, etc.

## Nouvelle organisation professionnelle (2025)

- `api/` : tests API (JS & Python)
- `fixtures/` : tests sur les fixtures et mocks
- `guides/` : tests de conformité des guides et documentations
- `plugins/` : tests d’intégration et de fallback des plugins
- `rgpd/` : tests RGPD et conformité données
- `security/` : tests de sécurité, audit, accessibilité
- `services/` : tests des services métier (core, fallback, helpers)
- `templates/` : tests des templates Jinja2 et helpers associés
- `utils/` : tests des utilitaires, helpers, i18n, etc.
- `integration/` : tests d’intégration multi-modules (optionnel)
- `legacy/` : tests de compatibilité ou de migration (optionnel)

Chaque sous-dossier doit contenir :
- Un `README.md` expliquant la logique métier et la couverture de test
- Les tests unitaires et d’intégration JS & Python, nommés de façon explicite
- Les fixtures/mocks nécessaires

Les fichiers racine doivent être déplacés dans leur sous-dossier respectif, sans doublon, selon la logique métier ci-dessus.

---
Pour toute question, voir le README principal du module ou contacter l’équipe métier Threed.
