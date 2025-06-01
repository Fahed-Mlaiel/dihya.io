"""
fixtures.py – Jeux de données anonymisés, multilingues pour tests/démo (Dihya Coding)
"""
from .models import HealthModel

def create_fixtures():
    HealthModel.objects.create(name="Clinique A", description_fr="Clinique privée", description_en="Private clinic")
    HealthModel.objects.create(name="Hôpital B", description_fr="Hôpital public", description_en="Public hospital")
