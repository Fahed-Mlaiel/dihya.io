"""
Module d'API pour la gestion avancée des projets social.
Sécurité, i18n, audit, plugins, conformité RGPD, multitenancy, SEO.
"""
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_babel import _
from .utils import validate_project_payload, role_required, log_audit_event
from .plugins import run_plugin_hooks
from .i18n import get_locale

bp = Blueprint('social', __name__, url_prefix='/api/social')

@bp.route('/projects', methods=['GET'])
@jwt_required()
@role_required(['admin', 'user'])
def list_projects():
    tenant = get_jwt_identity().get('tenant')
    projects = current_app.db.get_social_projects(tenant=tenant)
    log_audit_event('list_social_projects', tenant=tenant)
    return jsonify({'projects': projects, 'msg': _('Liste des projets social')})

@bp.route('/projects', methods=['POST'])
@jwt_required()
@role_required(['admin'])
def create_project():
    data = request.json
    validate_project_payload(data)
    tenant = get_jwt_identity().get('tenant')
    project = current_app.db.create_social_project(data, tenant=tenant)
    run_plugin_hooks('after_create_social_project', project)
    log_audit_event('create_social_project', tenant=tenant, details=project)
    return jsonify({'project': project, 'msg': _('Projet social créé')}), 201

@bp.route('/projects/<project_id>', methods=['GET'])
@jwt_required()
@role_required(['admin', 'user', 'invité'])
def get_project(project_id):
    tenant = get_jwt_identity().get('tenant')
    project = current_app.db.get_social_project(project_id, tenant=tenant)
    log_audit_event('get_social_project', tenant=tenant, details=project)
    return jsonify({'project': project, 'msg': _('Projet social récupéré')})

# SEO, robots, sitemap
@bp.route('/robots.txt')
def robots():
    return "User-agent: *\nDisallow: /api/", 200, {'Content-Type': 'text/plain'}

@bp.route('/sitemap.xml')
def sitemap():
    return current_app.generate_sitemap('social'), 200, {'Content-Type': 'application/xml'}

def get_template(*args, **kwargs):
    return None
