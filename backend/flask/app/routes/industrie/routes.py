"""
Blueprint-Export für Industrie (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.industrie import blueprint
except ImportError:
    blueprint = None
