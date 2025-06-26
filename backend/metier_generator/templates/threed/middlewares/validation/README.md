# Middlewares de validation pour threed

Ce dossier regroupe tous les middlewares de validation pour le module threed, organisés en deux sous-dossiers :

- `input/` : middlewares de validation d'entrée (présence et format des données)
- `schema/` : middlewares de validation de schéma (validation avancée via un schéma)

## Utilisation Node.js

```js
const validation = require('./validation');
app.use(validation.threedInput);   // Middleware d'entrée
app.use(validation.threedSchema);  // Middleware de schéma
```

## Utilisation Python

Voir les README dans `input/` et `schema/` pour les exemples Python.

## Structure

- `index.js` : point d'entrée clé en main pour tous les middlewares JS
- `__init__.js` : point d'entrée global JS (équivalent Node.js)
- `input/` et `schema/` : chaque sous-dossier contient ses propres middlewares, README et __init__
