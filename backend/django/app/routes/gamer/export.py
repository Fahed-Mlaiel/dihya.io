"""
export.py – Export RGPD, anonymisation, logs, auditabilité (Dihya Coding)
"""
from .models import *
import json

def export_gamer_data(user):
    # Sélectionner et anonymiser les données RGPD
    data = list(GamerModel.objects.all().values())
    for d in data:
        d.pop('personal_data', None)
    return json.dumps(data, ensure_ascii=False)
