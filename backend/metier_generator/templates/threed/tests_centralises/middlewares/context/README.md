# Middleware de gestion de contexte threed

Ce dossier contient les middlewares de gestion de contexte (session, utilisateur, trace, etc.) pour le module threed.

- Python et JS, prêts à l’emploi.
- Extensibles selon les besoins métier.

# Tests des middlewares de contexte threed

Ce dossier regroupe tous les tests pour les middlewares de contexte du module threed, organisés en deux sous-dossiers :

- `session/` : tests des middlewares de gestion de session
- `trace/` : tests des middlewares de traçabilité

## Utilisation Node.js

```js
const contextTests = require('./context');
contextTests.testSession(...);
contextTests.testTrace(...);
```

## Utilisation Python

Voir les README dans `session/` et `trace/` pour les exemples Python.

## Structure

- `index.js` : point d'entrée clé en main pour tous les tests JS
- `__init__.js` : point d'entrée global JS (équivalent Node.js)
- `session/` et `trace/` : chaque sous-dossier contient ses propres tests, README et __init__
