"""
API de gestion des plugins pour Dihya Coding.

Ce module expose des routes et fonctions pour l’ajout, la suppression, la liste et l’activation/désactivation
de plugins côté backend. Il centralise la validation, la sécurité (authentification, rôles), et la documentation.

Bonnes pratiques :
- Authentifier chaque requête (JWT, rôle admin requis pour modification).
- Valider chaque plugin (nom, version, compatibilité, signature).
- Logger chaque action critique (ajout, suppression, activation).
- Ne jamais charger de code non validé ou non signé.
- Prévoir des tests unitaires pour chaque endpoint.

Exemple d’utilisation :
    POST /api/plugins/add
    GET /api/plugins/list
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..utils.validators import validate_plugin_payload
from backend.flask.app.utils.exceptions import ValidationError, PermissionError

plugins_bp = Blueprint("plugins", __name__, url_prefix="/api/plugins")

# Stockage fictif en mémoire (à remplacer par une base de données)
PLUGINS = []

def is_admin(user):
    # À remplacer par une vraie vérification de rôle
    return user and user.get("role") == "admin"

@plugins_bp.route("/list", methods=["GET"])
@jwt_required()
def list_plugins():
    """
    Liste tous les plugins installés.
    """
    return jsonify({"plugins": PLUGINS}), 200

@plugins_bp.route("/add", methods=["POST"])
@jwt_required()
def add_plugin():
    """
    Ajoute un nouveau plugin (admin uniquement).
    """
    user = get_jwt_identity()
    if not is_admin(user):
        raise PermissionError("Seul un administrateur peut ajouter un plugin.")
    payload = request.get_json()
    if not payload or not validate_plugin_payload(payload):
        raise ValidationError("Payload plugin invalide.")
    # Vérifier unicité
    if any(p["name"] == payload["name"] for p in PLUGINS):
        raise ValidationError("Plugin déjà installé.")
    PLUGINS.append({
        "name": payload["name"],
        "version": payload.get("version", "1.0.0"),
        "enabled": True,
        "author": payload.get("author", ""),
        "description": payload.get("description", "")
    })
    return jsonify({"success": True, "message": "Plugin ajouté."}), 201

@plugins_bp.route("/enable", methods=["POST"])
@jwt_required()
def enable_plugin():
    """
    Active ou désactive un plugin (admin uniquement).
    """
    user = get_jwt_identity()
    if not is_admin(user):
        raise PermissionError("Seul un administrateur peut modifier un plugin.")
    payload = request.get_json()
    name = payload.get("name")
    enabled = payload.get("enabled", True)
    for plugin in PLUGINS:
        if plugin["name"] == name:
            plugin["enabled"] = enabled
            return jsonify({"success": True, "message": f"Plugin {'activé' if enabled else 'désactivé'}."}), 200
    raise ValidationError("Plugin introuvable.")

@plugins_bp.route("/remove", methods=["POST"])
@jwt_required()
def remove_plugin():
    """
    Supprime un plugin installé (admin uniquement).
    """
    user = get_jwt_identity()
    if not is_admin(user):
        raise PermissionError("Seul un administrateur peut supprimer un plugin.")
    payload = request.get_json()
    name = payload.get("name")
    global PLUGINS
    before = len(PLUGINS)
    PLUGINS = [p for p in PLUGINS if p["name"] != name]
    if len(PLUGINS) == before:
        raise ValidationError("Plugin introuvable.")
    return jsonify({"success": True, "message": "Plugin supprimé."}), 200
