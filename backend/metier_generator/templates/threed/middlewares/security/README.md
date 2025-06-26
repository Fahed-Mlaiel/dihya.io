# Middlewares de sécurité pour threed

Ce dossier regroupe tous les middlewares de sécurité pour le module threed, organisés en deux sous-dossiers :

- `audit/` : middlewares d'audit (traçabilité, logs, etc.)
- `auth/` : middlewares d'authentification (contrôle d'accès, tokens, etc.)

## Utilisation Node.js

```js
const security = require('./security');
app.use(security.threedAudit);   // Middleware d'audit
app.use(security.threedAuth);    // Middleware d'authentification
```

## Utilisation Python

Voir les README dans `audit/` et `auth/` pour les exemples Python.

## Structure

- `index.js` : point d'entrée clé en main pour tous les middlewares JS
- `__init__.js` : point d'entrée global JS (équivalent Node.js)
- `audit/` et `auth/` : chaque sous-dossier contient ses propres middlewares, README et __init__
