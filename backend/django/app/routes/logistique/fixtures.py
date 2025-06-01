"""
fixtures.py – Jeux de données anonymisés, multilingues pour tests/démo (Dihya Coding)
"""
from .models import LogistiqueModel

def create_fixtures():
    LogistiqueModel.objects.create(name="Entrepôt A", description_fr="Entrepôt principal", description_en="Main warehouse")
    LogistiqueModel.objects.create(name="Transport B", description_fr="Transport routier", description_en="Road transport")
