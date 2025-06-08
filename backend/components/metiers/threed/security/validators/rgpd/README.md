# rgpd/

Ce dossier contient les validateurs relatifs à la conformité RGPD.

- `rgpd_validator.js` : Validateur RGPD côté Node.js
- `rgpd_validator.py` : Validateur RGPD côté Python
- `__init__.js`, `__init__.py` : points d’entrée
- `.keep` : versionnement du dossier

## Bonnes pratiques
- Centraliser toute la logique de validation RGPD ici.
- Ajouter des tests unitaires pour chaque validateur.
