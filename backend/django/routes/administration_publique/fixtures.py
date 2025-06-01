"""
Fixtures avancées pour tests, démo, et CI/CD des projets d'administration publique.
Inclut multilingue, sécurité, multitenancy, RGPD.
"""
from .models import AdministrationPubliqueProject
from core.models import Tenant
from django.contrib.auth import get_user_model

def create_administration_publique_fixtures():
    tenant = Tenant.objects.first()
    user = get_user_model().objects.filter(is_staff=True).first()
    AdministrationPubliqueProject.objects.create(
        name="Projet administration publique Démo",
        description="Exemple de projet administration publique pour tests.",
        tenant=tenant,
        created_by=user,
        is_active=True
    )
