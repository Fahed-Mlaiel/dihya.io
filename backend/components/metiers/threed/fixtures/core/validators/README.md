# helpers/validators

Ce dossier contient les helpers de validation ultra avancés pour les fixtures Threed (JS & Python).

## Fichiers principaux
- `fixtures_validator.py` : Fonctions de validation Python (is_valid_3d_model, is_valid_user)
- `fixtures_validator.js` : Fonctions de validation JS (isValid3DModel, isValidUser)
- `__init__.py` / `__init__.js` : Points d’entrée pour import direct
- `__init__.test.py` / `__init__.test.js` : Tests d’import et de structure

## Exemples d’utilisation synchronisés

### Python
```python
from .fixtures_validator import is_valid_3d_model, is_valid_user
```

### JavaScript
```js
const { isValid3DModel, isValidUser } = require('./fixtures_validator');
```

## Conformité & audit
- Respecte la logique métier 3D avancée
- Compatible avec les outils de test, audit, CI/CD
- Prêt pour la documentation automatique
- Conforme RGPD, accessibilité, auditabilité

## Bonnes pratiques
- Utiliser les points d’entrée pour importer les validateurs
- Maintenir la synchronisation JS/Python
- Ajouter des tests et documenter chaque évolution
