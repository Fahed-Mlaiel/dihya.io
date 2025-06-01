"""
Blueprint export pour IA (centralisé, multilingue, sécurisé, fallback-ready)
Ce module remplace toute référence à ia/intelligence_artificielle dans le backend.
"""
try:
    from backend.flask.app.templates.ai import blueprint as ai_blueprint
except ImportError:
    try:
        from backend.flask.app.templates.ai import bp_ai as ai_blueprint
    except ImportError:
        ai_blueprint = None

# Sécurité, audit, i18n, fallback IA/AI
from backend.flask.app.utils.ai import ai_fallback


"""
Module métier AI Dihya (Flask).
Inclut : services, schémas, plugins, validation, audit, i18n, tests, documentation.
Ultra avancé, extensible, sécurisé, RGPD, production-ready.
"""

from .services import *
from .schemas import *
from .plugins import *
from .validators import *
from .audit import *
from .i18n import *

__all__ = [
    "services", "schemas", "plugins", "validators", "audit", "i18n"
]
