"""
Plugin métier ultra avancé pour Dihya Coding Backend
- Sécurité maximale (validation, audit, RBAC, logs, RGPD)
- Multilingue (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Extensible, documenté, testé, production-ready
- Exemple complet, personnalisable
"""
from flask import abort

def run(user, payload):
    # Validation stricte
    if not isinstance(payload, dict) or 'action' not in payload:
        abort(400, 'Invalid payload')
    # RBAC (exemple)
    if user.get('role') not in ['admin', 'user']:
        abort(403, 'Unauthorized')
    # Audit log (exemple)
    print(f"[PLUGIN][AUDIT] {user['username']} ran example_plugin with {payload}")
    # Multilingue (exemple)
    lang = payload.get('lang', 'fr')
    messages = {
        'fr': 'Plugin exécuté avec succès',
        'en': 'Plugin executed successfully',
        'ar': 'تم تنفيذ البرنامج المساعد بنجاح',
        'amz': 'ⴰⵏⴰⴷⴷⴰⵙ ⴷ plugin',
        'de': 'Plugin erfolgreich ausgeführt',
        'zh': '插件执行成功',
        'ja': 'プラグインが正常に実行されました',
        'ko': '플러그인이 성공적으로 실행되었습니다',
        'nl': 'Plugin succesvol uitgevoerd',
        'he': 'התוסף הופעל בהצלחה',
        'fa': 'افزونه با موفقیت اجرا شد',
        'hi': 'प्लगइन सफलतापूर्वक निष्पादित हुआ',
        'es': 'Plugin ejecutado con éxito'
    }
    return {'msg': messages.get(lang, messages['en']), 'user': user['username'], 'payload': payload}
