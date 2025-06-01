"""
Blueprint-Export für Services Personne (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.services_personne import blueprint
except ImportError:
    blueprint = None
