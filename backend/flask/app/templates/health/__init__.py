"""
Module Health - Gestion avancée des projets IA, VR, AR dans le secteur santé.
Sécurité, i18n, multitenancy, plugins, auditabilité RGPD.
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flask_babel import _
from .policy import HEALTH_POLICIES
from ...utils.security import role_required, validate_payload, waf_protect
from ...utils.audit import audit_log
from ...utils.i18n import get_locale
from ...utils.plugins import plugin_hook
from ...utils.ai import ai_fallback

health_bp = Blueprint('health', __name__, url_prefix='/api/health')

@health_bp.before_request
def before():
    waf_protect(request)
    audit_log(request, module='health')

@health_bp.route('/', methods=['GET'])
@jwt_required()
@role_required(['admin', 'user', 'invite'])
def list_projects():
    locale = get_locale()
    projects = plugin_hook('health_list_projects', default=[{"id": 1, "name": _(u"Projet Health Démo", locale=locale)}])
    return jsonify(projects)

@health_bp.route('/', methods=['POST'])
@jwt_required()
@role_required(['admin'])
@validate_payload(['name', 'description'])
def create_project():
    data = request.json
    result = plugin_hook('health_create_project', default=data)
    if not result:
        result = ai_fallback('health', data)
    return jsonify(result), 201
