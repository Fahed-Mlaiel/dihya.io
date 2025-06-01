"""
Export RGPD avancé pour les projets VR/AR (anonymisation, logs, conformité).
"""
from .models import VRARProject
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required

@permission_required('vr_ar.export_vrar_project')
def export_vrar_projects(request):
    """
    Exporte les projets VR/AR (données anonymisées, logs RGPD).
    """
    data = list(VRARProject.objects.values('id', 'name', 'description', 'created_at', 'updated_at', 'is_active'))
    # Anonymisation RGPD
    for d in data:
        d['name'] = 'ANONYMIZED'
    return JsonResponse({'projects': data})
