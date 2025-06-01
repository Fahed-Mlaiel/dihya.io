"""
Blueprint-Export für Environnement (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.environnement import blueprint
except ImportError:
    blueprint = None
