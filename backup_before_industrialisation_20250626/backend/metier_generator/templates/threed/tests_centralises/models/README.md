# Modèles métier threed

Ce dossier contient les modèles de données Python et JS pour la gestion des assets threed.

## Python
- `threed_asset.py` : Modèle SQLAlchemy complet, prêt à l’emploi

## Node.js
- `threed_asset.js` : Modèle Sequelize, prêt à l’emploi

## Convention
- Tous les modèles sont documentés, typés, extensibles.
- Importés automatiquement via `__init__.py`.

# Tests des modèles threed

Ce dossier contient les tests avancés pour les modèles métier threed.

## Scripts présents
- `test_models.py` : Tests unitaires et d’intégration des modèles Python (User, Project, Permission).
- `test_models.js` : Tests unitaires et d’intégration des modèles Node.js (User, Project, Permission).

## Initialisation
- `__init__.py` et `__init__.js` exposent les modules de tests pour importation et exécution centralisée.
