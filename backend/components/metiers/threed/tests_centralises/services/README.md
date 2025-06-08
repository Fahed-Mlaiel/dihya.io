# Tests centralisés Services – Threed

## Objectif
Ce module regroupe tous les tests ultra avancés pour les services du métier Threed, avec structure modulaire, synchronisation JS/Python, auto-discovery, documentation automatique, CI/CD, auditabilité, et respect du cahier des charges.

## Structure
- `core/` : Tests services cœur (ex: controllers)
- `fallback/` : Tests services fallback
- `helpers/` : Tests helpers services
- `samples/` : Tests sur jeux de données services
- `__init__.js` et `__init__.py` : Initialisation et auto-discovery JS/Python

## Exécution
- **JS** : `npm test` ou via pipeline CI
- **Python** : `pytest` ou via pipeline CI

## CI/CD
- Intégration complète dans les pipelines existants
- Synchronisation automatique JS/Python
- Documentation et auditabilité incluses
