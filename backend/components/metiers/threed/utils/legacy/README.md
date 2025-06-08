# Module Legacy – Threed Utils

## Structure
- `core/`, `fallback/`, `helpers/`, `samples/` : sous-modules synchronisés avec les tests centralisés.
- `__init__.js`, `__init__.py` : initialisation, auto-discovery, synchronisation JS/Python.
- `index.js` : centralisation des exports legacy.
- `.keep` : versionnement des dossiers vides.

## Exécution & CI/CD
- Exécution modulaire, auto-discovery, intégration continue.
- Synchronisation automatique avec les tests centralisés.

## Logique métier
- Fonctions legacy, helpers, fallback, samples, routes, imports/exports modulaires.
- Respect strict du cahier des charges Threed.

## Conventions
- Documentation à chaque niveau.
- Structure modulaire, évolutive, clé en main.
