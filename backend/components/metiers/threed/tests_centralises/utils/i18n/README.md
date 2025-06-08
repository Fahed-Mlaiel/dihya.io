# i18n – Utils

Tests ultra avancés pour les utilitaires i18n du module Threed.

- Parité JS/Python à chaque niveau (core, fallback, helpers, samples)
- Découverte automatique des tests via `__init__.js`, `__init__.py`, `index.js`
- Exécution centralisée des tests JS (index.js) et Python (pytest)
- Prêt pour CI/CD, documentation automatique, structure modulaire exhaustive

## Structure
- `core/` : logique i18n principale
- `fallback/` : gestion des cas de repli i18n
- `helpers/` : helpers i18n
- `samples/` : jeux de données/tests i18n

## Exécution
- **JS** : `npm test` ou exécution via Jest/Mocha
- **Python** : `pytest`

## CI/CD
- Intégration directe dans les pipelines (GitHub Actions, GitLab CI, etc.)
- Génération automatique de rapports JS/Python

## Logique métier
- Respect du cahier des charges, structure modulaire, imports/exports, documentation à chaque sous-niveau
