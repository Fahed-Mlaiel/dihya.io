"""
fixtures.py – Jeux de données anonymisés, multilingues pour tests/démo (Dihya Coding)
"""
from .models import EnvironnementModel

def create_fixtures():
    EnvironnementModel.objects.create(name="Parc National", description_fr="Zone protégée", description_en="Protected area")
    EnvironnementModel.objects.create(name="Rivière Bleue", description_fr="Rivière naturelle", description_en="Natural river")
