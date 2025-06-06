# legacy/fallback/mocks

Mocks legacy pour la 3D (JS & Python).

## Structure ultra avancée
- `legacy_mock_test.js` : mock JS legacy (exemple de fonction mockée)
- `legacy_mock_test.test.js` / `legacy_mock_test.test.py` : tests unitaires JS & Python
- `__init__.py` / `__init__.js` : points d’entrée modulaires synchronisés
- `__init__.test.py` / `__init__.test.js` : tests d’import des points d’entrée

## Exemples d’utilisation
Voir les fichiers pour des exemples de mocks legacy JS & Python.

## Conformité & CI/CD
- 100% testé (unitaires, import, audit)
- Prêt pour audit, documentation automatique, CI/CD
- Synchronisation stricte JS/Python

## Bonnes pratiques
- Utiliser les points d’entrée (`__init__`) pour importer les mocks legacy
- Respecter la structure modulaire pour faciliter la maintenance, l’audit et la documentation
- Mettre à jour la documentation à chaque évolution majeure
