# README – plugins (guides/fallback/plugins)

Ce dossier regroupe les fallback métiers ultra avancés pour les plugins : guides, helpers, edge cases, synchronisation JS/Python, conformité RGPD, audit, CI/CD.

- Fallbacks synchronisés JS/Python
- Exemples d’utilisation, edge cases, auditabilité
- Points d’entrée (`__init__.py`, `__init__.js`)
- Tests d’import et de conformité

## Exemples d’utilisation

### Python
```python
from .fallback_plugins import fallback_plugins
```

### JavaScript
```js
const { fallbackPlugins } = require('./fallback_plugins');
```
