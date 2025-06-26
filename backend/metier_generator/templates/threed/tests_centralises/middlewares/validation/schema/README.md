# Tests du middleware de schéma threed

Ce dossier contient les tests unitaires pour le middleware de validation de schéma du module threed.

## Node.js (Jest)
- `test_threed_schema.js` : Teste le middleware Express `threedSchema` (appel de `validate`, gestion des cas sans schéma).

## Python (pytest)
- `test_threed_schema.py` : Teste la fonction `validate_schema` (appel de `schema.validate`, gestion des cas sans schéma).

## Exécution

### Node.js
```bash
npx jest test_threed_schema.js
```

### Python
```bash
pytest test_threed_schema.py
```
