"""
Module d'API pour la gestion avancée des projets science.
Sécurité, i18n, audit, plugins, conformité RGPD, multitenancy, SEO.
"""
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_babel import _
from .utils import validate_project_payload, role_required, log_audit_event
from .plugins import run_plugin_hooks
from .i18n import get_locale

bp = Blueprint('science', __name__, url_prefix='/api/science')

@bp.route('/projects', methods=['GET'])
@jwt_required()
@role_required(['admin', 'user'])
def list_projects():
    tenant = get_jwt_identity().get('tenant')
    projects = current_app.db.get_science_projects(tenant=tenant)
    log_audit_event('list_science_projects', tenant=tenant)
    return jsonify({'projects': projects, 'msg': _('Liste des projets science')})

@bp.route('/projects', methods=['POST'])
@jwt_required()
@role_required(['admin'])
def create_project():
    data = request.json
    validate_project_payload(data)
    tenant = get_jwt_identity().get('tenant')
    project = current_app.db.create_science_project(data, tenant=tenant)
    run_plugin_hooks('after_create_science_project', project)
    log_audit_event('create_science_project', tenant=tenant, details=project)
    return jsonify({'project': project, 'msg': _('Projet science créé')}), 201

@bp.route('/projects/<project_id>', methods=['GET'])
@jwt_required()
@role_required(['admin', 'user', 'invité'])
def get_project(project_id):
    tenant = get_jwt_identity().get('tenant')
    project = current_app.db.get_science_project(project_id, tenant=tenant)
    log_audit_event('get_science_project', tenant=tenant, details=project)
    return jsonify({'project': project, 'msg': _('Projet science récupéré')})

# SEO, robots, sitemap
@bp.route('/robots.txt')
def robots():
    return "User-agent: *\nDisallow: /api/", 200, {'Content-Type': 'text/plain'}

@bp.route('/sitemap.xml')
def sitemap():
    return current_app.generate_sitemap('science'), 200, {'Content-Type': 'application/xml'}

bp_science = bp
__all__ = ["bp", "bp_science"]
