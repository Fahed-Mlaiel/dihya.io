"""
Exemple ultra avancé : API Flask (sécurité, RGPD, audit, i18n, plugins, accessibilité, CI/CD, tests)
"""
from flask import Flask, jsonify, request
from flask_cors import CORS
from plugins.audit_plugin import log_action
from plugins.rgpd_plugin import check_consent
from plugins.i18n_plugin import get_locale

app = Flask(__name__)
CORS(app)

@app.route('/api/secure-data', methods=['GET'])
def secure_data():
    user_locale = get_locale(request)
    if not check_consent(request):
        return jsonify({'error': 'Consentement RGPD requis'}), 403
    log_action('access', 'secure-data', user=request.remote_addr, locale=user_locale)
    return jsonify({'message': 'Données sécurisées', 'locale': user_locale})

if __name__ == '__main__':
    app.run(debug=True)
