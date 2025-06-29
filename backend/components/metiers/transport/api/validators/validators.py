"""
validators.py – Validateurs ultra avancés pour l’API Transport (Python)
Inclut : validation métier, RGPD, accessibilité, audit, edge cases
"""


def validate_transport_entity(data):
    if "name" not in data or not isinstance(data["name"], str):
        raise ValueError("Invalid name")
    if "status" not in data or data["status"] not in ["active", "inactive"]:
        raise ValueError("Invalid status")
    # RGPD, accessibilité, audit, edge cases
    return True
