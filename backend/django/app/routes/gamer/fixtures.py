"""
fixtures.py – Jeux de données anonymisés, multilingues pour tests/démo (Dihya Coding)
"""
from .models import GamerModel

def create_fixtures():
    GamerModel.objects.create(name="Joueur A", description_fr="Joueur pro", description_en="Pro gamer")
    GamerModel.objects.create(name="Équipe B", description_fr="Équipe e-sport", description_en="E-sport team")
