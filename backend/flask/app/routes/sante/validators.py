"""
Validators pour le module Sante (RGPD, sécurité, logique métier)
"""
def validate_patient(patient):
    if not patient or len(patient) < 2:
        raise ValueError('Le nom du patient doit comporter au moins 2 caractères.')
    return patient
