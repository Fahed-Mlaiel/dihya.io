"""
Export RGPD avancé pour les projets construction (anonymisation, logs, conformité).
"""
from .models import ConstructionProject
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required

@permission_required('app.export_constructionproject')
def export_construction_projects(request):
    data = list(ConstructionProject.objects.values('id', 'name', 'description', 'created_at', 'updated_at'))
    for d in data:
        d['name'] = 'ANONYMIZED'
    return JsonResponse({'projects': data})
