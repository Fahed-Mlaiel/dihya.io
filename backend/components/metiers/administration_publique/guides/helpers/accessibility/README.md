# README – accessibility (guides/helpers/accessibility)

Ce dossier regroupe les helpers ultra avancés pour l’accessibilité : guides, helpers, edge cases, synchronisation JS/Python, conformité RGPD, audit, CI/CD.

- Helpers synchronisés JS/Python
- Exemples d’utilisation, edge cases, auditabilité
- Points d’entrée (`__init__.py`, `__init__.js`)
- Tests d’import et de conformité

## Exemples d’utilisation

### Python
```python
from .helpers_accessibility import check_accessibility, audit_accessibility
```

### JavaScript
```js
const { checkAccessibility, auditAccessibility } = require('./helpers_accessibility');
```

## Bonnes pratiques
- Utiliser les points d’entrée pour importer les helpers
- Ajouter des tests pour chaque helper ou extension
- Documenter chaque cas métier, edge case, conformité RGPD/accessibilité
