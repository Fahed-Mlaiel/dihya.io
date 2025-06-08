# README – Tests ultra avancés pour guides/core

Ce dossier regroupe tous les tests unitaires, d’intégration et de conformité pour guides/core (JS & Python).

- Découverte automatique via `__init__.js` et `__init__.py`
- Exécution centralisée via `index.js` (à créer si besoin)
- Synchronisation JS/Python, documentation automatique, CI/CD ready
- Respecte la logique métier et le cahier des charges Dihya

## Structure
- Tous les sous-dossiers doivent contenir des tests `.test.js` et `.test.py`.
- Les fichiers d’initialisation assurent l’auto-discovery et l’exécution centralisée.
- Les sous-modules : accessibility, fixtures, plugins, samples, services, utils, views

## Exécution
- JS : utiliser l’index.js ou les runners de test (Jest, Mocha, etc.)
- Python : utiliser pytest ou un runner compatible.

## CI/CD
- Intégration continue prête à l’emploi, synchronisation JS/Python assurée.
- Documentation générée automatiquement à chaque niveau.
