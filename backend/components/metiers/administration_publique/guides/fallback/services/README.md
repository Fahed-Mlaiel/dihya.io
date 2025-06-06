# README – services (guides/fallback/services)

Ce dossier regroupe les fallback métiers ultra avancés pour les services : guides, helpers, edge cases, synchronisation JS/Python, conformité RGPD, audit, CI/CD.

- Fallbacks synchronisés JS/Python
- Exemples d’utilisation, edge cases, auditabilité
- Points d’entrée (`__init__.py`, `__init__.js`)
- Tests d’import et de conformité

## Exemples d’utilisation

### Python
```python
from .fallback_services import fallback_services
```

### JavaScript
```js
const { fallbackServices } = require('./fallback_services');
```
