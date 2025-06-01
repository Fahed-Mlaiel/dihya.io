# Tests – Dihya Backend DB

Ce fichier documente la stratégie de tests pour le module DB.

## Types de tests
- Tests unitaires (schéma, sécurité, performance, migration, multilingue)
- Tests d’intégration (import/export, migration, audit)
- Tests de conformité RGPD, accessibilité, souveraineté

## Lancement
- Utiliser `pytest` pour Python
- Couverture minimale : 95% sur les modules critiques

## Références
- Voir `tests/`, `fixtures_example.json`, `migrations/`, `database_schema.sql`
