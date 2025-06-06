# legacy/fallback/migrations

Migrations legacy pour la 3D (JS & Python).

## Structure
- `legacy_migration.py` / `legacy_migration.js` : scripts de migration legacy
- `legacy_migration.test.py` / `legacy_migration.test.js` : tests unitaires
- `__init__.py` / `__init__.js` : points d’entrée modulaires synchronisés
- `__init__.test.py` / `__init__.test.js` : tests d’import des points d’entrée

## Exemples d’utilisation
Voir les fichiers pour des exemples de migration legacy JS & Python.

## Conformité & CI/CD
- 100% testé (unitaires, import, audit)
- Prêt pour audit, documentation automatique, CI/CD
- Synchronisation stricte JS/Python

## Bonnes pratiques
- Utiliser les points d’entrée (`__init__`) pour importer les migrations legacy
- Respecter la structure modulaire pour faciliter la maintenance, l’audit et la documentation
- Mettre à jour la documentation à chaque évolution majeure
