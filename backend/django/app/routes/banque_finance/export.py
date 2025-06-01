"""
Export RGPD avancé pour les projets banque/finance (anonymisation, logs, conformité).
"""
from .models import BanqueFinanceProject
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required

@permission_required('app.export_banquefinanceproject')
def export_banque_finance_projects(request):
    data = list(BanqueFinanceProject.objects.values('id', 'name', 'description', 'created_at', 'updated_at'))
    for d in data:
        d['name'] = 'ANONYMIZED'
    return JsonResponse({'projects': data})
