"""
Exemple de plugin template pour Dihya Coding.

Ce module sert de modèle pour la création de plugins personnalisés.
Il montre comment déclarer un plugin, valider sa configuration, exposer des routes API sécurisées,
et respecter les bonnes pratiques Dihya Coding (sécurité, modularité, documentation).

Bonnes pratiques :
- Valider la configuration du plugin à l'initialisation
- Protéger toutes les routes par JWT
- Logger les actions importantes
- Prévoir l'extensibilité (paramètres, hooks, etc.)
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

bp = Blueprint("example_plugin", __name__, url_prefix="/api/plugins/example")

def validate_config(config):
    """
    Valide la configuration du plugin.
    """
    if not isinstance(config, dict):
        raise ValueError("Config plugin invalide (dict attendu)")
    if "enabled" not in config or not isinstance(config["enabled"], bool):
        raise ValueError("Champ 'enabled' manquant ou invalide")
    return True

def log_plugin_action(user_id, action):
    print(f"[{datetime.utcnow().isoformat()}] [PLUGIN] user={user_id} action={action}")

# Exemple de configuration par défaut
PLUGIN_CONFIG = {
    "enabled": True,
    "param": "default"
}

@bp.route("/status", methods=["GET"])
@jwt_required()
def plugin_status():
    """
    Retourne le statut du plugin pour l'utilisateur courant.
    """
    user_id = get_jwt_identity()
    log_plugin_action(user_id, "status")
    return jsonify({
        "plugin": "example_plugin",
        "enabled": PLUGIN_CONFIG["enabled"],
        "param": PLUGIN_CONFIG["param"]
    }), 200

@bp.route("/run", methods=["POST"])
@jwt_required()
def plugin_run():
    """
    Exécute une action du plugin (exemple).
    Entrée : { "input": "..." }
    """
    user_id = get_jwt_identity()
    data = request.get_json(force=True)
    input_value = data.get("input")
    if not input_value or not isinstance(input_value, str):
        return jsonify({"error": "Entrée invalide"}), 400
    log_plugin_action(user_id, "run")
    # Traitement fictif
    result = f"Plugin exécuté avec : {input_value}"
    return jsonify({"result": result}), 200

# À intégrer dans votre app Flask principale :
# from backend.flask.app.plugins.templates.example_plugin import bp as example_plugin_bp
# app.register_blueprint(example_plugin_bp)