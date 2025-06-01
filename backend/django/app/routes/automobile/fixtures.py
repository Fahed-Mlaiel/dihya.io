"""
Dihya – Automobile Fixtures Ultra Avancé
---------------------------------------
- Multilingue, multitenant, RGPD, anonymisation, accessibilité, plugins, audit, CI/CD-ready
"""
from .models import *
from django.utils import timezone

def create_automobile_fixtures():
    tenants = ['default', 'garage', 'assureur']
    langues = ['fr', 'en', 'ar', 'tzm']
    for tenant in tenants:
        for lang in langues:
            proprietaire = Proprietaire.objects.create(
                nom=f"DemoProprio_{lang}_{tenant}",
                adresse=f"Adresse_{tenant}"
            )
            vehicule = Vehicule.objects.create(
                proprietaire=proprietaire,
                marque=f"Marque_{lang}",
                modele=f"Modele_{lang}",
                immatriculation=f"IMM_{lang}_{tenant}"
            )
            Entretien.objects.create(
                vehicule=vehicule,
                date=timezone.now(),
                description=f"Entretien {lang} {tenant}"
            )
            Sinistre.objects.create(
                vehicule=vehicule,
                date=timezone.now(),
                description=f"Sinistre {lang} {tenant}"
            )
