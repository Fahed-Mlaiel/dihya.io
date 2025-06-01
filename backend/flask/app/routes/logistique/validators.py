"""
Validators pour le module Logistique (RGPD, sécurité, logique métier)
"""
def validate_reference(reference):
    if not reference or len(reference) < 2:
        raise ValueError('La référence doit comporter au moins 2 caractères.')
    return reference
