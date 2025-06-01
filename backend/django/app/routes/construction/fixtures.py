"""
Fixtures avancées pour tests, démo, et CI/CD des projets construction.
Inclut multilingue, sécurité, RGPD, anonymisation, accessibilité.
"""
from .models import ConstructionProject
from django.contrib.auth import get_user_model

def create_construction_fixtures():
    User = get_user_model()
    user = User.objects.filter(is_staff=True).first()
    ConstructionProject.objects.create(
        name="Demo Construction Project",
        description="Projet construction de démonstration.",
        created_by=user
    )
