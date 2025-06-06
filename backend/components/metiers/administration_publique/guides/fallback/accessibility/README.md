# README – accessibility (guides/fallback/accessibility)

Ce dossier regroupe les fallback métiers ultra avancés pour l’accessibilité : guides, helpers, edge cases, synchronisation JS/Python, conformité RGPD, audit, CI/CD.

- Fallbacks synchronisés JS/Python
- Exemples d’utilisation, edge cases, auditabilité
- Points d’entrée (`__init__.py`, `__init__.js`)
- Tests d’import et de conformité

## Exemples d’utilisation

### Python
```python
from .fallback_accessibility import fallback_accessibility
```

### JavaScript
```js
const { fallbackAccessibility } = require('./fallback_accessibility');
```

## Bonnes pratiques
- Utiliser les points d’entrée pour importer les helpers
- Ajouter des tests pour chaque fallback ou extension
- Documenter chaque cas métier, edge case, conformité RGPD/accessibilité
