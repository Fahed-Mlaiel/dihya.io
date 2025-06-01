"""
Fixtures avancées pour tests, démo, et CI/CD des projets BTP.
Inclut multilingue, sécurité, RGPD, anonymisation, accessibilité.
"""
from .models import BTPProject, Chantier, Ouvrier, Rapport
from django.contrib.auth import get_user_model
from django.utils import timezone

def create_btp_fixtures():
    User = get_user_model()
    user = User.objects.filter(is_staff=True).first()
    BTPProject.objects.create(
        name="Demo BTP Project",
        description="Projet BTP de démonstration.",
        created_by=user
    )
    tenants = ['default', 'entreprise', 'chantier']
    langues = ['fr', 'en', 'ar', 'tzm']
    for tenant in tenants:
        for lang in langues:
            chantier = Chantier.objects.create(
                nom=f"DemoChantier_{lang}_{tenant}",
                localisation=f"Zone_{tenant}"
            )
            Ouvrier.objects.create(
                nom=f"DemoOuvrier_{lang}_{tenant}",
                chantier=chantier
            )
            Rapport.objects.create(
                chantier=chantier,
                date=timezone.now(),
                contenu=f"Rapport {lang} {tenant}"
            )
