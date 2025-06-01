"""
Validators pour le module Gamer (RGPD, sécurité, logique métier)
"""
def validate_pseudo(pseudo):
    if not pseudo or len(pseudo) < 2:
        raise ValueError('Le pseudo doit comporter au moins 2 caractères.')
    return pseudo
