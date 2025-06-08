# validators/

Ce dossier regroupe tous les validateurs de sécurité, organisés par thématique :

- `input/` : validateurs d’input utilisateur (Node.js, Python)
- `rgpd/` : validateurs de conformité RGPD (Node.js, Python)
- `samples/` : exemples avancés d’utilisation (input, rgpd)

Chaque sous-dossier contient :
- Les scripts principaux
- Un README explicatif
- Les fichiers d’initialisation (`__init__.js`, `__init__.py`)
- Un fichier `.keep` pour le versionnement

Le point d’entrée principal du module est `index.js`.

## Bonnes pratiques
- Ajouter tout nouveau validateur ou exemple dans le sous-dossier approprié.
- Documenter chaque validateur et fournir des exemples d’utilisation.
- Ajouter des tests unitaires pour chaque validateur.
