"""
Module d'API pour la gestion avancée des modules SEO backend.
Sécurité, i18n, audit, plugins, conformité RGPD, multitenancy, SEO.
"""
from flask import Blueprint, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_babel import _
from .utils import role_required, log_audit_event
from .plugins import run_plugin_hooks
from .i18n import get_locale
from backend.flask.app.utils.seo import generate_robots_txt, generate_sitemap

bp = Blueprint('seo', __name__, url_prefix='/api/seo')

@bp.route('/robots.txt')
def robots():
    """Fichier robots.txt dynamique pour SEO."""
    return generate_robots_txt(), 200, {'Content-Type': 'text/plain'}

@bp.route('/sitemap.xml')
def sitemap():
    """Sitemap dynamique pour SEO."""
    urls = ['/', '/api/seo', '/api/health']  # Beispiel-URLs, in Produktion dynamisch generieren
    base_url = 'https://dihya.ai'  # In Produktion dynamisch bestimmen
    return generate_sitemap(urls, base_url), 200, {'Content-Type': 'application/xml'}

@bp.route('/logs', methods=['GET'])
@jwt_required()
@role_required(['admin'])
def get_logs():
    """Accès aux logs structurés SEO (admin only)."""
    tenant = get_jwt_identity().get('tenant')
    logs = current_app.db.get_seo_logs(tenant=tenant)
    log_audit_event('get_seo_logs', tenant=tenant)
    return jsonify({'logs': logs, 'msg': _('Logs SEO récupérés')})

bp_seo = bp
__all__ = ["bp", "bp_seo"]
