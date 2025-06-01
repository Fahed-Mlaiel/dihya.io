"""
Serveur de documentation OpenAPI pour Dihya Coding.

Ce module expose la documentation OpenAPI (swagger) du backend via un endpoint sécurisé,
permettant la consultation interactive de l’API par les développeurs et parties prenantes.

Bonnes pratiques :
- Ne jamais exposer d’informations sensibles dans la doc
- Sécuriser l’accès à la doc en production (auth, IP whitelist, etc.)
- Générer la doc à partir de la source (openapi.yaml)
- Prévoir l’extensibilité (ajout de doc dynamique, versionnage, etc.)

Utilisation :
    from backend.flask.app.docs.serve_openapi import openapi_bp
    app.register_blueprint(openapi_bp)
"""

import os
from flask import Blueprint, send_from_directory, abort, request

OPENAPI_DIR = os.path.abspath(os.path.dirname(__file__))
OPENAPI_FILE = "openapi.yaml"

openapi_bp = Blueprint("openapi", __name__, url_prefix="/api/docs")

def is_authorized():
    """
    Contrôle d’accès à la documentation (à adapter selon besoin).
    Par défaut : autorise seulement localhost.
    """
    allowed_ips = ["127.0.0.1", "::1"]
    return request.remote_addr in allowed_ips

@openapi_bp.route("/", methods=["GET"])
def serve_openapi():
    """
    Sert le fichier openapi.yaml (documentation API).
    """
    if not is_authorized():
        abort(403)
    return send_from_directory(OPENAPI_DIR, OPENAPI_FILE, mimetype="text/yaml")

# Pour intégrer dans l’app Flask :
# from backend.flask.app.docs.serve_openapi import openapi_bp
# app.register_blueprint(openapi_bp)
