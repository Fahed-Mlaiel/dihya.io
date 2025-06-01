"""
Blueprint export for AI (centralisé, multilingue, sécurisé, fallback-ready)
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
