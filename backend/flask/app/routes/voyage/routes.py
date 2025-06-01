"""
Blueprint-Export für Voyage (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.voyage import blueprint
except ImportError:
    blueprint = None
