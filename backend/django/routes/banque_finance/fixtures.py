"""
Fixtures avancées pour tests, démo, et CI/CD des projets banque/finance.
Inclut multilingue, sécurité, multitenancy, RGPD.
"""
from .models import BanqueFinanceProject
from core.models import Tenant
from django.contrib.auth import get_user_model

def create_banque_finance_fixtures():
    tenant = Tenant.objects.first()
    user = get_user_model().objects.filter(is_staff=True).first()
    BanqueFinanceProject.objects.create(
        name="Projet banque/finance Démo",
        description="Exemple de projet banque/finance pour tests.",
        tenant=tenant,
        created_by=user,
        is_active=True
    )
