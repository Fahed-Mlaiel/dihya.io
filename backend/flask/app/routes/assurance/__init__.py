"""
Blueprint-Export für Assurance (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.assurance import blueprint as assurance_blueprint
except ImportError:
    from backend.flask.app.templates.assurance import bp_assurance as assurance_blueprint
except Exception:
    assurance_blueprint = None
