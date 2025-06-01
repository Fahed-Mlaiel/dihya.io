"""
plugin.py - Exemple de plugin Dihya (Python)
Plugin extensible, sécurisé, internationalisé, documenté
"""
def init_plugin(app, options=None):
    """Initialise le plugin exemple pour Dihya.
    :param app: Flask app
    :param options: dict d'options
    """
    @app.route('/api/plugins/exemple', methods=['GET'])
    def exemple_plugin():
        lang = (app.current_request.headers.get('Accept-Language') or 'fr')
        messages = {
            'fr': 'Plugin exemple actif',
            'en': 'Example plugin active',
            'ar': 'الإضافة نشطة',
            'de': 'Beispiel-Plugin aktiv',
            'zh': '示例插件已激活',
            'ja': 'サンプルプラグインが有効です',
            'ko': '예제 플러그인이 활성화됨',
            'nl': 'Voorbeeldplugin actief',
            'he': 'תוסף לדוגמה פעיל',
            'fa': 'افزونه نمونه فعال است',
            'hi': 'उदाहरण प्लगइन सक्रिय है',
            'es': 'Plugin de ejemplo activo'
        }
        return {"message": messages.get(lang, messages['fr']), "lang": lang}
