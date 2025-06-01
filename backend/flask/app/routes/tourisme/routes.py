"""
Blueprint-Export für Tourisme (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.tourisme import blueprint
except ImportError:
    blueprint = None
