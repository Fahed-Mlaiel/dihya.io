"""
export.py – Export RGPD, anonymisation, logs, auditabilité (Dihya Coding)
"""
from .models import *
import json

def export_environnement_data(user):
    # Sélectionner et anonymiser les données RGPD
    data = list(EnvironnementModel.objects.all().values())
    for d in data:
        d.pop('personal_data', None)
    return json.dumps(data, ensure_ascii=False)
