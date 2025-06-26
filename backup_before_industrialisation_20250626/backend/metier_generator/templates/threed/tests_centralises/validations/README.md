# Validations métier threed

Ce dossier contient les règles de validation Python & JS pour les assets threed.

- RGPD, unicité, conformité, etc.
- Importées via `__init__.py`.
- Prêtes à l’emploi, extensibles.

# Tests centralisés des validations threed

Ce dossier contient les tests pour les validations threed (Python & JS).
- Ultra avancé, clé en main.

# Tests de validation d'asset threed

Ce dossier contient les tests unitaires pour la validation d'asset du module threed.

## Node.js (Jest)
- `test_threed_asset_validation.js` : Teste la fonction `validateAsset` (présence du nom, gestion des erreurs).

## Python (pytest)
- `test_threed_asset_validation.py` : Teste la fonction `validate_asset` (présence du nom, gestion des exceptions).

## Exécution

### Node.js
```bash
npx jest test_threed_asset_validation.js
```

### Python
```bash
pytest test_threed_asset_validation.py
```
