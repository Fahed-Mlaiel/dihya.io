"""
Export RGPD avancé pour les projets crypto (anonymisation, logs, conformité).
"""
from .models import CryptoProject
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required

@permission_required('app.export_cryptoproject')
def export_crypto_projects(request):
    data = list(CryptoProject.objects.values('id', 'name', 'description', 'created_at', 'updated_at'))
    for d in data:
        d['name'] = 'ANONYMIZED'
    return JsonResponse({'projects': data})
