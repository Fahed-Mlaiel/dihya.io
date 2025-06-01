"""
fixtures.py – Jeux de données anonymisés, multilingues pour tests/démo (Dihya Coding)
"""
from .models import CultureModel

def create_fixtures():
    CultureModel.objects.create(name="Musée Amazigh", description_fr="Musée culturel", description_en="Cultural museum")
    CultureModel.objects.create(name="Festival Printemps", description_fr="Festival annuel", description_en="Annual festival")
