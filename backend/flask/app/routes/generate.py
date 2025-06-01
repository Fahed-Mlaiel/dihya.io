"""
Route API pour la génération automatique de projets (Dihya Coding).

Cette route permet de générer un projet numérique complet (frontend, backend, mobile, etc.)
à partir d’un cahier des charges fourni en texte ou en vocal, en s’appuyant sur l’IA et les modules internes.

Bonnes pratiques :
- Authentifier chaque requête (JWT obligatoire).
- Valider et filtrer le cahier des charges (anti-injection, taille max, etc.).
- Logger chaque génération avec horodatage, utilisateur, type de projet et statut.
- Ne jamais inclure de secrets ou de code sensible dans la réponse.
- Prévoir un fallback IA open source si quota GPT/Cloud dépassé.
- Retourner un lien de prévisualisation ou de téléchargement sécurisé.
- Respecter la conformité RGPD (logs anonymisés, purge possible).
- Documenter chaque paramètre et chaque étape critique.

Exemple d’utilisation :
    POST /api/generate
    {
        "spec": "Je veux une app de gestion de tâches multilingue...",
        "type": "webapp",
        "stack": "react+flask"
    }
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..utils.validators import validate_generate_payload
from ..utils.security import sanitize_input
from ..ai_fallback.quotas import check_quota, use_fallback_ai
from ..services.generation_service import generate_project
from ..generation_logs import log_generation_event
import logging
from datetime import datetime

generate_bp = Blueprint("generate", __name__, url_prefix="/api/generate")

@generate_bp.route("", methods=["POST"])
@jwt_required()
def generate_project_route():
    """
    Génère un projet à partir d’un cahier des charges fourni par l’utilisateur authentifié.

    Sécurité :
        - JWT obligatoire
        - Validation stricte du payload
        - Sanitation du cahier des charges (anti-injection)
        - Logging sans fuite de données sensibles

    Returns:
        JSON : {success, status, code, preview_url, error}
    """
    user = get_jwt_identity()
    payload = request.get_json()
    if not payload or not validate_generate_payload(payload):
        return jsonify({"success": False, "error": "Spécification invalide."}), 400

    spec = sanitize_input(payload.get("spec", ""))
    if not spec or len(spec) < 10 or len(spec) > 2000:
        return jsonify({"success": False, "error": "Cahier des charges invalide."}), 400

    project_type = payload.get("type", "webapp")
    stack = payload.get("stack", "react+flask")

    # Vérification quota IA propriétaire
    if not check_quota(user):
        # Fallback IA open source
        code, preview_url = use_fallback_ai(spec, project_type, stack)
        status = "FALLBACK"
    else:
        # Génération principale via service métier (peut appeler l’IA propriétaire)
        result = generate_project(spec, user_id=user)
        if not result.success:
            logging.warning(f"Generation failed for user={user}: {result.error}")
            log_generation_event(user, {"project_type": project_type, "stack": stack}, {}, status="error", error=result.error)
            return jsonify({"success": False, "error": result.error}), 500
        code = result.data.get("code", {})
        preview_url = result.data.get("project", {}).get("preview_url", "")
        status = "SUCCESS"

    # Log de la génération (auditabilité, RGPD)
    log_generation_event(
        user_id=user,
        needs={"project_type": project_type, "stack": stack},
        code={k: "" for k in code} if isinstance(code, dict) else {},
        status=status
    )

    logging.info(f"{datetime.utcnow().isoformat()} | user={user} | type={project_type} | stack={stack} | status={status}")

    return jsonify({
        "success": True,
        "status": status,
        "code": code,
        "preview_url": preview_url
    }), 200
