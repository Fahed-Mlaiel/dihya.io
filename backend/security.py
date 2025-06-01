# security.py – Kompatibilitäts-Stubs für create_jwt_token
from backend.flask.app.utils.jwt import create_jwt_token


def get_jwt_token_for_role(role: str) -> str:
    """
    Génère un JWT factice pour un rôle donné (stub de compatibilité pour les tests).
    Args:
        role (str): Le rôle de l'utilisateur (ex: 'admin', 'user', etc.)
    Returns:
        str: Un JWT simulé encodant le rôle.
    """
    payload = {"role": role}
    return create_jwt_token(payload)
