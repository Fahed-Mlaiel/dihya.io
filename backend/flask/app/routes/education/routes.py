"""
Blueprint-Export für Education (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.education import education_bp as education_blueprint
except ImportError:
    education_blueprint = None
except Exception:
    education_blueprint = None
