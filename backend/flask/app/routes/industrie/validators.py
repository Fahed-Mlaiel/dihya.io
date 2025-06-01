"""
Validators pour le module Industrie (RGPD, sécurité, logique métier)
"""
def validate_secteur(secteur):
    if not secteur or len(secteur) < 2:
        raise ValueError('Le secteur doit comporter au moins 2 caractères.')
    return secteur
