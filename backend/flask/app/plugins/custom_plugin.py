"""
Exemple de squelette de plugin custom pour Dihya Coding.

Ce module sert de modèle pour créer des plugins personnalisés, extensibles et sécurisés,
avec API REST, gestion des rôles, validation stricte et documentation claire.

Bonnes pratiques :
- Protéger toutes les routes par des vérifications de permissions (ACL).
- Valider et filtrer toutes les entrées utilisateur.
- Logger les opérations critiques pour audit.
- Prévoir des tests unitaires pour chaque endpoint.
- Ne jamais exposer de données sensibles ou de secrets dans les contenus ou logs.

Exemple d’utilisation :
    from backend.flask.app.plugins.custom_plugin import custom_blueprint
    app.register_blueprint(custom_blueprint, url_prefix="/api/custom")
"""

from flask import Blueprint, request, jsonify, abort, g
from backend.flask.app.security.acl import require_permission
import logging

custom_blueprint = Blueprint("custom", __name__)

def validate_custom_payload(data):
    """Valide le payload reçu pour l’API custom."""
    name = data.get("name", "")
    if not name or not isinstance(name, str) or len(name) > 100:
        return False, "Nom invalide"
    return True, ""

@custom_blueprint.route("/item", methods=["POST"])
@require_permission("custom_create")
def create_custom_item():
    """
    Exemple d’endpoint POST sécurisé pour créer un item custom.

    Sécurité :
    - Vérifie la permission 'custom_create'.
    - Valide les champs reçus.
    - Loggue l’opération pour audit.
    """
    data = request.get_json(force=True)
    valid, msg = validate_custom_payload(data)
    if not valid:
        abort(400, msg)
    item = {
        "id": 1,  # À remplacer par un vrai ID ou auto-incrément
        "name": data["name"],
        "created_by": getattr(g, "current_user", None).id if hasattr(g, "current_user") else "unknown"
    }
    logging.info(f"[CUSTOM_PLUGIN] Création item custom par {item['created_by']}")
    return jsonify(item), 201

@custom_blueprint.route("/item/<int:item_id>", methods=["GET"])
@require_permission("custom_view")
def get_custom_item(item_id):
    """
    Exemple d’endpoint GET sécurisé pour récupérer un item custom.

    Sécurité :
    - Vérifie la permission 'custom_view'.
    """
    # Simulation de récupération (à remplacer par DB)
    if item_id != 1:
        abort(404, "Item introuvable")
    item = {
        "id": 1,
        "name": "Exemple",
        "created_by": "admin"
    }
    return jsonify(item)