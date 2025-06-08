# migrations – Dihya Threed

## Objectif
Ce dossier centralise tous les outils, scripts et tests de migration pour le module Threed. Il respecte la logique métier, la structure modulaire, l’auto-discovery, la documentation automatique, l’intégration CI/CD, la synchronisation JS/Python, et le cahier des charges Dihya.

## Structure
- `migration_tools.js` : Outils de migration avancés (JS)
- `migration_tools.py` : Outils de migration avancés (Python)
- `__init__.js` et `__init__.py` : Initialisation et auto-découverte
- `index.js` : Exécution centralisée des migrations JS
- `tests/` : Tests ultra avancés, parité JS/Python, auto-discovery

## Exécution
- **JS** : `node index.js` ou via pipeline CI
- **Python** : `pytest` dans `tests/` ou via pipeline CI

## CI/CD
- Intégration complète dans les pipelines existants
- Synchronisation automatique JS/Python
- Documentation et auditabilité incluses
