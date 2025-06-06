# Sample Service – Core Services Threed

Ce dossier contient un exemple de service (sample) pour le module core services du domaine 3D. Il sert de référence pour l'intégration, la documentation, les tests et la conformité CI/CD.

## Structure du dossier

- `sample_service.js` : Exemple de service (JavaScript, clé en main, synchronisé).
- `sample_service.py` : Exemple de service (Python, clé en main, synchronisé).
- `sample_service.test.js` : Tests unitaires JS, CI/CD ready.
- `sample_service.test.py` : Tests unitaires Python, CI/CD ready.
- `__init__.js` / `__init__.py` : Points d'entrée du sous-module samples (import JS/Python, découverte automatique).
- `__init__.test.js` / `__init__.test.py` : Tests d'import des points d'entrée.
- `README.md` : Documentation métier, structure, conformité, exemples d’usage.

## Exemples d’utilisation

**JavaScript**
```js
const { SampleService } = require('./__init__');
const service = new SampleService({ mode: 'prod' });
service.init({ level: 1 });
const result = service.run('DATA');
```

**Python**
```python
from .sample_service import SampleService
service = SampleService(options={"mode": "prod"})
service.init({"level": 1})
result = service.run("DATA")
```

## Bonnes pratiques
- Un seul sample ultra avancé, sans doublon.
- Tous les points d'entrée sont testés (JS & Python).
- Synchronisation JS/Python assurée.
- Prêt pour CI/CD, audit et documentation automatique.
- Respect strict de la logique métier et du cahier des charges.

## CI/CD & Documentation
- Les tests sont automatiquement détectés et exécutés.
- La documentation de chaque sample est générée à partir de ce README et des docstrings.

## Conformité
- Structure modulaire, sans doublons, 100% testée, prête pour audit.
- Respect strict des conventions du projet `threed`.
