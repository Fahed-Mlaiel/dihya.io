"""
export.py – Export RGPD, anonymisation, logs, auditabilité (Dihya Coding)
"""
from .models import *
from .logs import log_export
import json

def export_logistique_data(user):
    log_export(user, action="export_logistique")
    # Sélectionner et anonymiser les données RGPD
    data = list(LogistiqueModel.objects.all().values())
    for d in data:
        d.pop('personal_data', None)
    return json.dumps(data, ensure_ascii=False)
