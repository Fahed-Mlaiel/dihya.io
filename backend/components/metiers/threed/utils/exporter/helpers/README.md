# helpers

Ce dossier est prévu pour accueillir des fonctions utilitaires, helpers ou extensions internes au module.

- Ajoutez ici vos helpers spécifiques au module.
- Structure recommandée : un fichier par helper, tests associés, README si besoin.
- `__init__.js` / `__init__.py` : points d'entrée modulaires (JS & Python)
- `__init__.test.js` / `__init__.test.py` : tests d'import et de conformité

## Exemples fournis
- `exporter_helper.js` / `exporter_helper.py` : formatage JSON pour l’export
- `exporter_helper.test.js` / `exporter_helper.test.py` : tests unitaires associés

## Bonnes pratiques
- Un helper = une fonction ou classe réutilisable, documentée, testée
- Ajoutez un README par helper complexe si besoin
- Respectez la structure modulaire, la synchronisation JS/Python et la conformité CI/CD
