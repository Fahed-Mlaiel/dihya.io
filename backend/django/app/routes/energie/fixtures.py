"""
fixtures.py – Jeux de données anonymisés, multilingues pour tests/démo (Dihya Coding)
"""
from .models import EnergieModel

def create_fixtures():
    EnergieModel.objects.create(name="Centrale Solaire", description_fr="Production solaire", description_en="Solar power plant")
    EnergieModel.objects.create(name="Éolienne B", description_fr="Production éolienne", description_en="Wind power plant")
