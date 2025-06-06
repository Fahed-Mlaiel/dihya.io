# guides/core/accessibility

Ce dossier contient les guides d’accessibilité ultra avancés pour le module Threed (JS & Python).

## Structure
- `guides/` : guides d’accessibilité (guide_accessibility.py, guide_accessibility.js)
- `samples/` : fixtures d’exemple pour l’accessibilité (sample_fixture.py, sample_fixture.js)
- `tests/` : tous les tests unitaires JS & Python (fixtures, guides, init)
- `__init__.py` / `__init__.js` : points d’entrée pour import direct

## Exemples d’utilisation

### Python
```python
from .guides import guide_accessibility
from .samples import sample_accessibility_guide
# Utilisation :
guide = guide_accessibility.get_accessibility_guide()
sample = sample_accessibility_guide
```

### JavaScript
```js
const { getAccessibilityGuide } = require('./guides/guide_accessibility');
const { sample } = require('./samples/sample_fixture');
// Utilisation :
const guide = getAccessibilityGuide();
```

## Documentation avancée & intégration
- Synchronisation JS/Python : chaque guide et fixture est disponible dans les deux langages.
- Documentation automatique compatible Sphinx, JSDoc, DocGen, auditabilité CI/CD.
- Tous les points d’entrée sont testés (voir `index.test.js`, `__init__.test.py`).
- Exemples d’intégration dans les tests unitaires et d’intégration.
- Liens vers les guides : [ACCESSIBILITY_GUIDE.md](../../../ACCESSIBILITY_GUIDE.md), [README_ULTRA.md](../../../../../README_ULTRA.md)

## Conformité
- Respecte la logique métier 3D avancée et le cahier des charges
- Compatible avec la documentation automatique, les tests et l’audit
- Prêt pour l’industrialisation, la CI/CD et l’évolution du projet

---

> **Bonnes pratiques** : Toujours utiliser les points d’entrée (`__init__`, `index.js`) pour garantir la compatibilité et la traçabilité. Documenter chaque extension, synchroniser les évolutions JS/Python, et valider la conformité RGPD/accessibilité à chaque mise à jour.
