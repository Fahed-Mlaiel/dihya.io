"""
Resolvers GraphQL pour Dihya Coding.

Ce module centralise la logique métier des queries et mutations GraphQL.
Il sépare la logique d’accès aux données, la validation et la sécurité des schémas.

Bonnes pratiques :
- Valider toutes les entrées côté serveur.
- Protéger les mutations sensibles par authentification et contrôle de rôle.
- Logger chaque action critique pour auditabilité (sans fuite de données sensibles).
- Ne jamais exposer de données sensibles dans les erreurs ou réponses.
- Utiliser les services métiers pour la logique métier (pas d’accès direct à la base ici).
- Respecter la conformité RGPD (pas de données sensibles, audit, purge).
"""

import logging
from backend.flask.app.services.user_service import get_user_by_id
from backend.flask.app.services.project_service import create_project as service_create_project

logger = logging.getLogger("dihya.graphql.resolvers")

def resolve_me(user_id):
    """
    Résout la query 'me' pour retourner les infos de l'utilisateur courant.

    Args:
        user_id (int): ID de l'utilisateur courant

    Returns:
        dict | None: Dictionnaire utilisateur (hors données sensibles) ou None si non trouvé.
    """
    user = get_user_by_id(user_id)
    if not user:
        logger.info(f"GraphQL: Utilisateur {user_id} non trouvé pour 'me'")
        return None
    logger.info(f"GraphQL: Consultation du profil utilisateur {user_id}")
    return {
        "id": user.id,
        "email": user.email,
        "role": user.role
    }

def resolve_create_project(user_id, name, type):
    """
    Résout la mutation 'create_project' pour créer un projet.

    Args:
        user_id (int): ID de l'utilisateur courant
        name (str): nom du projet
        type (str): type de projet

    Returns:
        dict: {ok, project_id, message}
    """
    # Validation stricte des entrées
    if not name or len(name) < 3:
        logger.warning(f"GraphQL: Création projet refusée (nom invalide) par user={user_id}")
        return {
            "ok": False,
            "project_id": None,
            "message": "Nom de projet invalide."
        }
    if type not in {"webapp", "mobile", "ecommerce", "blog"}:
        logger.warning(f"GraphQL: Création projet refusée (type invalide) par user={user_id}")
        return {
            "ok": False,
            "project_id": None,
            "message": "Type de projet non supporté."
        }
    try:
        # Appel au service métier (doit gérer audit, sécurité, RGPD)
        project_id = service_create_project(user_id, name, type)
        logger.info(f"GraphQL: Projet créé (id={project_id}) par user={user_id}")
        return {
            "ok": True,
            "project_id": project_id,
            "message": "Projet créé avec succès."
        }
    except Exception as e:
        logger.error(f"GraphQL: Erreur création projet par user={user_id}: {e}")
        return {
            "ok": False,
            "project_id": None,
            "message": "Erreur lors de la création du projet."
        }