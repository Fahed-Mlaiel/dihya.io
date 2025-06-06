# fallback

Ce dossier est destiné à accueillir les mécanismes de secours (fallback) pour l'export, par exemple : export minimal, backup, gestion d'échec, etc.

- Placez ici les fallback d'export JS/Python, leurs tests et documentation.
- Structure recommandée :
  - fallback.js / fallback.py
  - fallback.test.js / fallback.test.py
  - __init__.js / __init__.py : points d'entrée modulaires (JS & Python)
  - __init__.test.js / __init__.test.py : tests d'import et de conformité
  - README.md

Bonnes pratiques :
- Garder ce dossier centré sur les fallback métier (pas de helpers ici)
- Respecter la structure modulaire, la synchronisation JS/Python et la conformité CI/CD
