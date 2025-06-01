"""
Blueprint-Export für Crypto (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.crypto import crypto_bp as crypto_blueprint
except ImportError:
    crypto_blueprint = None
except Exception:
    crypto_blueprint = None
