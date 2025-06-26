# API threed

Ce dossier expose les routes REST du métier threed.

## Exemple d’utilisation (FastAPI)
```python
from fastapi import FastAPI
from .threed_asset_routes import router as threed_router

app = FastAPI()
app.include_router(threed_router, prefix="/threed")
```

## Exemple d’utilisation (Express.js)
```js
const express = require('express');
const initThreedAsset = require('../models/threed_asset');
const threedAssetRoutes = require('./threed_asset_routes');

const app = express();
const ThreedAsset = initThreedAsset(sequelize);
app.use('/threed', threedAssetRoutes(ThreedAsset));
```

# Tests API threed

Ce dossier contient les tests centralisés pour l’API threed (Python & JS).
- Inclut tous les sous-dossiers (routes, controllers, middlewares, etc.).
- Ultra avancé, clé en main.
