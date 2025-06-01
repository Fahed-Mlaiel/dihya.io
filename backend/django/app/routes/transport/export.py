"""
export.py – Export RGPD, anonymisation, logs, auditabilité (Dihya Coding)
"""
from .models import *
from .logs import log_export
import json

def export_transport_data(user):
    log_export(user, action="export_transport")
    # Sélectionner et anonymiser les données RGPD
    data = list(TransportModel.objects.all().values())
    for d in data:
        d.pop('personal_data', None)
    return json.dumps(data, ensure_ascii=False)
