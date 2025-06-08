# Tests centralisés RGPD – Threed

## Objectif
Ce module regroupe tous les tests ultra avancés pour la conformité RGPD du métier Threed, avec structure modulaire, synchronisation JS/Python, auto-discovery, documentation automatique, CI/CD, auditabilité, et respect du cahier des charges.

## Structure
- `core/` : Tests cœur RGPD
- `helpers/` : Tests helpers RGPD
- `samples/` : Tests sur jeux de données RGPD
- `tests/` : Suites de tests ultra avancées, parité JS/Python
- `index.js` : Exécution centralisée de tous les tests JS RGPD
- `__init__.js` et `__init__.py` : Initialisation et auto-discovery JS/Python

## Exécution
- **JS** : `npm test` ou via pipeline CI, ou via `index.js`
- **Python** : `pytest` ou via pipeline CI

## CI/CD
- Intégration complète dans les pipelines existants
- Synchronisation automatique JS/Python
- Documentation et auditabilité incluses
