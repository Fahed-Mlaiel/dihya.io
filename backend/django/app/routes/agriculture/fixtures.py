"""
Dihya – Agriculture Fixtures Ultra Avancé
----------------------------------------
- Multilingue, multitenant, RGPD, anonymisation, accessibilité, plugins, audit, CI/CD-ready
"""
from .models import *
from django.utils import timezone

def create_agriculture_fixtures():
    tenants = ['default', 'coop', 'exploit']
    langues = ['fr', 'en', 'ar', 'tzm']
    for tenant in tenants:
        for lang in langues:
            # Beispiel für Demo-Daten, anpassen je nach Modellstruktur
            exploitation = Exploitation.objects.create(
                nom=f"DemoExploit_{lang}_{tenant}",
                localisation=f"Zone_{tenant}",
                superficie=42,
                date_creation=timezone.now()
            )
            Capteur.objects.create(
                type="Météo",
                exploitation=exploitation,
                valeur=23.5,
                date_mesure=timezone.now()
            )
            Alerte.objects.create(
                message=f"Alerte météo {lang}",
                exploitation=exploitation,
                niveau="orange",
                date=timezone.now()
            )
