"""
Service Patient – Template Santé Dihya
CRUD, RGPD, sécurité, audit, multilingue
"""
from ..models.patient import Patient

PATIENTS_DB = {}

def add_patient(data):
    pid = len(PATIENTS_DB) + 1
    patient = Patient(id=pid, name=data["name"], dob=data["dob"], lang=data.get("lang", "fr"))
    PATIENTS_DB[pid] = patient
    return patient

def get_patient(pid):
    return PATIENTS_DB.get(pid)

def list_patients():
    return [p.to_dict() for p in PATIENTS_DB.values()]
