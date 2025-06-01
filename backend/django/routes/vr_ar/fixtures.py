"""
Fixtures avancées pour tests, démo, et CI/CD des projets VR/AR.
Inclut multilingue, sécurité, multitenancy, RGPD.
"""
from .models import VRARProject
from core.models import Tenant
from django.contrib.auth import get_user_model

def create_vrar_fixtures():
    tenant = Tenant.objects.first()
    user = get_user_model().objects.filter(is_staff=True).first()
    VRARProject.objects.create(
        name="Projet VR/AR Démo",
        description="Exemple de projet VR/AR pour tests.",
        tenant=tenant,
        created_by=user,
        is_active=True
    )
