# README – plugins (guides/helpers/plugins)

Ce dossier regroupe les helpers ultra avancés pour les plugins : helpers, edge cases, synchronisation JS/Python, conformité RGPD, audit, CI/CD.

- Helpers synchronisés JS/Python
- Exemples d’utilisation, edge cases, auditabilité
- Points d’entrée (`__init__.py`, `__init__.js`)
- Tests d’import et de conformité

## Exemples d’utilisation

### Python
```python
from .helpers_plugins import check_plugin, audit_plugin
```

### JavaScript
```js
const { checkPlugin, auditPlugin } = require('./helpers_plugins');
```

## Bonnes pratiques
- Utiliser les points d’entrée pour importer les helpers
- Ajouter des tests pour chaque helper ou extension
- Documenter chaque cas métier, edge case, conformité RGPD/accessibilité
