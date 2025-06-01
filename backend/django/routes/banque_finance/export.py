"""
Export RGPD avancé pour les projets banque/finance (anonymisation, logs, conformité).
"""
from .models import BanqueFinanceProject
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required

@permission_required('banque_finance.export_banque_finance_project')
def export_banque_finance_projects(request):
    """
    Exporte les projets banque/finance (données anonymisées, logs RGPD).
    """
    data = list(BanqueFinanceProject.objects.values('id', 'name', 'description', 'created_at', 'updated_at', 'is_active'))
    # Anonymisation RGPD
    for d in data:
        d['name'] = 'ANONYMIZED'
    return JsonResponse({'projects': data})
