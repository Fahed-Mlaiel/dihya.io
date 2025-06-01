"""
routes.py - Routes RESTful/GraphQL pour la gestion de projets voice/IA vocale
Sécurité maximale, multitenancy, i18n, plugins, audit, fallback IA, SEO, RGPD
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin
from flask_babel import gettext as _
from typing import Any

from ..utils import validate_project_ia, audit_log, get_tenant, get_locale, get_plugins, fallback_ia, anonymize_data, export_projects
from ..utils.security import waf_protect, anti_ddos_protect, rbac_required
from ..utils.seo import seo_headers
from ..utils.logging import structured_log
from ..utils.graphql import graphql_ia_schema

bp = Blueprint('routes_voice', __name__, url_prefix='/api/voice')

@bp.before_request
def before_request():
    waf_protect()
    anti_ddos_protect()
    seo_headers()
    structured_log(request)

@bp.route('/projects', methods=['GET'])
@cross_origin()
@jwt_required()
@rbac_required(['admin', 'user', 'invité'])
def list_projects_voice() -> Any:
    """Lister les projets voice/IA vocale (multitenancy, i18n, audit, plugins, fallback IA, RGPD, accessibilité, SEO).
    Returns:
        JSON: Liste des projets voice filtrés selon tenant, rôle, langue, plugins, fallback IA, RGPD, accessibilité, SEO.
    """
    user = get_jwt_identity()
    tenant = get_tenant(user)
    locale = get_locale(request)
    plugins = get_plugins(tenant)
    projects = fallback_ia(tenant, plugins, locale)
    projects = anonymize_data(projects, user)
    audit_log(user, 'list_projects_voice', tenant, locale)
    export = request.args.get('export')
    if export:
        return export_projects(projects, format=export)
    return jsonify({'projects': projects, 'locale': locale, 'tenant': tenant}), 200

@bp.route('/projects', methods=['POST'])
@cross_origin()
@jwt_required()
@rbac_required(['admin', 'user'])
def create_project_voice() -> Any:
    """Créer un projet voice/IA vocale (validation, audit, plugins, RGPD, accessibilité, SEO).
    Returns:
        JSON: Projet voice créé ou erreur de validation.
    """
    user = get_jwt_identity()
    tenant = get_tenant(user)
    locale = get_locale(request)
    data = request.get_json()
    valid, errors = validate_project_ia(data, locale)
    if not valid:
        structured_log({'event': 'validation_error', 'errors': errors, 'user': user, 'tenant': tenant})
        return jsonify({'error': _('Validation error'), 'details': errors}), 400
    plugins = get_plugins(tenant)
    project = fallback_ia(tenant, plugins, locale, data)
    project = anonymize_data(project, user)
    audit_log(user, 'create_project_voice', tenant, locale, project)
    return jsonify({'msg': _('Projet voice/IA vocale créé'), 'project': project}), 201

# GraphQL endpoint (exemple)
@bp.route('/graphql', methods=['POST'])
@cross_origin()
@jwt_required()
@rbac_required(['admin', 'user', 'invité'])
def graphql_voice() -> Any:
    """Endpoint GraphQL voice (sécurité, plugins, audit, RGPD, SEO, accessibilité)."""
    user = get_jwt_identity()
    tenant = get_tenant(user)
    locale = get_locale(request)
    data = request.get_json()
    result = graphql_ia_schema.execute(data.get('query'), context_value={'user': user, 'tenant': tenant, 'locale': locale})
    audit_log(user, 'graphql_voice', tenant, locale, data)
    return jsonify(result.data), 200

voice_bp = bp
