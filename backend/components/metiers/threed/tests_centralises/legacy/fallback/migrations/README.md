# README – Tests ultra avancés pour legacy/fallback/migrations

Ce dossier est destiné à accueillir tous les tests unitaires, d’intégration et de conformité pour legacy/fallback/migrations (JS & Python).
- Respecte la logique métier, la structure modulaire et le cahier des charges Dihya.
- Synchronisation JS/Python, documentation automatique, auditabilité CI/CD.

# legacy/fallback/migrations

## Structure et logique
Ce dossier contient les tests ultra avancés pour les migrations fallback legacy. Il assure la parité JS/Python, l’auto-discovery, et l’intégration CI/CD.

- Découverte automatique via `__init__.js` et `__init__.py`
- Tests synchronisés JS (`legacy_migration.test.js`) et Python (`legacy_migration.test.py`)
- Documentation et structure clé en main

## Exécution
- **JS** : Utiliser `npm test` ou exécuter via l’`index.js` parent
- **Python** : `pytest`

## CI/CD
- Intégration complète dans les pipelines existants
- Synchronisation automatique JS/Python
