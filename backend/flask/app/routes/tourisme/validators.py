"""
Validators pour le module Tourisme (RGPD, sécurité, logique métier)
"""
def validate_nom(nom):
    if not nom or len(nom) < 2:
        raise ValueError('Le nom doit comporter au moins 2 caractères.')
    return nom
