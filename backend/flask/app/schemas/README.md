# schemas/ — Schémas de validation Backend Flask Dihya Coding

Ce dossier contient les schémas Marshmallow utilisés pour la sérialisation, la validation et la désérialisation des données dans l’API Flask Dihya Coding.

---

## Contenu

- **user.py** : Schéma de validation pour les utilisateurs (inscription, login, update, etc.).
- **project.py** : Schéma de validation pour les projets générés (structure, sécurité, auditabilité).
- **plugin.py** : Schéma de validation pour les plugins (activation, sécurité, conformité).
- **__init__.py** : Initialisation du package schemas.

---

## Bonnes pratiques

- Utiliser Marshmallow pour tous les schémas de validation et de sérialisation.
- Documenter chaque schéma et chaque champ avec une docstring claire et précise.
- Séparer les schémas de création, de mise à jour et de réponse (UserSchema, UserRegisterSchema, UserUpdateSchema, etc.).
- Ajouter des validations personnalisées pour les règles métier spécifiques (unicité, format, sécurité).
- Ne jamais exposer de champs sensibles (ex : mot de passe, token, secret) dans les schémas de sortie.
- Logger les erreurs de validation pour auditabilité (sans fuite de données sensibles).
- Prévoir la purge et l’export des logs de validation pour conformité RGPD.
- Versionner les schémas en cas d’évolution majeure pour garantir la compatibilité.

---

## Exemple d’utilisation

```python
from app.schemas.user import UserSchema

user_schema = UserSchema()
result = user_schema.load(request.json)  # Validation et désérialisation

from app.schemas.project import ProjectSchema

project_data = {...}
ProjectSchema.validate(project_data)  # Validation stricte, lève une exception si invalide