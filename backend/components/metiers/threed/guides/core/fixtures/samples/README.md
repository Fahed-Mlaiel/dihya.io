# guides/core/fixtures/samples

Ce dossier contient les fixtures d’exemple pour les guides fixtures (JS & Python).

## Structure
- `sample_fixture.py` : Fixture d’exemple Python (sample_fixture_guide)
- `sample_fixture.js` : Fixture d’exemple JS (sample)
- `sample_fixture.test.py` / `sample_fixture.test.js` : Tests unitaires
- `__init__.py` / `__init__.js` : Points d’entrée globaux pour import direct
- `__init__.test.py` / `__init__.test.js` : Tests d’import et de structure

## Exemples d’utilisation

### Python
```python
from .sample_fixture import sample_fixture_guide
sample = sample_fixture_guide
```

### JavaScript
```js
const { sample } = require('./sample_fixture');
```

## Documentation avancée & intégration
- Synchronisation JS/Python : chaque fixture d’exemple est disponible dans les deux langages.
- Documentation automatique compatible Sphinx, JSDoc, auditabilité CI/CD.
- Tests unitaires et d’intégration présents pour chaque fixture et point d’entrée.
- Liens vers les guides globaux : [README_ULTRA.md](../../../../../README_ULTRA.md)

## Conformité
- Respecte la logique métier 3D avancée et le cahier des charges
- Compatible avec la documentation automatique, les tests et l’audit
- Prêt pour l’industrialisation, la CI/CD et l’évolution du projet

---

> **Bonnes pratiques** : Toujours utiliser les points d’entrée (`__init__`, `sample_fixture`) pour garantir la compatibilité, la traçabilité et la documentation automatique. Documenter chaque extension, synchroniser les évolutions JS/Python, et valider la conformité RGPD/accessibilité à chaque mise à jour.
