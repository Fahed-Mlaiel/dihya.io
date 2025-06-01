"""
Validators pour le module IT DevOps (RGPD, sécurité, logique métier)
"""
def validate_projet(projet):
    if not projet or len(projet) < 2:
        raise ValueError('Le nom du projet doit comporter au moins 2 caractères.')
    return projet
