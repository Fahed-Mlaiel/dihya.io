# guides/core/fixtures

Ce dossier est structuré selon la logique métier et le cahier des charges Dihya :

## Structure
- `guides/` : guides métier sur les fixtures (guide_fixtures.js, guide_fixtures.py, tests, points d’entrée `__init__`)
- `samples/` : fixtures d’exemple (sample_fixture.js, sample_fixture.py, tests, points d’entrée `__init__`)
- `__init__.py` / `__init__.js` : points d’entrée globaux Python/JS (import/export de tous les sous-modules critiques)
- `index.js` : point d’entrée global JS (clé en main, pour Node.js/ESM)
- `__init__.test.py` / `__init__.test.js` : tests d’import et de structure pour chaque point d’entrée
- `index.test.js` / `index.test.py` : tests d’intégration pour l’entrée JS globale
- `README.md` : documentation d’ensemble

## Points d’entrée et intégration
- Tous les sous-modules sont importables via les points d’entrée (`__init__`, `index.js`).
- Les tests garantissent la conformité, la traçabilité et la compatibilité CI/CD.

## Exemples d’utilisation

### Python
```python
from backend.components.metiers.threed.guides.core.fixtures import guides, samples
```

### JavaScript
```js
const fixtures = require('./__init__.js');
const all = require('./index.js');
// fixtures.guides, fixtures.samples
```

## Documentation avancée & intégration
- Synchronisation JS/Python : chaque guide et fixture d’exemple est disponible dans les deux langages.
- Documentation automatique compatible Sphinx, JSDoc, auditabilité CI/CD.
- Tests unitaires et d’intégration présents pour chaque point d’entrée et sous-module.
- Liens vers les guides globaux : [README_ULTRA.md](../../../../../README_ULTRA.md)

## Conformité
- Respecte la logique métier 3D avancée et le cahier des charges
- Compatible avec la documentation automatique, les tests et l’audit
- Prêt pour l’industrialisation, la CI/CD et l’évolution du projet

---

> **Bonnes pratiques** : Toujours utiliser les points d’entrée (`__init__`, `index.js`) pour garantir la compatibilité, la traçabilité et la documentation automatique. Documenter chaque extension, synchroniser les évolutions JS/Python, et valider la conformité RGPD/accessibilité à chaque mise à jour.
