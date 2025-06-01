"""
Fixtures avancées pour tests, démo, et CI/CD des projets banque/finance.
Inclut multilingue, sécurité, RGPD, anonymisation, accessibilité.
"""
from .models import BanqueFinanceProject
from django.contrib.auth import get_user_model
from django.utils import timezone

def create_banque_finance_fixtures():
    User = get_user_model()
    user = User.objects.filter(is_staff=True).first()
    BanqueFinanceProject.objects.create(
        name="Demo Banque/Finance Project",
        description="Projet banque/finance de démonstration.",
        created_by=user
    )
    tenants = ['default', 'banque', 'fintech']
    langues = ['fr', 'en', 'ar', 'tzm']
    for tenant in tenants:
        for lang in langues:
            client = Client.objects.create(
                nom=f"DemoClient_{lang}_{tenant}",
                numero_compte=f"CPT_{lang}_{tenant}"
            )
            Compte.objects.create(
                client=client,
                solde=1000,
                devise="EUR"
            )
            Transaction.objects.create(
                compte=Compte.objects.last(),
                montant=100,
                date=timezone.now(),
                type="virement"
            )
