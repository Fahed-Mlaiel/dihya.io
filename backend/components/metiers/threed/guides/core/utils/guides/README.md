# utils/guides

Guides d’utilisation avancée des utilitaires 3D pour Threed (JS & Python).

## Structure ultra avancée
- `guide_utils.py` / `guide_utils.js` : guides d’utilisation, patterns, bonnes pratiques, tests
- `__init__.py` / `__init__.js` : points d’entrée modulaires synchronisés
- `__init__.test.py` / `__init__.test.js` : tests d’import des points d’entrée
- `guide_utils.test.py` / `guide_utils.test.js` : tests unitaires
- `guide_utils_advanced.md` : documentation avancée

## Exemples d’utilisation
Voir les fichiers guides pour des exemples de deep clone, formatage, validation, etc.

## Conformité & CI/CD
- 100% testé (unitaires, import, audit)
- Prêt pour audit, documentation automatique, CI/CD
- Synchronisation stricte JS/Python

## Bonnes pratiques
- Utiliser les points d’entrée (`__init__`) pour importer les guides utilitaires
- Respecter la structure modulaire pour faciliter la maintenance, l’audit et la documentation
- Mettre à jour la documentation à chaque évolution majeure
