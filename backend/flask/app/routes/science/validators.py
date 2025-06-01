"""
Validators pour le module Science (RGPD, sécurité, logique métier)
"""
def validate_domaine(domaine):
    if not domaine or len(domaine) < 2:
        raise ValueError('Le domaine doit comporter au moins 2 caractères.')
    return domaine
