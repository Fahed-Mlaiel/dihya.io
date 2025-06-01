"""
Service utilisateur pour l'application Dihya Coding.
Inclut : récupération, mise à jour, suppression, et gestion des utilisateurs.
"""

from ..models.user import User, get_user_by_id as model_get_user_by_id, USERS_DB, remove_user

def get_user_by_id(user_id):
    """
    Récupère un utilisateur par son ID.
    Args:
        user_id (int): Identifiant utilisateur
    Returns:
        User ou None
    """
    return model_get_user_by_id(user_id)

def get_all_users():
    """
    Retourne la liste de tous les utilisateurs.
    Returns:
        list[User]
    """
    return list(USERS_DB.values())

def update_user(user_id, data):
    """
    Met à jour les informations d'un utilisateur.
    Args:
        user_id (int): Identifiant utilisateur
        data (dict): Données à mettre à jour
    Returns:
        (User, str): Utilisateur mis à jour ou None, message d'erreur ou None
    """
    user = get_user_by_id(user_id)
    if not user:
        return None, "Utilisateur non trouvé."

    username = data.get("username")
    email = data.get("email")
    role = data.get("role")
    is_active = data.get("is_active")

    if username:
        user.username = username
    if email:
        user.email = email
    if role:
        user.role = role
    if is_active is not None:
        user.is_active = is_active

    return user, None

def delete_user(user_id):
    """
    Supprime un utilisateur par son ID.
    Args:
        user_id (int): Identifiant utilisateur
    Returns:
        (bool, str): True si supprimé, message d'erreur ou None
    """
    user = get_user_by_id(user_id)
    if not user:
        return False, "Utilisateur non trouvé."
    remove_user(user_id)
    return True, None