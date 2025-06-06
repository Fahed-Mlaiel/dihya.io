# core – Plugins (clé en main, ultra avancé)

Ce dossier contient la logique métier principale du module plugins :

- `pluginManager.js` / `pluginManager.py` : gestionnaire de plugins (JS/Python)
- `pluginManager.test.js` / `pluginManager.test.py` : tests unitaires associés
- `__init__.js` / `__init__.py` : points d’entrée modulaires (synchronisation, conformité, CI/CD)
- `__init__.test.js` / `__init__.test.py` : tests d’import et d’intégration (audit, conformité)
- `sample_plugin.js` / `sample_plugin.py` : exemple de plugin (si besoin)
- `sample_plugin.test.js` / `sample_plugin.test.py` : tests unitaires plugin exemple

## Bonnes pratiques
- Garder ce dossier centré sur le cœur métier (pas de helpers ici)
- Synchroniser JS/Python (API, logique, tests)
- Ajouter un README par logique complexe si besoin
- Documenter chaque ajout pour l’audit, la CI/CD et la traçabilité
- Utiliser les points d’entrée `__init__` pour garantir la conformité et l’intégration continue

---

> Ce dossier est la référence pour la logique métier du module plugins. Toute extension doit respecter la structure, la synchronisation JS/Python et la conformité métier.
