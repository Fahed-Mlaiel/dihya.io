"""
Validateurs avancés pour vr_ar.
Permet de garantir la conformité des entités métier.
"""


def validate_vr_ar(data):
    """
    Valide les données d'une entité vr_ar.
    Lève une exception si le nom est manquant ou si le statut est invalide.
    """
    if not data.get("nom"):
        raise ValueError("Nom requis")
    if data.get("statut") not in (None, "actif", "inactif", "archivé"):
        raise ValueError("Statut invalide")
    return True
