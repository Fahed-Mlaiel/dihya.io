"""
Blueprint-Export für Mobile (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.mobile import blueprint
except ImportError:
    blueprint = None
