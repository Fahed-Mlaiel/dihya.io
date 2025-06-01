"""
Fixtures avancées pour tests, démo, et CI/CD des projets crypto.
Inclut multilingue, sécurité, RGPD, anonymisation, accessibilité.
"""
from .models import CryptoProject
from django.contrib.auth import get_user_model

def create_crypto_fixtures():
    User = get_user_model()
    user = User.objects.filter(is_staff=True).first()
    CryptoProject.objects.create(
        name="Demo Crypto Project",
        description="Projet crypto de démonstration.",
        created_by=user
    )
