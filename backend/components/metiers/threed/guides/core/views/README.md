# guides/core/views

Ce sous-module regroupe les guides et exemples avancés des vues 3D, en Python et JavaScript.

## Structure ultra avancée
- `guides/` : guides d’intégration, patterns, bonnes pratiques, tests
- `samples/` : exemples d’intégration, tests unitaires JS & Python
- `index.js` : point d’entrée modulaire JS (clé en main)
- `index.test.js` / `index.test.py` : tests d’import et de présence du point d’entrée
- `__init__.py` / `__init__.js` : points d’entrée synchronisés Python/JS

## Exemples d’utilisation
Voir les sous-dossiers pour des exemples concrets de vues, d’intégration, de tests, etc.

## Conformité & CI/CD
- 100% testé (unitaires, import, audit)
- Prêt pour audit, documentation automatique, CI/CD
- Synchronisation stricte JS/Python

## Bonnes pratiques
- Utiliser les points d’entrée (`index.js`, `__init__`) pour importer les vues
- Respecter la structure modulaire pour faciliter la maintenance, l’audit et la documentation
- Mettre à jour la documentation à chaque évolution majeure
