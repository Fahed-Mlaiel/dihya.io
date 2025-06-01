"""
Blueprint-Export für Culture (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.culture import blueprint
except ImportError:
    blueprint = None
