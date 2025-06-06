# guides/core/plugins

Ce dossier est structuré selon la logique métier et le cahier des charges Dihya :

## Structure
- `guides/` : guides métier sur les plugins (guide_plugins.js, guide_plugins.py, tests, points d’entrée `__init__`, `index.js`)
- `README.md` : documentation d’ensemble

## Points d’entrée et intégration
- Tous les sous-modules sont importables via les points d’entrée (`__init__`, `index.js`) dans `guides/`.
- Les tests garantissent la conformité, la traçabilité et la compatibilité CI/CD.

## Exemples d’utilisation

### Python
```python
from .guides import get_plugins_guide
```

### JavaScript
```js
const { getPluginsGuide } = require('./guides');
```

## Documentation avancée & intégration
- Synchronisation JS/Python : chaque guide est disponible dans les deux langages.
- Documentation automatique compatible Sphinx, JSDoc, auditabilité CI/CD.
- Tests unitaires et d’intégration présents pour chaque point d’entrée et sous-module.
- Liens vers les guides globaux : [README_ULTRA.md](../../../../../README_ULTRA.md)

## Conformité
- Respecte la logique métier 3D avancée et le cahier des charges
- Compatible avec la documentation automatique, les tests et l’audit
- Prêt pour l’industrialisation, la CI/CD et l’évolution du projet

---

> **Bonnes pratiques** : Toujours utiliser les points d’entrée (`__init__`, `index.js`) pour garantir la compatibilité, la traçabilité et la documentation automatique. Documenter chaque extension, synchroniser les évolutions JS/Python, et valider la conformité RGPD/accessibilité à chaque mise à jour.
