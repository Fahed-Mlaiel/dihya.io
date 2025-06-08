# README – Tests ultra avancés pour guides/core/samples

Ce dossier regroupe tous les tests unitaires, d’intégration et de conformité pour guides/core/samples (JS & Python).

- Découverte automatique via `__init__.js` et `__init__.py`
- Exécution centralisée via `index.js`
- Synchronisation JS/Python, documentation automatique, CI/CD ready
- Respecte la logique métier et le cahier des charges Dihya

## Structure
- Tous les sous-dossiers doivent contenir des tests `.test.js` et `.test.py`.
- Les fichiers d’initialisation assurent l’auto-discovery et l’exécution centralisée.

## Exécution
- JS : utiliser l’index.js ou les runners de test (Jest, Mocha, etc.)
- Python : utiliser pytest ou un runner compatible.

## CI/CD
- Intégration continue prête à l’emploi, synchronisation JS/Python assurée.
