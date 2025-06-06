"""
Endpoint d’export de logs d’audit filtrable (user/tenant/date) pour le module 3D (Dihya)
"""
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .audit import threed_audit_logger

@require_GET
def export_audit_logs(request):
    user = request.GET.get('user')
    tenant = request.GET.get('tenant')
    date = request.GET.get('date')
    logs = threed_audit_logger.audit_log
    if user:
        logs = [l for l in logs if l.get('user') == user]
    if tenant:
        logs = [l for l in logs if l.get('tenant') == tenant]
    if date:
        logs = [l for l in logs if l.get('timestamp', '').startswith(date)]
    return JsonResponse({'logs': logs})
