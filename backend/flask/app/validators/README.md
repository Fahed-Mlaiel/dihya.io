# Dossier `validators/` — Backend Dihya Coding

Ce dossier regroupe tous les schémas et fonctions de validation utilisés dans le backend Dihya Coding.

## Bonnes pratiques Dihya Coding

- **Centralisation** : tous les schémas de validation (utilisateur, projet, plugin, notification, etc.) sont regroupés ici pour garantir la cohérence et la sécurité des données.
- **Validation stricte** : chaque schéma doit vérifier la présence, le type et le format des champs attendus.
- **Extensibilité** : prévoir l’ajout facile de nouveaux schémas métiers sans modifier la logique métier existante.
- **Sécurité** : ne jamais valider ou exposer de secrets ou de données sensibles dans ce dossier.
- **Documentation** : chaque schéma/fonction doit être documenté pour faciliter l’intégration et l’audit.

## Exemples de contenu

- `schemas.py` : fonctions de validation pour les principaux objets métiers (user, projet, plugin, notification…)
- `__init__.py` : point d’entrée pour importer facilement tous les validateurs dans le backend

## Utilisation

Dans vos modules backend :

```python
from validators import validate_user, validate_project
validate_user(data)
```

---

*Ce dossier fait partie de la documentation technique interne Dihya Coding.*