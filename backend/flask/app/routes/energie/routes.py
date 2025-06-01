"""
Blueprint-Export für Energie (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.energie import energie_bp as energie_blueprint
except ImportError:
    energie_blueprint = None
except Exception:
    energie_blueprint = None
