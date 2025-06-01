"""
Fixtures avancées pour tests, démo, et CI/CD des projets agricoles.
Inclut multilingue, sécurité, multitenancy, RGPD.
"""
from .models import AgricultureProject
from core.models import Tenant
from django.contrib.auth import get_user_model

def create_agriculture_fixtures():
    tenant = Tenant.objects.first()
    user = get_user_model().objects.filter(is_staff=True).first()
    AgricultureProject.objects.create(
        name="Projet agricole Démo",
        description="Exemple de projet agricole pour tests.",
        tenant=tenant,
        created_by=user,
        is_active=True
    )
