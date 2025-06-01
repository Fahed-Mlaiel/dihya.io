# models/ — Modèles de données Backend Flask Dihya Coding

Ce dossier contient les modèles de données SQLAlchemy utilisés par le backend Flask de Dihya Coding.

## Contenu

- **user.py** : Modèle utilisateur (User), avec gestion des rôles, timestamps, sécurité des mots de passe, etc.
- **__init__.py** : Initialisation du package models.

## Bonnes pratiques

- Utiliser SQLAlchemy pour la définition de tous les modèles de base de données.
- Ajouter des docstrings à chaque modèle et champ important.
- Prévoir des champs standards : `id`, `created_at`, `updated_at`, `is_active`, etc.
- Gérer la sécurité des mots de passe (hash, vérification) dans le modèle ou via des utilitaires.
- Prévoir des méthodes utilitaires pour la sérialisation ou la gestion des droits.
- Ne jamais stocker de mot de passe en clair.
- Prévoir des relations explicites (ForeignKey, relationship) si besoin.

## Exemple d’utilisation

```python
from app.models.user import User

new_user = User(username="alice", email="alice@example.com")
new_user.set_password("motdepassefort")
## Exemple d'utilisation

```python
# Voir la documentation du module pour un exemple précis
```

