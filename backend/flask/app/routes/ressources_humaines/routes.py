"""
Blueprint-Export für Ressources Humaines (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.ressources_humaines import blueprint
except ImportError:
    blueprint = None
