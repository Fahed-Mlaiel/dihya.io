"""
Plugin CMS (Content Management System) pour Dihya Coding.

Ce module fournit un plugin extensible pour la gestion de contenus (pages, articles, médias, etc.)
dans les projets générés par Dihya Coding, avec API REST sécurisée, gestion des rôles et validation.

Bonnes pratiques :
- Protéger toutes les routes par des vérifications de permissions (ACL).
- Valider et filtrer toutes les entrées utilisateur (titre, contenu, fichiers).
- Logger les opérations critiques (création, modification, suppression).
- Prévoir des tests unitaires pour chaque endpoint.
- Ne jamais exposer de données sensibles ou de secrets dans les contenus ou logs.

Exemple d’utilisation :
    from backend.flask.app.plugins.cms_plugin import cms_blueprint
    app.register_blueprint(cms_blueprint, url_prefix="/api/cms")
"""

from flask import Blueprint, request, jsonify, abort, g
from backend.flask.app.security.acl import require_permission
import logging

cms_blueprint = Blueprint("cms", __name__)

# Simu base mémoire (remplacer par DB réelle)
_CMS_CONTENT = {}
_CONTENT_ID_SEQ = 1

def validate_content(data):
    """Valide les champs d'un contenu CMS."""
    title = data.get("title", "")
    body = data.get("body", "")
    if not title or not isinstance(title, str) or len(title) > 200:
        return False, "Titre invalide"
    if not body or not isinstance(body, str):
        return False, "Contenu invalide"
    return True, ""

@cms_blueprint.route("/content", methods=["POST"])
@require_permission("edit_content")
def create_content():
    """
    Crée un nouveau contenu CMS.

    Sécurité :
    - Vérifie la permission 'edit_content'.
    - Valide les champs reçus.
    - Loggue l'opération pour audit.
    """
    global _CONTENT_ID_SEQ
    data = request.get_json(force=True)
    valid, msg = validate_content(data)
    if not valid:
        abort(400, msg)
    content_id = str(_CONTENT_ID_SEQ)
    _CONTENT_ID_SEQ += 1
    _CMS_CONTENT[content_id] = {
        "id": content_id,
        "title": data["title"],
        "body": data["body"],
        "author": getattr(g, "current_user", None).id if hasattr(g, "current_user") else "unknown"
    }
    logging.info(f"[CMS] Création contenu {content_id} par {g.current_user.id if hasattr(g, 'current_user') else 'unknown'}")
    return jsonify(_CMS_CONTENT[content_id]), 201

@cms_blueprint.route("/content/<content_id>", methods=["GET"])
@require_permission("view_content")
def get_content(content_id):
    """
    Récupère un contenu CMS par son ID.

    Sécurité :
    - Vérifie la permission 'view_content'.
    """
    content = _CMS_CONTENT.get(content_id)
    if not content:
        abort(404, "Contenu introuvable")
    return jsonify(content)

@cms_blueprint.route("/content/<content_id>", methods=["PUT"])
@require_permission("edit_content")
def update_content(content_id):
    """
    Modifie un contenu CMS existant.

    Sécurité :
    - Vérifie la permission 'edit_content'.
    - Valide les champs reçus.
    - Loggue l'opération pour audit.
    """
    content = _CMS_CONTENT.get(content_id)
    if not content:
        abort(404, "Contenu introuvable")
    data = request.get_json(force=True)
    valid, msg = validate_content(data)
    if not valid:
        abort(400, msg)
    content.update({
        "title": data["title"],
        "body": data["body"]
    })
    logging.info(f"[CMS] Modification contenu {content_id} par {g.current_user.id if hasattr(g, 'current_user') else 'unknown'}")
    return jsonify(content)

@cms_blueprint.route("/content/<content_id>", methods=["DELETE"])
@require_permission("delete_content")
def delete_content(content_id):
    """
    Supprime un contenu CMS existant.

    Sécurité :
    - Vérifie la permission 'delete_content'.
    - Loggue l'opération pour audit.
    """
    content = _CMS_CONTENT.pop(content_id, None)
    if not content:
        abort(404, "Contenu introuvable")
    logging.info(f"[CMS] Suppression contenu {content_id} par {g.current_user.id if hasattr(g, 'current_user') else 'unknown'}")
    return jsonify({"status": "deleted", "id": content_id})