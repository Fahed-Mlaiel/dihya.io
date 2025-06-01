"""
Blueprint-Export für Voice (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.voice import blueprint
except ImportError:
    blueprint = None
