# core – Logique métier principale (clé en main, ultra avancé)

Ce dossier contient la logique métier principale du module templates centralisés Threed :
- Fonctions robustes, testées, prêtes pour CI/CD, audit, documentation automatique
- Synchronisation JS/Python, conformité RGPD, accessibilité, auditabilité

## Structure
- `template_threed.js` / `template_threed.py` : logique métier templates
- `core_helpers.test.js` / `core_helpers.test.py` : tests unitaires
- `index.js`, `__init__.js`, `__init__.py` : points d’entrée modulaires, synchronisation, conformité

## Bonnes pratiques
- Garder ce dossier centré sur le cœur métier (pas de helpers ici)
- Typage, documentation, tests, robustesse, conformité, traçabilité
- Ajouter un README par logique complexe si besoin

## Extension
Pour toute extension, créez un fichier dédié par logique métier, ajoutez tests et documentation associés.
