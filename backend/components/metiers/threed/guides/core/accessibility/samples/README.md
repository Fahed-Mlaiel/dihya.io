# guides/core/accessibility/samples

Ce dossier contient les fixtures d’exemple (sample_fixture) pour l’accessibilité (JS & Python).

- `sample_fixture.py` : Fixture d’exemple Python (sample_accessibility_guide)
- `sample_fixture.js` : Fixture d’exemple JS (sample)
- `sample_fixture.test.py` / `sample_fixture.test.js` : Tests unitaires
- `__init__.py` / `__init__.js` : Points d’entrée pour import direct
- `__init__.test.py` / `__init__.test.js` : Tests d’import et de structure

## Exemples d’utilisation

### Python
```python
from .sample_fixture import sample_accessibility_guide
```

### JavaScript
```js
const { sample } = require('./sample_fixture');
```

## Conformité
- Respecte la logique métier 3D avancée
- Compatible avec les outils de test et d'intégration continue
- Prêt pour l'audit et la documentation automatique
