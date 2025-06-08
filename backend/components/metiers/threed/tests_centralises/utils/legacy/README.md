# Tests Centralisés Legacy – Module Threed Utils

## Structure du dossier
- `core/`, `fallback/`, `helpers/`, `samples/` : sous-modules synchronisés avec `/utils/legacy`.
- `__init__.js`, `__init__.py` : initialisation, auto-discovery, synchronisation JS/Python.
- `index.js` : exécution centralisée des tests JS à la racine du module legacy.
- `.keep` : versionnement des dossiers vides.

## Exécution des tests
- JS : `npm test` ou via `index.js` (auto-import de tous les tests du module legacy).
- Python : `pytest` (pour la parité et la couverture croisée).

## CI/CD & Synchronisation
- Intégration continue avec scripts de test JS/Python.
- Synchronisation automatique de la structure avec `/utils/legacy`.
- Documentation et conventions à jour.

## Logique métier
- Tests exhaustifs des helpers, core, fallback, samples legacy JS.
- Respect des imports/exports modulaires, logique métier Threed.

## Imports/Exports
- Tous les tests sont auto-importés via `index.js`.
- Exports centralisés pour intégration CI/CD et reporting.

## Conventions
- Parité stricte JS/Python.
- Documentation à chaque niveau.
- Structure modulaire, évolutive, clé en main.
