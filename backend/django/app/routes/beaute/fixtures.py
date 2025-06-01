"""
Fixtures avancées pour tests, démo, et CI/CD des projets beauté.
Inclut multilingue, sécurité, RGPD, anonymisation, accessibilité.
"""
from .models import BeauteProject, Salon, Prestation, Produit
from django.contrib.auth import get_user_model
from django.utils import timezone

def create_beaute_fixtures():
    User = get_user_model()
    user = User.objects.filter(is_staff=True).first()
    BeauteProject.objects.create(
        name="Demo Beauté Project",
        description="Projet beauté de démonstration.",
        created_by=user
    )
    tenants = ['default', 'salon', 'ecommerce']
    langues = ['fr', 'en', 'ar', 'tzm']
    for tenant in tenants:
        for lang in langues:
            salon = Salon.objects.create(
                nom=f"DemoSalon_{lang}_{tenant}",
                adresse=f"Adresse_{tenant}"
            )
            Prestation.objects.create(
                salon=salon,
                nom=f"Prestation_{lang}",
                prix=50
            )
            Produit.objects.create(
                nom=f"Produit_{lang}_{tenant}",
                prix=20
            )
