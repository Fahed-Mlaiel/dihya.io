# roles/ — Gestion avancée des rôles utilisateurs (Dihya Coding)

Ce dossier centralise la définition, la validation et la gestion des rôles utilisateurs et de leurs permissions pour le backend Flask Dihya Coding.

## Objectif

- Définir clairement les rôles (Admin, User, Invité, etc.) et leurs droits associés.
- Permettre une gestion fine des accès et des actions sensibles.
- Faciliter l’extension pour de nouveaux rôles ou permissions spécifiques.
- Garantir la conformité RGPD et la traçabilité des accès.

## Bonnes pratiques

- Centraliser toutes les permissions ici pour éviter la dispersion de la logique métier.
- Valider chaque action sensible côté backend selon le rôle de l’utilisateur.
- Documenter chaque rôle et ses droits.
- Ne jamais exposer la logique de permission côté client.
- Prévoir des tests unitaires pour la gestion des rôles et permissions.
- Prévoir l’extensibilité pour de nouveaux rôles ou permissions métiers.
- Logger les accès et refus pour audit et conformité.

## Exemple de rôles et permissions

- **admin** : gestion des utilisateurs, logs, plugins, suppression de projets, export/import, accès admin panel, gestion des rôles et paramètres.
- **user** : création, édition, consultation de ses projets, utilisation des plugins, modification de profil, feedback.
- **guest** : consultation de projets publics, inscription, accès aux templates publics.

## Exemple d’utilisation

```python
from app.models.roles.permissions import has_permission

if has_permission(user, "delete_project"):
    # action autorisée
else:
    raise PermissionError("Accès refusé")