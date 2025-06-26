# Services métier threed

Ce dossier contient la logique métier (Python & JS) pour la gestion des assets threed.

## Python
- `threed_asset_service.py` : CRUD complet, transactionnel, typé

## Node.js
- `threed_asset_service.js` : CRUD complet, transactionnel

## Convention
- Tous les services sont importés via `__init__.py`.
- Séparation stricte entre logique métier et accès aux données.

# Tests avancés des services threed

Ce dossier contient des tests automatisés pour les services métier :
- Exécution de services critiques
- Vérification du statut

Scripts :
- test_services.js (Node.js)
- test_services.py (Python)
