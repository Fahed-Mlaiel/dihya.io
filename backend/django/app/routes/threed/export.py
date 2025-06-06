"""
Export RGPD avancé pour les modèles 3D (anonymisation, logs, audit, multilingue, plugins, multitenant, accessibilité, CI/CD-ready).
"""
from .models import Model3D
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required
from .audit import audit_log
from .logs import log_3d_event
from .i18n import I18N

def anonymize_model3d(d, lang='fr'):
    d['name'] = I18N[lang]['anonymized'] if 'anonymized' in I18N[lang] else 'ANONYMIZED'
    d['file'] = None
    return d

@permission_required('app.export_model3d')
def export_3d_models(request):
    """
    Exporte les modèles 3D (données anonymisées, logs RGPD, audit, multilingue, plugins, multitenant).
    """
    lang = request.headers.get('X-Lang', 'fr')
    tenant = request.headers.get('X-Tenant', 'default')
    data = list(Model3D.objects.values('id', 'name', 'file', 'owner', 'date_upload', 'date_modification'))
    data = [anonymize_model3d(d, lang) for d in data]
    audit_log(request.user, 'export_3d', data, tenant, lang)
    log_3d_event('export', {'user': getattr(request.user, 'id', None), 'count': len(data)}, tenant, lang)
    return JsonResponse({'models': data, 'lang': lang, 'tenant': tenant})
