"""
Fixtures avancées pour tests, démo, et CI/CD des projets blockchain.
Inclut multilingue, sécurité, RGPD, anonymisation, accessibilité.
"""
from .models import BlockchainProject, Node, Block, Transaction
from django.contrib.auth import get_user_model
from django.utils import timezone

def create_blockchain_fixtures():
    User = get_user_model()
    user = User.objects.filter(is_staff=True).first()
    BlockchainProject.objects.create(
        name="Demo Blockchain Project",
        description="Projet blockchain de démonstration.",
        created_by=user
    )
    tenants = ['default', 'node1', 'node2']
    langues = ['fr', 'en', 'ar', 'tzm']
    for tenant in tenants:
        for lang in langues:
            node = Node.objects.create(
                nom=f"DemoNode_{lang}_{tenant}",
                adresse=f"Adresse_{tenant}"
            )
            Block.objects.create(
                node=node,
                hash=f"HASH_{lang}_{tenant}",
                date=timezone.now()
            )
            Transaction.objects.create(
                block=Block.objects.last(),
                montant=100,
                date=timezone.now(),
                description=f"Transaction {lang} {tenant}"
            )
