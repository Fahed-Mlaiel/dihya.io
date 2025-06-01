"""
Blueprint-Export für Gamer (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.gamer import blueprint
except ImportError:
    blueprint = None
