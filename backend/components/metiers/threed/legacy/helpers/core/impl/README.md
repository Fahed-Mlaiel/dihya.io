# legacy/helpers/core/impl

Implémentations legacy helpers pour la 3D (JS & Python).

## Structure
- `legacy_helper.py` / `legacy_helper.js` : helpers legacy implémentation
- `legacy_helper.test.py` / `legacy_helper.test.js` : tests unitaires
- `__init__.py` / `__init__.js` : points d’entrée modulaires synchronisés
- `__init__.test.py` / `__init__.test.js` : tests d’import des points d’entrée

## Exemples d’utilisation
Voir les fichiers pour des exemples d’implémentation legacy JS & Python.

## Conformité & CI/CD
- 100% testé (unitaires, import, audit)
- Prêt pour audit, documentation automatique, CI/CD
- Synchronisation stricte JS/Python

## Bonnes pratiques
- Utiliser les points d’entrée (`__init__`) pour importer les implémentations legacy
- Respecter la structure modulaire pour faciliter la maintenance, l’audit et la documentation
- Mettre à jour la documentation à chaque évolution majeure
