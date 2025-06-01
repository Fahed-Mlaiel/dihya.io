"""
Blueprint-Export für Medias (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.medias import blueprint
except ImportError:
    blueprint = None
