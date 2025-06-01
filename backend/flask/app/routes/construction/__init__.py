"""
Blueprint-Export für Construction (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.construction import blueprint
except ImportError:
    blueprint = None
