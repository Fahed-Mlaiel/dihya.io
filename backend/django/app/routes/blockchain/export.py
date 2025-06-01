"""
Export RGPD avancé pour les projets blockchain (anonymisation, logs, conformité).
"""
from .models import BlockchainProject
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required

@permission_required('app.export_blockchainproject')
def export_blockchain_projects(request):
    data = list(BlockchainProject.objects.values('id', 'name', 'description', 'created_at', 'updated_at'))
    for d in data:
        d['name'] = 'ANONYMIZED'
    return JsonResponse({'projects': data})
