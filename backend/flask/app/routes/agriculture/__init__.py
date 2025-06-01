"""
Blueprint-Export für Agriculture (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.agriculture import blueprint
except ImportError:
    blueprint = None
