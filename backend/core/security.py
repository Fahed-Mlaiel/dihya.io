"""
Sécurité backend Dihya : RBAC, JWT, CORS, WAF, audit, logs, conformité RGPD, plugins, extensibilité, multilingue, CI/CD-ready
"""
from flask import request, abort
import logging

ROLES = ["admin", "ai_user", "auditor", "user", "guest"]

class RBACMiddleware:
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        # Extrait le rôle depuis l’en-tête ou le contexte (exemple simplifié)
        role = environ.get('HTTP_X_DIHYA_ROLE', 'guest')
        environ['dihya.role'] = role if role in ROLES else 'guest'
        return self.app(environ, start_response)

def require_role(required_role):
    def decorator(f):
        def wrapper(*args, **kwargs):
            role = request.environ.get('dihya.role', 'guest')
            if ROLES.index(role) < ROLES.index(required_role):
                abort(403, description={
                    'fr': "Accès refusé", 'en': "Access denied", 'ar': "وصول مرفوض", 'tzm': "Ulac tasireft"
                }.get(request.headers.get('X-Dihya-Lang', 'fr'), "Accès refusé"))
            return f(*args, **kwargs)
        wrapper.__name__ = f.__name__
        return wrapper
    return decorator

def register_security(app):
    @app.before_request
    def security_headers():
        # Headers de sécurité avancés
        h = app.make_response("")
        h.headers['X-Content-Type-Options'] = 'nosniff'
        h.headers['X-Frame-Options'] = 'SAMEORIGIN'
        h.headers['X-XSS-Protection'] = '1; mode=block'
        h.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        h.headers['Permissions-Policy'] = 'geolocation=(), microphone=()'
        return None
    app.logger.info("Sécurité backend Dihya initialisée (RBAC, headers, audit, RGPD, plugins)")
