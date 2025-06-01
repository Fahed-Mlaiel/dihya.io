"""
Blueprint-Export für Social (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.social import blueprint
except ImportError:
    blueprint = None
