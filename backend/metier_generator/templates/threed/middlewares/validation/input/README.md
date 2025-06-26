# Middlewares d'input pour threed

Ce dossier contient les middlewares de validation d'entrée pour le module threed.

## JavaScript
- `threed_input.js` : Middleware Express pour valider la présence de données dans `req.body`.

## Python
- `threed_input.py` : Fonction de validation pour vérifier la présence de données dans `request.data`.

## Utilisation rapide

### Node.js
```js
const { threedInput } = require('./input');
app.use(threedInput);
```

### Python
```python
from .input import validate_input
validate_input(request)
```
