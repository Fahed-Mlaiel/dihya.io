"""
Blueprint-Export für Utils (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.utils import blueprint
except ImportError:
    blueprint = None
