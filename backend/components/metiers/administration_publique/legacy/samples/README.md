# legacy/core/samples

Exemples et tests avancés pour le module legacy/core (JS & Python).

## Structure
- `sample_legacy.py` / `sample_legacy.js` : exemples d’utilisation legacy
- `sample_legacy.test.py` / `sample_legacy.test.js` : tests unitaires
- `__init__.py` / `__init__.js` : points d’entrée modulaires synchronisés
- `__init__.test.py` / `__init__.test.js` : tests d’import des points d’entrée

## Exemples d’utilisation
Voir les fichiers pour des exemples legacy JS & Python.

## Conformité & CI/CD
- 100% testé (unitaires, import, audit)
- Prêt pour audit, documentation automatique, CI/CD
- Synchronisation stricte JS/Python

## Bonnes pratiques
- Utiliser les points d’entrée (`__init__`) pour importer les exemples legacy
- Respecter la structure modulaire pour faciliter la maintenance, l’audit et la documentation
- Mettre à jour la documentation à chaque évolution majeure
