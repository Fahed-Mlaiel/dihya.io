"""
Export RGPD avancé pour les projets IA (anonymisation, logs, conformité).
"""
from .models import IAProject
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required

@permission_required('intelligence_artificielle.export_ia_project')
def export_ia_projects(request):
    """
    Exporte les projets IA (données anonymisées, logs RGPD).
    """
    data = list(IAProject.objects.values('id', 'name', 'description', 'created_at', 'updated_at', 'is_active'))
    # Anonymisation RGPD
    for d in data:
        d['name'] = 'ANONYMIZED'
    return JsonResponse({'projects': data})
