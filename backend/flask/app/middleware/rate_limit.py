"""
Middleware de rate limiting pour Dihya Coding.

Ce module protège l’API backend contre les abus (DoS, brute force, etc.) en limitant le nombre de requêtes par utilisateur/IP.
Il est conçu pour être simple, efficace et facilement extensible (Redis, DB, etc. en production).

Bonnes pratiques :
- Limite stricte configurable par endpoint et par utilisateur/IP
- Réinitialisation automatique de la fenêtre de temps
- Retour d’erreur explicite (429) en cas de dépassement
- Logging horodaté des dépassements
- Extensible pour whitelist/blacklist, quotas dynamiques, etc.
"""

from flask import request, jsonify, g
from time import time
from functools import wraps

# Configuration par défaut (à adapter)
RATE_LIMIT = 100         # Nombre max de requêtes
WINDOW_SECONDS = 60      # Par minute

# Stockage en mémoire (à remplacer par Redis ou DB en prod)
RATE_LIMIT_STORE = {}

def get_remote_id():
    # Utilise l’ID utilisateur si dispo, sinon l’IP
    return getattr(g, "user_id", None) or request.remote_addr

def rate_limited(func):
    """
    Décorateur Flask pour limiter le nombre de requêtes par utilisateur/IP.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = f"{get_remote_id()}:{request.endpoint}"
        now = int(time())
        window = now // WINDOW_SECONDS
        store_key = f"{key}:{window}"
        count = RATE_LIMIT_STORE.get(store_key, 0)
        if count >= RATE_LIMIT:
            # Logging simple (à remplacer par logger)
            print(f"[{now}] [RATE_LIMIT] Dépassement pour {key}")
            return jsonify({"error": "Trop de requêtes, réessayez plus tard."}), 429
        RATE_LIMIT_STORE[store_key] = count + 1
        return func(*args, **kwargs)
    return wrapper

# Exemple d’utilisation :
# from middleware.rate_limit import rate_limited
#
# @app.route("/api/secure")
# @jwt_required()
# @rate_limited
# def secure_endpoint():
#     return jsonify({"ok": True})