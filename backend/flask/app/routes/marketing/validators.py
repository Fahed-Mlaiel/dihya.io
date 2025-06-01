"""
Validators pour le module Marketing (RGPD, sécurité, logique métier)
"""
def validate_campagne(campagne):
    if not campagne or len(campagne) < 2:
        raise ValueError('Le nom de la campagne doit comporter au moins 2 caractères.')
    return campagne
