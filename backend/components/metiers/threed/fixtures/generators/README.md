# Dossier generators (fixtures/core/generators)

Ce dossier regroupe tous les générateurs dynamiques de fixtures pour le module Threed, en Python et JavaScript. Il est structuré pour répondre aux exigences avancées du cahier des charges et garantir la maintenabilité, la robustesse et la parité JS/Python.

## Structure

- `fixtures.generator.js` : Générateur ultra avancé de modèles et d'utilisateurs 3D (JavaScript)
- `fixtures_generator.py` : Générateur ultra avancé de modèles et d'utilisateurs 3D (Python)
- `__init__.js` / `__init__.py` : Points d'entrée pour import direct des fonctions principales
- `fixtures.generator.test.js` / `fixtures_generator.test.py` : Tests unitaires avancés pour chaque générateur
- `__init__.test.js` / `__init__.test.py` : Tests d'import et de structure du sous-module

## Exemples d'utilisation

### JavaScript
```js
const { generateModel, generateUser } = require('./fixtures.generator');
const model = generateModel('UltraModel', 12, 20);
const user = generateUser('superadmin');
```

### Python
```python
from .fixtures_generator import generate_model, generate_user
model = generate_model('UltraModel', 12, 20)
user = generate_user('superadmin')
```

## Tests
Tous les tests sont présents et validés (voir fichiers `.test.js` et `.test.py`).

## Conformité
- Respecte la logique métier 3D avancée
- Compatible avec les outils de test et d'intégration continue
- Prêt pour l'audit et la documentation automatique
