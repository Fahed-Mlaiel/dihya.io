"""
Validation avancée d'asset.
"""


def validate_asset(asset):
    """Valide un asset selon les règles métier."""
    if "name" not in asset:
        raise ValueError("Le nom est requis")
    # Ajoutez d'autres règles métier ici
    return True
