# README.md – Documentation avancée des fixtures et mocks Threed

## Objectif
Ce dossier fournit des fixtures et mocks avancés, prêts à l'emploi, pour garantir la conformité RGPD, la modularité, la réutilisabilité et la robustesse des tests métiers 3D.

## Structure
- `fixtures.js` / `fixtures.py` : Générateurs de données métiers (assets 3D, services, utilisateurs, etc.) paramétrables.
- `services_environnement.js` / `services_environnement.py` : Liste de services d'environnement enrichis (statut, conformité, audit, etc.).
- `*.test.js` / `*.test.py` : Tests unitaires et d'intégration, validant la structure, la conformité et la logique métier.

## Bonnes pratiques
- Respect strict du cahier des charges (modularité, conformité, testabilité, documentation).
- Ajoutez vos propres fixtures en respectant la structure et la documentation.
- Tous les ajouts doivent être testés et documentés.

## Exemples d'utilisation
```js
const { sample3DAsset, sampleService } = require('./fixtures');
const services = require('./services_environnement');
```

```python
from .fixtures import sample_3d_asset, sample_service
from .services_environnement import services
```

## Conformité
- RGPD, audit, modularité, extensibilité, multilingue.
- 100% open source, documentation claire, tests > 90% sur le cœur métier.
