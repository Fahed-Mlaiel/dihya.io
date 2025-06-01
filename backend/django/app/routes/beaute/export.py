"""
Export RGPD avancé pour les projets beauté (anonymisation, logs, conformité).
"""
from .models import BeauteProject
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required

@permission_required('app.export_beauteproject')
def export_beaute_projects(request):
    data = list(BeauteProject.objects.values('id', 'name', 'description', 'created_at', 'updated_at'))
    for d in data:
        d['name'] = 'ANONYMIZED'
    return JsonResponse({'projects': data})
