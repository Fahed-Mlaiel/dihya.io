"""
Validateurs avancés pour Publicite.
Permet de garantir la conformité des entités métier.
"""


def validate_publicite(data):
    """
    Valide les données d'une entité Publicite.
    Lève une exception si le nom est manquant ou si le statut est invalide.
    """
    if not data.get("nom"):
        raise ValueError("Nom requis")
    if data.get("statut") not in (None, "actif", "inactif", "archivé"):
        raise ValueError("Statut invalide")
    return True
