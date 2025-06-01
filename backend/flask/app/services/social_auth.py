"""
Module d’authentification sociale (OAuth2) pour Dihya Coding.

Ce module permet l’intégration de l’authentification via Google, GitHub, etc.
pour simplifier l’inscription et la connexion des utilisateurs.

Bonnes pratiques :
- Ne jamais stocker de secrets OAuth dans le code source (utiliser variables d’environnement).
- Valider et vérifier chaque token reçu auprès du fournisseur.
- Logger chaque tentative de connexion sociale avec horodatage (sans données sensibles).
- Prévoir un fallback sécurisé si le service tiers est indisponible.
- Associer ou créer un compte utilisateur local à chaque connexion sociale.

Exemple d’utilisation :
    from backend.flask.app.services.social_auth import get_google_user_info, handle_social_login

"""

import os
import requests
from flask import request, redirect, url_for, session

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

def get_google_user_info(token):
    """
    Vérifie le token Google et retourne les infos utilisateur.
    """
    userinfo_endpoint = get_google_provider_cfg()["userinfo_endpoint"]
    resp = requests.get(
        userinfo_endpoint,
        headers={"Authorization": f"Bearer {token}"}
    )
    if resp.status_code != 200:
        return None
    return resp.json()

def handle_social_login(provider, token):
    """
    Gère la connexion sociale pour un provider donné.
    :param provider: 'google', 'github', etc.
    :param token: access_token reçu du frontend
    :return: dict user_info ou None
    """
    if provider == "google":
        user_info = get_google_user_info(token)
        # Ici, associer ou créer un compte local selon user_info['email']
        return user_info
    # Ajouter d'autres providers ici (GitHub, etc.)
    return None

# Exemple de route Flask (à placer dans routes/auth.py)
# @app.route("/auth/social/<provider>", methods=["POST"])
# def social_auth(provider):
#     token = request.json.get("token")
#     user_info = handle_social_login(provider, token)
#     if not user_info:
#         return {"success": False, "error": "Authentification sociale échouée"}, 401
#     # Créer ou récupérer l'utilisateur local, générer JWT, etc.
#     return {"success": True, "user": user_info}