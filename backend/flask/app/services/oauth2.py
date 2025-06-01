"""
Service OAuth2 pour Dihya Coding.

Ce module centralise l’intégration OAuth2 avec les principaux fournisseurs (Google, GitHub, etc.).
Il gère la sécurité, la validation des tokens, la création ou la liaison d’utilisateurs, et la gestion des erreurs.

Bonnes pratiques :
- Ne jamais stocker ou logguer de tokens d’accès ou de refresh.
- Valider chaque token côté serveur auprès du provider.
- Logger chaque tentative de connexion OAuth2 (sans données sensibles).
- Prévoir la gestion des erreurs et des cas de refus d’accès.
- Modulariser chaque provider pour faciliter l’ajout ou la maintenance.

Exemple d’utilisation :
    from backend.flask.app.services.oauth2 import get_google_user_info, get_github_user_info
    user_info = get_google_user_info(access_token)
"""

import requests

GOOGLE_USERINFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"
GITHUB_USERINFO_URL = "https://api.github.com/user"

def get_google_user_info(access_token):
    """
    Récupère les informations utilisateur Google via OAuth2.
    :param access_token: Token d’accès Google OAuth2
    :return: dict (id, email, name, picture, etc.) ou None
    """
    headers = {"Authorization": f"Bearer {access_token}"}
    resp = requests.get(GOOGLE_USERINFO_URL, headers=headers, timeout=5)
    if resp.status_code == 200:
        data = resp.json()
        return {
            "id": data.get("sub"),
            "email": data.get("email"),
            "name": data.get("name"),
            "picture": data.get("picture"),
            "provider": "google"
        }
    return None

def get_github_user_info(access_token):
    """
    Récupère les informations utilisateur GitHub via OAuth2.
    :param access_token: Token d’accès GitHub OAuth2
    :return: dict (id, email, name, avatar_url, etc.) ou None
    """
    headers = {"Authorization": f"Bearer {access_token}"}
    resp = requests.get(GITHUB_USERINFO_URL, headers=headers, timeout=5)
    if resp.status_code == 200:
        data = resp.json()
        return {
            "id": data.get("id"),
            "email": data.get("email"),
            "name": data.get("name") or data.get("login"),
            "avatar_url": data.get("avatar_url"),
            "provider": "github"
        }
    return None

# Ajouter ici d’autres providers si besoin (Microsoft, Facebook, etc.)