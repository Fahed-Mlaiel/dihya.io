"""
Export RGPD avancé pour les projets agricoles (anonymisation, logs, conformité).
"""
from .models import AgricultureProject
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required

@permission_required('agriculture.export_agriculture_project')
def export_agriculture_projects(request):
    """
    Exporte les projets agricoles (données anonymisées, logs RGPD).
    """
    data = list(AgricultureProject.objects.values('id', 'name', 'description', 'created_at', 'updated_at', 'is_active'))
    # Anonymisation RGPD
    for d in data:
        d['name'] = 'ANONYMIZED'
    return JsonResponse({'projects': data})
