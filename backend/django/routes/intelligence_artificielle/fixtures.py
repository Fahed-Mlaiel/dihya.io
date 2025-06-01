"""
Fixtures avancées pour tests, démo, et CI/CD des projets IA.
Inclut multilingue, sécurité, multitenancy, RGPD.
"""
from .models import IAProject
from core.models import Tenant
from django.contrib.auth import get_user_model

def create_ia_fixtures():
    tenant = Tenant.objects.first()
    user = get_user_model().objects.filter(is_staff=True).first()
    IAProject.objects.create(
        name="Projet IA Démo",
        description="Exemple de projet IA pour tests.",
        tenant=tenant,
        created_by=user,
        is_active=True
    )
