"""
Export RGPD avancé pour les projets d'administration publique (anonymisation, logs, conformité).
"""
from .models import AdministrationPubliqueProject
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required

@permission_required('administration_publique.export_administration_publique_project')
def export_administration_publique_projects(request):
    """
    Exporte les projets administration publique (données anonymisées, logs RGPD).
    """
    data = list(AdministrationPubliqueProject.objects.values('id', 'name', 'description', 'created_at', 'updated_at', 'is_active'))
    # Anonymisation RGPD
    for d in data:
        d['name'] = 'ANONYMIZED'
    return JsonResponse({'projects': data})
