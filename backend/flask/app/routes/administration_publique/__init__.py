"""
Blueprint-Export für Administration Publique (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.administration_publique import blueprint
except ImportError:
    blueprint = None
