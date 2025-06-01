"""
Blueprint-Export für Immobilier (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.immobilier import blueprint
except ImportError:
    blueprint = None
