"""
Blueprint-Export für Recherche (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.recherche import blueprint
except ImportError:
    blueprint = None
