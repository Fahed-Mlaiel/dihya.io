# core

Ce dossier contient la logique métier principale du module i18n :
- `i18n.js` / `i18n.py` : logique métier i18n
- `i18n.test.js` / `i18n.test.py` : tests unitaires associés
- `__init__.js` / `__init__.py` : points d'entrée modulaires (JS & Python)
- `__init__.test.js` / `__init__.test.py` : tests d'import et de conformité

Bonnes pratiques :
- Garder ce dossier centré sur le cœur métier (pas de helpers ici)
- Respecter la structure modulaire, la synchronisation JS/Python et la conformité CI/CD
- Ajouter un README par logique complexe si besoin
