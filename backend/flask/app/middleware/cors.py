"""
Middleware CORS pour Dihya Coding.

Ce module gère la politique Cross-Origin Resource Sharing (CORS) pour sécuriser l’accès à l’API backend.
Il permet de contrôler les origines autorisées, les méthodes, les headers, et d’éviter les failles XSS/CORS.

Bonnes pratiques :
- Origines autorisées configurables (whitelist)
- Headers et méthodes strictement définis
- Support des credentials si besoin (cookies, JWT)
- Pas d’origines génériques en production ("*")
- Logging des accès cross-origin suspects
"""

from flask import request, make_response

# Liste blanche des origines autorisées (à adapter dynamiquement en prod)
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://dihya.app",
    # Ajouter d'autres domaines front autorisés ici
]

ALLOWED_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
ALLOWED_HEADERS = ["Content-Type", "Authorization"]

def cors_middleware(app):
    """
    À appeler dans create_app() pour activer CORS sur toutes les routes.
    """

    @app.after_request
    def add_cors_headers(response):
        origin = request.headers.get("Origin")
        if origin and origin in ALLOWED_ORIGINS:
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Vary"] = "Origin"
            response.headers["Access-Control-Allow-Methods"] = ", ".join(ALLOWED_METHODS)
            response.headers["Access-Control-Allow-Headers"] = ", ".join(ALLOWED_HEADERS)
            response.headers["Access-Control-Allow-Credentials"] = "true"
        elif origin:
            # Logging simple (à remplacer par logger)
            print(f"[CORS] Origine non autorisée : {origin}")
        return response

    # Gestion des preflight OPTIONS
    @app.route('/<path:path>', methods=['OPTIONS'])
    def options_handler(path):
        response = make_response()
        origin = request.headers.get("Origin")
        if origin and origin in ALLOWED_ORIGINS:
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Access-Control-Allow-Methods"] = ", ".join(ALLOWED_METHODS)
            response.headers["Access-Control-Allow-Headers"] = ", ".join(ALLOWED_HEADERS)
            response.headers["Access-Control-Allow-Credentials"] = "true"
        return response, 204

# Exemple d’utilisation dans app/__init__.py :
# from middleware.cors import cors_middleware
# cors_middleware(app)