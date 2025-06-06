# fallback – Validators (clé en main, ultra avancé)

Ce dossier est destiné à accueillir les mécanismes de secours (fallback) pour les validators :

- `fallback.js` / `fallback.py` : fallback validators JS/Python (validation minimale, gestion d’échec, etc.)
- `fallback.test.js` / `fallback.test.py` : tests unitaires associés
- `__init__.js` / `__init__.py` : points d’entrée modulaires (synchronisation, conformité, CI/CD)
- `__init__.test.js` / `__init__.test.py` : tests d’import et d’intégration (audit, conformité)

## Bonnes pratiques
- Un fallback = une solution de secours robuste, testée, documentée
- Synchroniser JS/Python (API, logique, tests)
- Documenter chaque ajout pour l’audit, la CI/CD et la traçabilité
- Utiliser les points d’entrée `__init__` pour garantir la conformité et l’intégration continue

---

> Ce dossier est la référence pour les fallback validators. Toute extension doit respecter la structure, la synchronisation JS/Python et la conformité métier.
