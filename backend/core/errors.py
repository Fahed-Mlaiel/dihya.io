"""
Gestion centralisée des erreurs backend Dihya (Flask)
- Sécurité, RGPD, multilingue, audit, plugins, CI/CD-ready
"""
from flask import jsonify, request

def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'error': {
                'fr': "Requête invalide",
                'en': "Bad request",
                'ar': "طلب غير صالح",
                'tzm': "Aɣbalu ur yettwafaq ara"
            }.get(request.headers.get('X-Dihya-Lang', 'fr'), "Requête invalide"),
            'details': str(error)
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'error': {
                'fr': "Non autorisé",
                'en': "Unauthorized",
                'ar': "غير مصرح",
                'tzm': "Ulac tasireft"
            }.get(request.headers.get('X-Dihya-Lang', 'fr'), "Non autorisé"),
            'details': str(error)
        }), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'error': {
                'fr': "Accès refusé",
                'en': "Access denied",
                'ar': "وصول مرفوض",
                'tzm': "Ulac tasireft"
            }.get(request.headers.get('X-Dihya-Lang', 'fr'), "Accès refusé"),
            'details': str(error)
        }), 403

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'error': {
                'fr': "Non trouvé",
                'en': "Not found",
                'ar': "غير موجود",
                'tzm': "Ulac"
            }.get(request.headers.get('X-Dihya-Lang', 'fr'), "Non trouvé"),
            'details': str(error)
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            'error': {
                'fr': "Erreur interne serveur",
                'en': "Internal server error",
                'ar': "خطأ داخلي في الخادم",
                'tzm': "Tuccfa n uẓerrig"
            }.get(request.headers.get('X-Dihya-Lang', 'fr'), "Erreur interne serveur"),
            'details': str(error)
        }), 500
