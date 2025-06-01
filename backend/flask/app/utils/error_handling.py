"""
Module de gestion centralisée des erreurs pour Dihya Coding.

Ce module fournit des fonctions et classes pour capturer, logger et retourner des réponses d’erreur
cohérentes et sécurisées à l’API, tout en respectant la confidentialité et la souveraineté des données.

Bonnes pratiques :
- Ne jamais exposer de stacktrace ou d’informations sensibles côté client.
- Logger chaque erreur critique avec horodatage et contexte.
- Retourner des messages d’erreur clairs, structurés et multilingues si besoin.
- Prévoir des handlers pour les erreurs courantes (404, 400, 401, 500, etc.).
- Utiliser ce module dans l’app Flask via app.register_error_handler.

Exemple d’utilisation :
    from backend.flask.app.utils.error_handling import register_error_handlers
    register_error_handlers(app)
"""

import logging
from flask import jsonify

def register_error_handlers(app):
    """
    Enregistre les handlers d’erreurs personnalisés sur l’application Flask.
    """
    @app.errorhandler(400)
    def bad_request(error):
        log_error("BadRequest", error)
        return error_response("Requête invalide.", 400)

    @app.errorhandler(401)
    def unauthorized(error):
        log_error("Unauthorized", error)
        return error_response("Authentification requise.", 401)

    @app.errorhandler(403)
    def forbidden(error):
        log_error("Forbidden", error)
        return error_response("Accès interdit.", 403)

    @app.errorhandler(404)
    def not_found(error):
        log_error("NotFound", error)
        return error_response("Ressource non trouvée.", 404)

    @app.errorhandler(500)
    def internal_error(error):
        log_error("InternalServerError", error)
        return error_response("Erreur interne du serveur.", 500)

def error_response(message, status_code):
    """
    Retourne une réponse JSON structurée pour une erreur API.
    """
    return jsonify({
        "success": False,
        "error": {
            "message": message,
            "code": status_code
        }
    }), status_code

def log_error(error_type, error):
    """
    Logge l’erreur avec horodatage et type.
    """
    logging.error(f"[{error_type}] {error}")