"""
Service métier avancé pour la gestion des assets.
"""

_assets = []


def get_all_assets():
    """Retourne tous les assets."""
    return _assets


def create_asset(data):
    """Crée un nouvel asset et l'ajoute à la liste."""
    asset = dict(id=len(_assets) + 1, **data)
    _assets.append(asset)
    return asset
