"""
Blueprint-Export für 3D (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.threed import blueprint
except ImportError:
    blueprint = None
