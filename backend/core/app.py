"""
Dihya Backend Core – Initialisation Flask ultra avancée
- Sécurité maximale, multilingue, RBAC, plugins, audit, conformité RGPD, extensibilité, logs structurés, CI/CD-ready
"""
from flask import Flask
from .security import register_security, RBACMiddleware
from .plugins import load_plugins
from .routes import register_routes
from .logic import init_core_logic
from .errors import register_error_handlers
from .utils import log_structured
from flask_socketio import SocketIO, emit
import logging
import os

DASHBOARD_MD_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../dashboard_global.md'))

socketio = SocketIO()


def create_app(config_object=None):
    app = Flask(__name__)
    if config_object:
        app.config.from_object(config_object)
    # Sécurité, RBAC, logs, audit
    register_security(app)
    app.wsgi_app = RBACMiddleware(app.wsgi_app)
    # Plugins dynamiques
    load_plugins(app)
    # Logique métier centrale
    init_core_logic(app)
    # Routes principales
    register_routes(app)
    # Gestion centralisée des erreurs
    register_error_handlers(app)
    # Logs structurés
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    app.logger.info("Dihya Backend Core initialisé (Flask, sécurité, multilingue, plugins, audit, CI/CD)")
    log_structured('info', 'Dihya Backend Core initialisé', module='core', lang='fr')
    socketio.init_app(app, cors_allowed_origins="*")
    return app

@socketio.on('connect', namespace='/ws/dashboard')
def dashboard_connect():
    emit('dashboard', _read_dashboard_md())

@socketio.on('refresh', namespace='/ws/dashboard')
def dashboard_refresh():
    emit('dashboard', _read_dashboard_md())

def _read_dashboard_md():
    try:
        with open(DASHBOARD_MD_PATH, encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Erreur lecture dashboard: {e}"

if __name__ == "__main__":
    app = create_app()
    socketio.run(app, host="0.0.0.0", port=8000)
