"""
Validators pour le module Recherche (RGPD, sécurité, logique métier)
"""
def validate_sujet(sujet):
    if not sujet or len(sujet) < 2:
        raise ValueError('Le sujet doit comporter au moins 2 caractères.')
    return sujet
