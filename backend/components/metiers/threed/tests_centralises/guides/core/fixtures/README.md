# README – Tests ultra avancés pour guides/core/fixtures

Ce dossier regroupe tous les tests unitaires, d’intégration et de conformité pour le module guides/core/fixtures (JS & Python).

- Respecte la logique métier, la structure modulaire et le cahier des charges Dihya.
- Synchronisation JS/Python, documentation automatique, auditabilité CI/CD.
- Découverte automatique des tests via `__init__.js` et `__init__.py`.
- Prêt à être intégré dans les pipelines CI/CD et la documentation globale.

## Structure
- Tous les sous-dossiers doivent contenir des tests `.test.js` et `.test.py`.
- Les fichiers d’initialisation assurent l’auto-discovery et l’exécution centralisée.

## Exécution
- JS : utiliser l’index.js ou les runners de test (Jest, Mocha, etc.)
- Python : utiliser pytest ou un runner compatible.

## CI/CD
- Intégration continue prête à l’emploi, synchronisation JS/Python assurée.
