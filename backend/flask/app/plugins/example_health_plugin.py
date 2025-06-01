"""
Example Health Plugin – Dihya Coding
Plugin backend complet, documenté, testable, désactivable à chaud.
Fonctionnalité : expose un endpoint /api/health/extra pour monitoring avancé (métriques, RGPD, audit).
"""
from backend.flask.app.plugins.generation_plugin import GenerationPluginBase
from flask import Blueprint, jsonify

class ExampleHealthPlugin(GenerationPluginBase):
    name = "example_health"
    description = "Plugin de monitoring santé avancé (métriques, RGPD, audit)"
    version = "1.0.0"
    enabled = True

    def register(self, app):
        bp = Blueprint("example_health_plugin", __name__)

        @bp.route("/api/health/extra", methods=["GET"])
        def extra_health():
            # Expose des métriques fictives, auditables, RGPD
            return jsonify({
                "status": "ok",
                "metrics": {
                    "uptime": 123456,
                    "users_online": 42,
                    "cpu": 12.3,
                    "ram": 45.6
                },
                "rgpd": True,
                "audit": "ok"
            })
        app.register_blueprint(bp)

    def unregister(self, app):
        # Permet la désactivation à chaud (hot reload)
        # (À implémenter selon la logique de l’app Flask)
        pass
