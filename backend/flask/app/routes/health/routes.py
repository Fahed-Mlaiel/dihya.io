"""
Blueprint-Export für Health (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.health import blueprint
except ImportError:
    blueprint = None
