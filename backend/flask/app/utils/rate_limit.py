"""
Module de rate limiting et anti-DDoS pour Dihya Coding.

Ce module fournit des décorateurs et fonctions pour limiter le nombre de requêtes par utilisateur/IP
sur les endpoints critiques du backend Flask, afin de prévenir les abus et attaques par déni de service.

Bonnes pratiques :
- Configurer les limites via variables d’environnement ou paramètres centralisés.
- Logger chaque dépassement de quota avec horodatage et IP/utilisateur.
- Retourner une réponse claire et sécurisée en cas de dépassement.
- Ne jamais exposer d’informations sensibles dans les messages d’erreur.
- Prévoir des exceptions pour les administrateurs ou services internes si besoin.

Exemple d’utilisation :
    from backend.flask.app.utils.rate_limit import rate_limit

    @app.route("/api/secure")
    @rate_limit(limit=10, window=60)
    def secure_endpoint():
        return "OK"
"""

import time
from functools import wraps
from flask import request, jsonify, g

# Stockage simple en mémoire (à remplacer par Redis/Memcached en prod)
RATE_LIMIT_STORE = {}

def rate_limit(limit=60, window=60):
    """
    Décorateur Flask pour limiter le nombre de requêtes par IP sur une fenêtre temporelle.
    :param limit: Nombre max de requêtes autorisées
    :param window: Fenêtre en secondes
    """
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            ip = request.remote_addr or "unknown"
            now = int(time.time())
            window_start = now - (now % window)
            key = f"{ip}:{window_start}:{request.endpoint}"
            count = RATE_LIMIT_STORE.get(key, 0)
            if count >= limit:
                log_rate_limit_exceeded(ip, request.endpoint)
                return jsonify({
                    "success": False,
                    "error": {
                        "message": "Trop de requêtes. Merci de réessayer plus tard.",
                        "code": 429
                    }
                }), 429
            RATE_LIMIT_STORE[key] = count + 1
            return f(*args, **kwargs)
        return wrapped
    return decorator

def log_rate_limit_exceeded(ip, endpoint):
    """
    Logge chaque dépassement de quota pour audit.
    """
    from datetime import datetime
    log_file = "logs/rate_limit.log"
    msg = f"{datetime.utcnow().isoformat()} | IP: {ip} | Endpoint: {endpoint} | Rate limit exceeded"
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except Exception:
        pass