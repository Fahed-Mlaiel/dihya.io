# Middlewares de schéma pour threed

Ce dossier contient les middlewares de validation de schéma pour le module threed.

## JavaScript
- `threed_schema.js` : Middleware Express pour valider le schéma via `req.schema.validate`.

## Python
- `threed_schema.py` : Fonction de validation pour appliquer `schema.validate` sur `request.data`.

## Utilisation rapide

### Node.js
```js
const { threedSchema } = require('./schema');
app.use(threedSchema);
```

### Python
```python
from .schema import validate_schema
validate_schema(request)
```
