"""
Initialisation de l'application Flask pour Dihya Coding.
Inclut la configuration, l'enregistrement des blueprints, la gestion des extensions,
et les bonnes pratiques de sécurité.
"""

from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_babel import Babel
from .routes import main as main_blueprint
from .routes import auth as auth_blueprint
from .routes import user as user_blueprint
from .templates.seo import bp as seo_bp
from .utils.seo import set_robots_headers, set_sitemap_headers

mail = Mail()
jwt = JWTManager()
babel = Babel()

def create_app(config_object="config.Config"):
    """
    Crée et configure l'application Flask.
    - Charge la configuration.
    - Initialise les extensions.
    - Enregistre les blueprints (routes).
    - Active la sécurité de base (CORS, headers).
    """
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Sécurité de base : CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Extensions
    mail.init_app(app)
    jwt.init_app(app)
    babel.init_app(app)

    # Blueprints (routes)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix="/api/auth")
    app.register_blueprint(user_blueprint, url_prefix="/api/users")
    from .routes.generate import generate_bp
    app.register_blueprint(generate_bp)
    app.register_blueprint(seo_bp)

    # Headers de sécurité supplémentaires
    @app.after_request
    def set_security_headers(response):
        response = set_robots_headers(response)
        response = set_sitemap_headers(response)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["Permissions-Policy"] = "geolocation=(), microphone=()"
        return response

    # Gestion des erreurs globales
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Requête invalide", "details": str(error)}), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({"error": "Non autorisé", "details": str(error)}), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Ressource non trouvée"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Erreur interne du serveur"}), 500

    # Healthcheck (doublon pour compatibilité monitoring)
    @app.route("/api/health", methods=["GET"])
    def health():
        """Vérifie que l'API fonctionne."""
        return jsonify({"status": "ok", "message": "Dihya API up"}), 200

    return app
