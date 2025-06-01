"""
fixtures.py – Jeux de données anonymisés, multilingues pour tests/démo (Dihya Coding)
"""
from .models import EducationModel

def create_fixtures():
    EducationModel.objects.create(name="Université A", description_fr="Université principale", description_en="Main university")
    EducationModel.objects.create(name="Lycée B", description_fr="Lycée public", description_en="Public high school")
