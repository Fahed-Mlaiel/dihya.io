"""
Module Environnement - Gestion avancée des projets IA, VR, AR dans le secteur environnemental.
Sécurité, i18n, multitenancy, plugins, auditabilité RGPD.
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flask_babel import _
from .policy import ENV_POLICIES
from ...utils.security import role_required, validate_payload, waf_protect
from ...utils.audit import audit_log
from ...utils.i18n import get_locale
from ...utils.plugins import plugin_hook
from ...utils.ai import ai_fallback

environnement_bp = Blueprint('environnement', __name__, url_prefix='/api/environnement')

@environnement_bp.before_request
def before():
    waf_protect(request)
    audit_log(request, module='environnement')

@environnement_bp.route('/', methods=['GET'])
@jwt_required()
@role_required(['admin', 'user', 'invite'])
def list_projects():
    locale = get_locale()
    projects = plugin_hook('environnement_list_projects', default=[{"id": 1, "name": _(u"Projet Environnement Démo", locale=locale)}])
    return jsonify(projects)

@environnement_bp.route('/', methods=['POST'])
@jwt_required()
@role_required(['admin'])
@validate_payload(['name', 'description'])
def create_project():
    data = request.json
    result = plugin_hook('environnement_create_project', default=data)
    if not result:
        result = ai_fallback('environnement', data)
    return jsonify(result), 201
