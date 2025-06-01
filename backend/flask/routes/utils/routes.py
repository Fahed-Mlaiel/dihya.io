"""
routes.py - Routes RESTful/GraphQL utilitaires (outils, diagnostics, helpers, plugins)
Sécurité maximale, multitenancy, i18n, plugins, audit, fallback IA, SEO, RGPD
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin
from flask_babel import gettext as _
from typing import Any

from .utils import audit_log, get_tenant, get_locale, get_plugins, anonymize_data, export_diagnostics
from .security import waf_protect, anti_ddos_protect, rbac_required
from .seo import seo_headers
from .logging import structured_log
from .graphql import graphql_utils_schema

bp = Blueprint('routes_utils', __name__, url_prefix='/api/utils')

@bp.before_request
def before_request():
    waf_protect()
    anti_ddos_protect()
    seo_headers()
    structured_log(request)

@bp.route('/diagnostics', methods=['GET'])
@cross_origin()
@jwt_required()
@rbac_required(['admin', 'user'])
def diagnostics() -> Any:
    """Diagnostics système (audit, plugins, RGPD, multitenancy, export, anonymisation, accessibilité, SEO).
    Returns:
        JSON: Diagnostics filtrés selon tenant, plugins, RGPD, accessibilité, SEO.
    """
    user = get_jwt_identity()
    tenant = get_tenant(user)
    locale = get_locale(request)
    plugins = get_plugins(tenant)
    diagnostics = {'status': _('ok'), 'plugins': plugins, 'tenant': tenant, 'locale': locale}
    diagnostics = anonymize_data(diagnostics, user)
    audit_log(user, 'diagnostics', tenant, locale)
    export = request.args.get('export')
    if export:
        return export_diagnostics(diagnostics, format=export)
    return jsonify(diagnostics), 200

@bp.route('/tools', methods=['POST'])
@cross_origin()
@jwt_required()
@rbac_required(['admin'])
def run_tool() -> Any:
    """Exécuter un outil utilitaire (validation, audit, plugins, RGPD, accessibilité, SEO).
    Returns:
        JSON: Résultat de l’outil ou erreur de validation.
    """
    user = get_jwt_identity()
    tenant = get_tenant(user)
    locale = get_locale(request)
    data = request.get_json()
    tool = data.get('tool')
    plugins = get_plugins(tenant)
    # Validation stricte du nom d’outil
    if not tool or tool not in plugins.get('tools', []):
        structured_log({'event': 'validation_error', 'user': user, 'tenant': tenant, 'tool': tool})
        return jsonify({'error': _('Outil non autorisé')}), 400
    result = {'msg': _('Outil exécuté'), 'tool': tool, 'tenant': tenant, 'locale': locale}
    result = anonymize_data(result, user)
    audit_log(user, 'run_tool', tenant, locale, result)
    return jsonify(result), 201

# GraphQL endpoint (exemple)
@bp.route('/graphql', methods=['POST'])
@cross_origin()
@jwt_required()
@rbac_required(['admin', 'user'])
def graphql_utils() -> Any:
    """Endpoint GraphQL utilitaires (sécurité, plugins, audit, RGPD, SEO, accessibilité)."""
    user = get_jwt_identity()
    tenant = get_tenant(user)
    locale = get_locale(request)
    data = request.get_json()
    result = graphql_utils_schema.execute(data.get('query'), context_value={'user': user, 'tenant': tenant, 'locale': locale})
    audit_log(user, 'graphql_utils', tenant, locale, data)
    return jsonify(result.data), 200
