# Tests – Dihya Backend Storage

Ce fichier documente la stratégie de tests pour le module Storage.

## Types de tests
- Tests unitaires (upload, backup, purge, logs)
- Tests d’intégration (import/export, audit, RGPD)
- Tests de conformité RGPD, accessibilité, souveraineté

## Lancement
- Utiliser `pytest` pour Python, `jest` pour Node.js
- Couverture minimale : 95% sur les modules critiques

## Références
- Voir `uploads/`, `backups/`, `logs/`, `temp/`, `../../scripts/`
