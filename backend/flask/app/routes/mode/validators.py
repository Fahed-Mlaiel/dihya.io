"""
Validators pour le module Mode (RGPD, sécurité, logique métier)
"""
def validate_nom(nom):
    if not nom or len(nom) < 2:
        raise ValueError('Le nom doit comporter au moins 2 caractères.')
    return nom
