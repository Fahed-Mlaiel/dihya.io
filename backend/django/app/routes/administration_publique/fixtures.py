"""
Dihya – Administration Publique Fixtures Ultra Avancé
-----------------------------------------------------
- Multilingue, multitenant, RGPD, anonymisation, accessibilité, plugins, audit, CI/CD-ready
"""
from .models import Citoyen, Demarche, Document, AuditLog
from django.utils import timezone

def create_admin_publique_fixtures():
    tenants = ['default', 'mairie', 'prefecture']
    langues = ['fr', 'en', 'ar', 'tzm']
    for tenant in tenants:
        for lang in langues:
            citoyen = Citoyen.objects.create(
                nom=f"DemoNom_{lang}_{tenant}",
                prenom=f"DemoPrenom_{lang}_{tenant}",
                date_naissance="1980-01-01",
                numero_identite=f"ID_{lang}_{tenant}",
                adresse=f"1 rue Demo, {tenant}"
            )
            demarche = Demarche.objects.create(
                type=f"Demarche_{lang}",
                date_demande=timezone.now(),
                citoyen=citoyen,
                statut="en_cours"
            )
            Document.objects.create(
                titre=f"Document_{lang}_{tenant}",
                fichier_url=f"https://cdn.dihya.app/{tenant}/{lang}/demo.pdf",
                date_emission=timezone.now(),
                citoyen=citoyen
            )
            AuditLog.objects.create(
                action="fixture_create",
                user="system",
                date=timezone.now(),
                details=f"Fixture {lang} {tenant}"
            )
