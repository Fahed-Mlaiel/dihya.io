"""
fixtures.py – Jeux de données anonymisés, multilingues pour tests/démo (Dihya Coding)
"""
from .models import TransportModel

def create_fixtures():
    TransportModel.objects.create(name="Camion A", description_fr="Camion principal", description_en="Main truck")
    TransportModel.objects.create(name="Train B", description_fr="Transport ferroviaire", description_en="Rail transport")
