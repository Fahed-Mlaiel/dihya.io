# Tests du middleware d'input threed

Ce dossier contient les tests unitaires pour le middleware de validation d'entrée (input) du module threed.

## Node.js (Jest)
- `test_threed_input.js` : Teste le middleware Express `threedInput` (présence de `req.body`, gestion des erreurs).

## Python (pytest)
- `test_threed_input.py` : Teste la fonction `validate_input` (présence de données dans `request.data`, gestion des exceptions).

## Exécution

### Node.js
```bash
npx jest test_threed_input.js
```

### Python
```bash
pytest test_threed_input.py
```
