# Tests avancés – Services Core

Ce dossier contient les tests ultra avancés pour le module métier `services/core` (JS & Python).

- Respecte la logique métier et le cahier des charges
- Prêt à être répliqué sur d’autres modules
- Parité complète JS/Python à chaque niveau
- Découverte automatique récursive (init, index.js)
- Intégration CI/CD prête à l’emploi
- Documentation automatique à chaque sous-niveau

## Structure des sous-dossiers
- `api/` : tests API métier
- `controllers/` : tests des contrôleurs
- `helpers/` : helpers et utilitaires de test
- `impl/` : implémentations métier
- `samples/` : jeux de données et cas d’usage

## Découverte automatique & CI/CD
- Les fichiers d'initialisation (__init__.js, __init__.py) permettent la découverte automatique des tests et l'intégration dans les pipelines CI/CD.
- Le fichier `index.js` exécute tous les tests JS du module et sous-modules.

## Exécution
- **JS** : lancer `npm test` ou exécuter ce dossier avec Jest/Mocha.
- **Python** : lancer `pytest` à la racine ou dans ce dossier.

## Synchronisation JS/Python
- Chaque test métier existe en version `.test.js` et `.test.py`.
- Les helpers, samples, etc. sont synchronisés pour garantir la parité et la couverture métier.

## Auto-discovery
- Les fichiers d’initialisation (__init__.js, __init__.py) et `index.js` assurent la découverte automatique des tests dans tous les sous-dossiers.

## CI/CD
- Prêt à l’intégration dans les pipelines CI/CD (GitHub Actions, GitLab CI, etc.).
- Génération automatique de rapports de tests JS/Python.
