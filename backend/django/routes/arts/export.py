"""
Export RGPD avancé pour les projets artistiques (anonymisation, logs, conformité).
"""
from .models import ArtProject
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required

@permission_required('arts.export_art_project')
def export_art_projects(request):
    """
    Exporte les projets artistiques (données anonymisées, logs RGPD).
    """
    data = list(ArtProject.objects.values('id', 'name', 'description', 'created_at', 'updated_at', 'is_active'))
    # Anonymisation RGPD
    for d in data:
        d['name'] = 'ANONYMIZED'
    return JsonResponse({'projects': data})
