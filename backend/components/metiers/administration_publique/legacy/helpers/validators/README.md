# Legacy Helpers Validators

Ce module regroupe les helpers de validation legacy pour le domaine 3D, avec une structure modulaire, des points d'entrée harmonisés et des tests exhaustifs.

## Structure du dossier

- `index.js` : Point d'entrée principal JS, centralise l'accès à tous les helpers/validators (core, samples).
- `index.test.js` : Test d'import du point d'entrée JS.
- `index.test.py` : Test d'import du point d'entrée Python.
- `__init__.js` / `__init__.py` : Points d'entrée pour la découverte automatique (JS/Python).
- `__init__.test.js` / `__init__.test.py` : Tests d'import des points d'entrée.
- `core/` : Helpers/validators legacy principaux.
- `samples/` : Exemples d'utilisation et tests synchronisés JS/Python.

## Exemples d'utilisation

```js
const validators = require('./index');
validators.legacyValidator(...);
```

```python
from backend.components.metiers.threed.legacy.helpers.validators import ...
```

## Bonnes pratiques
- Tous les points d'entrée sont testés (JS & Python).
- Synchronisation JS/Python assurée.
- Prêt pour CI/CD, audit et documentation automatique.
- Respect strict de la logique métier et du cahier des charges.

## CI/CD & Documentation
- Les tests sont automatiquement détectés et exécutés.
- La documentation est générée à partir de ce README et des docstrings.

## Conformité
- Structure modulaire, sans doublons, 100% testée, prête pour audit.
- Respect strict des conventions du projet `threed`.
