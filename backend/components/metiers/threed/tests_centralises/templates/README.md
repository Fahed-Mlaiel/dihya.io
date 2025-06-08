# README ULTRA AVANCÉ – TEMPLATES (tests_centralises)

Ce module regroupe tous les tests ultra avancés pour les templates du module métier Threed, avec parité JS/Python, auto-discovery, CI/CD, documentation automatique, structure modulaire exhaustive et logique métier complète.

## Structure
- `core/` : cœur métier des templates (helpers, logique, tests)
- `j2/` : templates Jinja2 (tests, helpers)
- `static/` : fichiers statiques liés aux templates (tests, helpers)
- `templates/` : tests sur les templates globaux (helpers, logique)
- `helpers/` : helpers transverses pour tous les templates (tests, utils, samples)

## Découverte automatique & CI/CD
- Tous les dossiers disposent de `__init__.js`, `__init__.py` et `index.js` pour l’auto-discovery JS/Python et l’intégration CI/CD.
- Exécution centralisée des tests JS via `index.js` à chaque niveau.
- Exécution centralisée des tests Python via `pytest`.

## Parité JS/Python
- Chaque helper, sample, test métier existe en version `.test.js` et `.test.py`.
- Les helpers, samples, etc. sont synchronisés pour garantir la parité et la couverture métier.

## Exécution
- **JS** : lancer `npm test` ou exécuter ce dossier avec Jest/Mocha.
- **Python** : lancer `pytest` à la racine ou dans ce dossier.

## CI/CD
- Prêt à l’intégration dans les pipelines CI/CD (GitHub Actions, GitLab CI, etc.).
- Génération automatique de rapports de tests JS/Python.

## Logique métier
- Respect strict du cahier des charges, des routes, imports/exports, structure modulaire, et logique métier Threed.
- Documentation automatique à chaque sous-niveau.
