# README.md – Utilitaires ultra avancés (core)

Ce dossier contient des utilitaires ultra avancés, clé en main, pour les tests métiers 3D, respectant la modularité, la conformité RGPD, l’audit, la sécurité et la performance.

## Fonctions principales
- `generateId` / `generate_id` : Génération d’identifiants uniques avec préfixe.
- `deepClone` / `deep_clone` : Clonage profond d’objets/dictionnaires.
- `isValidEmail` / `is_valid_email` : Validation d’email conforme aux standards.
- `auditLog` / `audit_log` : Génération de logs d’audit structurés (action, user, meta, timestamp).

## Bonnes pratiques
- 100% testé (voir `core_utils.test.js` et `core_utils.test.py`)
- Utilisation dans tous les modules métiers pour garantir la robustesse et la conformité.
- Extensible pour d’autres utilitaires avancés (hash, sécurité, etc.)

## Exemples d’utilisation
```js
const { generateId, auditLog } = require('./core_utils');
const id = generateId('asset');
const log = auditLog('CREATE', 'user-001', { ip: '127.0.0.1' });
```

```python
from .core_utils import generate_id, audit_log
id = generate_id('asset')
log = audit_log('CREATE', 'user-001', {'ip': '127.0.0.1'})
```
