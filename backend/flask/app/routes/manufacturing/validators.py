"""
Validators pour le module Manufacturing (RGPD, sécurité, logique métier)
"""
def validate_produit(produit):
    if not produit or len(produit) < 2:
        raise ValueError('Le nom du produit doit comporter au moins 2 caractères.')
    return produit
