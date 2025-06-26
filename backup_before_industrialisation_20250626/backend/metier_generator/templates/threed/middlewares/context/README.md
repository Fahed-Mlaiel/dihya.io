# Middlewares de contexte pour threed

Ce dossier regroupe tous les middlewares de gestion de contexte pour le module threed, organisés en deux sous-dossiers :

- `session/` : middlewares de gestion de session (stockage, récupération, etc.)
- `trace/` : middlewares de traçabilité (logs, suivi de requêtes, etc.)

## Utilisation Node.js

```js
const context = require('./context');
app.use(context.threedSession);   // Middleware de session
app.use(context.threedTrace);     // Middleware de traçabilité
```

## Utilisation Python

Voir les README dans `session/` et `trace/` pour les exemples Python.

## Structure

- `index.js` : point d'entrée clé en main pour tous les middlewares JS
- `__init__.js` : point d'entrée global JS (équivalent Node.js)
- `session/` et `trace/` : chaque sous-dossier contient ses propres middlewares, README et __init__
