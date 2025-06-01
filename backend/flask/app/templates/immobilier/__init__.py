"""
Module Immobilier - Gestion avancée des projets IA, VR, AR dans le secteur immobilier.
Sécurité, i18n, multitenancy, plugins, auditabilité RGPD.
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flask_babel import _
from .policy import IMMO_POLICIES
from ...utils.security import role_required, validate_payload, waf_protect
from ...utils.audit import audit_log
from ...utils.i18n import get_locale
from ...utils.plugins import plugin_hook
from ...utils.ai import ai_fallback

immobilier_bp = Blueprint('immobilier', __name__, url_prefix='/api/immobilier')

@immobilier_bp.before_request
def before():
    waf_protect(request)
    audit_log(request, module='immobilier')

@immobilier_bp.route('/', methods=['GET'])
@jwt_required()
@role_required(['admin', 'user', 'invite'])
def list_projects():
    locale = get_locale()
    projects = plugin_hook('immobilier_list_projects', default=[{"id": 1, "name": _(u"Projet Immobilier Démo", locale=locale)}])
    return jsonify(projects)

@immobilier_bp.route('/', methods=['POST'])
@jwt_required()
@role_required(['admin'])
@validate_payload(['name', 'description'])
def create_project():
    data = request.json
    result = plugin_hook('immobilier_create_project', default=data)
    if not result:
        result = ai_fallback('immobilier', data)
    return jsonify(result), 201
