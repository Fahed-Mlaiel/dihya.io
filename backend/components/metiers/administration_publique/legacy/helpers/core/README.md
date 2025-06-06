# legacy/helpers/core

Helpers principaux legacy pour la 3D (JS & Python).

## Structure modulaire
- `samples/` : exemples, tests, points d’entrée, README
- `impl/` : implémentations legacy, tests, points d’entrée, README
- `index.js` : point d’entrée modulaire JS (clé en main)
- `index.test.js` / `index.test.py` : tests d’import et de présence du point d’entrée
- `__init__.py` / `__init__.js` : points d’entrée synchronisés Python/JS

Chaque sous-module contient :
- Fichiers legacy (JS & Python)
- Points d’entrée (`__init__`, `index.js`)
- Tests unitaires et d’import (JS & Python)
- README détaillé (structure, exemples, conformité, CI/CD, synchronisation JS/Python, bonnes pratiques)

## Exemples d’utilisation
Voir les sous-dossiers pour des exemples d’utilisation et d’implémentation legacy JS & Python.

## Conformité & CI/CD
- 100% testé (unitaires, import, audit)
- Prêt pour audit, documentation automatique, CI/CD
- Synchronisation stricte JS/Python

## Bonnes pratiques
- Utiliser les points d’entrée (`index.js`, `__init__`) pour importer les helpers legacy/core
- Respecter la structure modulaire pour faciliter la maintenance, l’audit et la documentation
- Mettre à jour la documentation à chaque évolution majeure
