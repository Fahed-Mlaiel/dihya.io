"""
Exemple ultra avancé : API FastAPI (OpenAPI, audit, RGPD, i18n, plugins, tests, accessibilité, CI/CD)
"""
from fastapi import FastAPI, Request, HTTPException
from plugins.audit_plugin import log_action
from plugins.rgpd_plugin import check_consent
from plugins.i18n_plugin import translate

app = FastAPI()

@app.get('/api/secure-data')
async def secure_data(request: Request):
    lang = request.headers.get('accept-language', 'fr')
    if not check_consent(request):
        raise HTTPException(status_code=403, detail=translate('Consentement RGPD requis', lang))
    log_action('access', 'secure-data', user='anonymous', lang=lang)
    return {'message': translate('Données sécurisées', lang), 'lang': lang}
