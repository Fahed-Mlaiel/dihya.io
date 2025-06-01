"""
Blueprint-Export für IT DevOps (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.it_devops import blueprint
except ImportError:
    blueprint = None
