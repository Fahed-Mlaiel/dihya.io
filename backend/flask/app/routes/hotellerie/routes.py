"""
Blueprint-Export für Hotellerie (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.hotellerie import blueprint
except ImportError:
    blueprint = None
