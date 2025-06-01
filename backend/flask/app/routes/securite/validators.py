"""
Validators pour le module Securite (RGPD, sécurité, logique métier)
"""
def validate_type(type_):
    if not type_ or len(type_) < 2:
        raise ValueError('Le type doit comporter au moins 2 caractères.')
    return type_
