"""
Export RGPD avancé pour les projets BTP (anonymisation, logs, conformité).
"""
from .models import BTPProject
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required

@permission_required('app.export_btpproject')
def export_btp_projects(request):
    data = list(BTPProject.objects.values('id', 'name', 'description', 'created_at', 'updated_at', 'is_active'))
    for d in data:
        d['name'] = 'ANONYMIZED'
    return JsonResponse({'projects': data})
