"""
Validators pour le module Immobilier (RGPD, sécurité, logique métier)
"""
def validate_titre(titre):
    if not titre or len(titre) < 2:
        raise ValueError('Le titre doit comporter au moins 2 caractères.')
    return titre
