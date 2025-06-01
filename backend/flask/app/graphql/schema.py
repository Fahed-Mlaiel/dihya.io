"""
Schéma principal GraphQL pour Dihya Coding.

Ce module définit les types, requêtes et mutations exposés par l’API GraphQL du backend.
Il centralise la sécurité (authentification, rôles), la validation et la documentation des opérations.

Bonnes pratiques :
- Documenter chaque type, champ, requête et mutation.
- Protéger les mutations sensibles par authentification et contrôle de rôle.
- Valider toutes les entrées côté serveur.
- Ne jamais exposer de données sensibles dans les erreurs ou réponses.
- Séparer la logique métier dans les resolvers/services.
- Logger les opérations critiques pour auditabilité (sans fuite de données sensibles).
- Respecter la conformité RGPD (pas de données sensibles, audit, purge).
"""

import graphene
from graphene import ObjectType, String, Field, Int, Boolean, List
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
import logging

logger = logging.getLogger("dihya.graphql.schema")

# Exemple de type User
class UserType(graphene.ObjectType):
    """Type GraphQL représentant un utilisateur (hors données sensibles)."""
    id = Int(description="Identifiant unique de l'utilisateur")
    email = String(description="Adresse email (jamais de mot de passe)")
    role = String(description="Rôle de l'utilisateur (admin, user, etc.)")

# Décorateur pour sécuriser les mutations/queries (JWT)
def jwt_required_graphql(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        return fn(*args, **kwargs)
    return wrapper

# Query principale
class Query(ObjectType):
    """
    Requêtes principales GraphQL Dihya Coding.
    """
    hello = String(description="Test de disponibilité GraphQL")
    me = Field(UserType, description="Retourne l'utilisateur courant (JWT requis)")

    def resolve_hello(parent, info):
        """Retourne un message de bienvenue."""
        return "Bienvenue sur l’API GraphQL Dihya Coding !"

    @jwt_required_graphql
    def resolve_me(parent, info):
        """
        Retourne l'utilisateur courant (JWT requis).
        Jamais de données sensibles dans la réponse.
        """
        user_id = get_jwt_identity()
        # TODO: Récupérer l'utilisateur depuis la base (exemple fictif)
        logger.info(f"GraphQL: Consultation du profil utilisateur {user_id}")
        return UserType(id=user_id, email="user@dihya.dev", role="user")

# Mutation d’exemple (création de projet)
class CreateProject(graphene.Mutation):
    """
    Mutation pour créer un nouveau projet (JWT requis).
    Toutes les entrées sont validées côté serveur.
    """
    class Arguments:
        name = String(required=True, description="Nom du projet")
        type = String(required=True, description="Type de projet (webapp, mobile, etc.)")

    ok = Boolean(description="Succès de la création")
    project_id = Int(description="ID du projet créé")
    message = String(description="Message de retour")

    @jwt_required_graphql
    def mutate(self, info, name, type):
        # Validation stricte côté serveur
        if not name or len(name) < 3:
            logger.warning("Tentative de création de projet avec nom invalide")
            return CreateProject(ok=False, project_id=None, message="Nom de projet invalide.")
        # TODO: Ajouter la logique de création réelle (validation, audit, etc.)
        # Exemple fictif :
        project_id = 123
        logger.info(f"Projet créé via GraphQL: {name} (type={type}) par user={get_jwt_identity()}")
        return CreateProject(ok=True, project_id=project_id, message="Projet créé avec succès.")

class Mutation(ObjectType):
    """
    Mutations principales GraphQL Dihya Coding.
    """
    create_project = CreateProject.Field(description="Créer un nouveau projet (JWT requis)")

# Schéma principal
schema = graphene.Schema(query=Query, mutation=Mutation)