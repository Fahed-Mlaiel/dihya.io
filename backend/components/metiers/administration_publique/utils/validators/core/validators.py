"""
Validateurs avancés pour Threed.
Permet de garantir la conformité des entités métier.
"""

def validate_threed(data):
    """
    Valide les données d'une entité Threed.
    Lève une exception si le nom est manquant ou si le statut est invalide.
    """
    if not data.get("nom"):
        raise ValueError("Nom requis")
    if data.get("statut") not in (None, "actif", "inactif", "archivé"):
        raise ValueError("Statut invalide")
    return True
