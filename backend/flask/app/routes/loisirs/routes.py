"""
Blueprint-Export für Loisirs (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.loisirs import blueprint
except ImportError:
    blueprint = None
