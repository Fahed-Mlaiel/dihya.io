"""
Blueprint-Export für Arts (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.arts import arts_bp as arts_blueprint
except ImportError:
    from backend.flask.app.templates.arts import bp_arts as arts_blueprint
except Exception:
    arts_blueprint = None
