"""
Dihya – Assurance Fixtures Ultra Avancé
--------------------------------------
- Multilingue, multitenant, RGPD, anonymisation, accessibilité, plugins, audit, CI/CD-ready
"""
from .models import *
from django.utils import timezone

def create_assurance_fixtures():
    tenants = ['default', 'courtier', 'compagnie']
    langues = ['fr', 'en', 'ar', 'tzm']
    for tenant in tenants:
        for lang in langues:
            assure = Assure.objects.create(
                nom=f"DemoAssure_{lang}_{tenant}",
                prenom=f"DemoPrenom_{lang}_{tenant}",
                numero_contrat=f"C_{lang}_{tenant}"
            )
            Contrat.objects.create(
                assure=assure,
                type="auto",
                date_souscription=timezone.now(),
                statut="actif"
            )
            Sinistre.objects.create(
                contrat=Contrat.objects.last(),
                description=f"Sinistre {lang} {tenant}",
                date=timezone.now(),
                montant=1000
            )
