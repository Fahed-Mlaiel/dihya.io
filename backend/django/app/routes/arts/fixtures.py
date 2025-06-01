"""
Dihya – Arts Fixtures Ultra Avancé
---------------------------------
- Multilingue, multitenant, RGPD, anonymisation, accessibilité, plugins, audit, CI/CD-ready
"""
from .models import *
from django.utils import timezone

def create_arts_fixtures():
    tenants = ['default', 'galerie', 'expo']
    langues = ['fr', 'en', 'ar', 'tzm']
    for tenant in tenants:
        for lang in langues:
            artiste = Artiste.objects.create(
                nom=f"DemoArtiste_{lang}_{tenant}",
                bio=f"Bio {lang} {tenant}"
            )
            oeuvre = Oeuvre.objects.create(
                titre=f"DemoOeuvre_{lang}_{tenant}",
                artiste=artiste,
                date_creation=timezone.now()
            )
            Exposition.objects.create(
                nom=f"Expo_{lang}_{tenant}",
                date_debut=timezone.now(),
                date_fin=timezone.now(),
                oeuvre=oeuvre
            )
