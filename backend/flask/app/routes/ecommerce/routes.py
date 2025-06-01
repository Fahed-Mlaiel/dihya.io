"""
Blueprint-Export für Ecommerce (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.ecommerce import blueprint
except ImportError:
    blueprint = None
