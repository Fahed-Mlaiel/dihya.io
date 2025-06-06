# helpers

Ce dossier est prévu pour accueillir des fonctions utilitaires, helpers ou extensions internes au module i18n.

- Ajoutez ici vos helpers spécifiques au module i18n.
- Structure recommandée : un fichier par helper, tests associés, README si besoin.
- `__init__.js` / `__init__.py` : points d'entrée modulaires (JS & Python)
- `__init__.test.js` / `__init__.test.py` : tests d'import et de conformité

## Exemples fournis
- `i18n_helper.js` / `i18n_helper.py` : helpers pour la gestion des langues
- `i18n_helper.test.js` / `i18n_helper.test.py` : tests unitaires associés

## Bonnes pratiques
- Un helper = une fonction ou classe réutilisable, documentée, testée
- Ajoutez un README par helper complexe si besoin
- Respectez la structure modulaire, la synchronisation JS/Python et la conformité CI/CD
