"""
fixtures.py – Jeux de données anonymisés, multilingues pour tests/démo (Dihya Coding)
"""
from .models import EcommerceModel

def create_fixtures():
    EcommerceModel.objects.create(name="Boutique A", description_fr="Boutique principale", description_en="Main shop")
    EcommerceModel.objects.create(name="Marketplace B", description_fr="Marché en ligne", description_en="Online marketplace")
