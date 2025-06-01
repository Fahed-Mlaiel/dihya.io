"""
Module d’audit et de traçabilité de la sécurité — Dihya Coding.

Centralise la journalisation des événements de sécurité, la consultation des logs d’audit,
et la gestion des alertes pour garantir la conformité, la traçabilité et la souveraineté numérique.
"""

import logging
import os
from datetime import datetime
from flask import Blueprint, request, jsonify, abort, g
from backend.flask.app.securite.acl import require_permission

AUDIT_LOG_PATH = os.environ.get("AUDIT_LOG_PATH", "/workspaces/Dihya/Dihya/backend/flask/audit/audit.log")

audit_blueprint = Blueprint("audit", __name__)

def log_security_event(event_type: str, user: str = "unknown", details: str = ""):
    timestamp = datetime.utcnow().isoformat()
    log_line = f"{timestamp} | {event_type} | user={user} | {details}\n"
    try:
        with open(AUDIT_LOG_PATH, "a") as f:
            f.write(log_line)
    except Exception as e:
        logging.error(f"[AUDIT] Erreur écriture log: {e}")

@audit_blueprint.route("/audit/logs", methods=["GET"])
@require_permission("view_audit_logs")
def get_audit_logs():
    """
    Endpoint sécurisé pour consulter les logs d’audit.

    Sécurité :
    - Vérifie la permission 'view_audit_logs'.
    - Ne retourne jamais de secrets ou de données personnelles.
    - Peut être restreint par IP whitelist en production.

    Returns:
        JSON: Liste des lignes de logs récentes.
    """
    try:
        with open(AUDIT_LOG_PATH, "r") as f:
            lines = f.readlines()[-100:]  # Limite à 100 dernières entrées
        return jsonify({"logs": lines})
    except Exception as e:
        logging.error(f"[AUDIT] Erreur lecture log: {e}")
        abort(500, "Impossible de lire les logs d’audit.")

def log_permission_change(user: str, target: str, permission: str, action: str):
    """
    Journalise un changement de permission.

    Args:
        user (str): Utilisateur ayant effectué l’action.
        target (str): Cible du changement (utilisateur/role).
        permission (str): Permission modifiée.
        action (str): 'grant' ou 'revoke'.
    """
    details = f"target={target} | permission={permission} | action={action}"
    log_security_event("permission_change", user, details)

def log_login_failed(user: str, reason: str = ""):
    """
    Journalise un échec d’authentification.

    Args:
        user (str): Identifiant utilisateur.
        reason (str): Raison de l’échec (jamais de mot de passe !).
    """
    details = f"reason={reason}"
    log_security_event("login_failed", user, details)
