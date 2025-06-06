# core

Ce dossier contient la logique métier principale du module d'export :
- `exporter.js` / `exporter.py` : logique métier d'export
- `exporter.test.js` / `exporter.test.py` : tests unitaires associés
- `__init__.js` / `__init__.py` : points d'entrée modulaires (JS & Python)
- `__init__.test.js` / `__init__.test.py` : tests d'import et de conformité

Bonnes pratiques :
- Garder ce dossier centré sur le cœur métier (pas de helpers ici)
- Ajouter un README par logique complexe si besoin
- Respecter la structure modulaire, la synchronisation JS/Python et la conformité CI/CD
