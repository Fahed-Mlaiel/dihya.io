# core/README.md

Ce dossier contient la logique métier principale RBAC :
- `rbac_core.js` / `rbac_core.py` : gestion des rôles, permissions, policies
- `rbac_core.test.js` / `rbac_core.test.py` : tests unitaires
- `__init__.js` / `__init__.py` : points d’entrée
- `__init__.test.js` / `__init__.test.py` : tests d’import

Bonnes pratiques :
- Synchroniser JS/Python
- Documenter chaque ajout
- Respecter la conformité, la CI/CD et l’audit
