"""
Blueprint-Export für Juridique (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.juridique import blueprint
except ImportError:
    blueprint = None
