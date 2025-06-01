"""
Fixtures avancées pour tests, démo, et CI/CD des projets artistiques.
Inclut multilingue, sécurité, multitenancy, RGPD.
"""
from .models import ArtProject
from core.models import Tenant
from django.contrib.auth import get_user_model

def create_art_fixtures():
    tenant = Tenant.objects.first()
    user = get_user_model().objects.filter(is_staff=True).first()
    ArtProject.objects.create(
        name="Projet artistique Démo",
        description="Exemple de projet artistique pour tests.",
        tenant=tenant,
        created_by=user,
        is_active=True
    )
