# Tests – Django 3D API

Ce fichier documente la stratégie de tests pour les endpoints, serializers, logs, templates, etc.

## Types de tests
- Tests unitaires (endpoints, serializers, permissions, i18n)
- Tests d’intégration (audit, RGPD, logs, edge cases)
- Tests multilingues (fr, en, ar, tzm)

## Lancement
- Utiliser `pytest` ou `python manage.py test`

## Couverture & CI/CD
- 100% des endpoints, plugins, policies, logs, audit, RGPD, accessibilité, multilingue, multitenant, fallback IA
- Tests automatisés exécutés à chaque build (voir `.github/workflows/test.yml`)
- Badge de couverture et conformité généré automatiquement

## Exemples avancés
- Voir `EXAMPLES_ADVANCED.md` pour des cas d’usage, edge cases, plugins, multilingue, audit, RGPD, accessibilité, e2e

## Accessibilité & auditabilité
- Tous les tests vérifient l’accessibilité (a11y), la conformité RGPD, l’audit logging, la souveraineté

## Plugins & extension
- Les tests couvrent aussi l’ajout/suppression dynamique de plugins, l’extension des policies, la gestion multitenant

---

> Pour toute contribution, voir `CONTRIBUTING.md`, `PLUGINS_GUIDE.md`, badge CI/CD, dashboard global.
