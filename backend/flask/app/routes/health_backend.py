"""
Blueprint-Export für Health Backend (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.health.backend import blueprint
except ImportError:
    blueprint = None
