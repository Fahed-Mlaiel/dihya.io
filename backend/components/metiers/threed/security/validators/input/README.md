# input/

Ce dossier contient les validateurs relatifs à la validation des entrées utilisateur (input).

- `input_validator.js` : Validateur d’input côté Node.js
- `input_validator.py` : Validateur d’input côté Python
- `__init__.js`, `__init__.py` : points d’entrée
- `.keep` : versionnement du dossier

## Bonnes pratiques
- Centraliser toute la logique de validation d’input ici.
- Ajouter des tests unitaires pour chaque validateur.
