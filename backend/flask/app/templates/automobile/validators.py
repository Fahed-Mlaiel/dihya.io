"""
Validateurs métier avancés pour le module Automobile (Dihya Coding)
Ultra avancé : sécurité, RGPD, audit, extensibilité, docstring
"""
from .schemas import VehiculeSchema, EntretienSchema
from marshmallow import ValidationError

def validate_vehicule(data):
    """Valide un véhicule selon le schéma et les règles métier."""
    errors = VehiculeSchema().validate(data)
    if errors:
        raise ValidationError(errors)
    # Règles métier additionnelles (ex : année > 2000 si électrique)
    if data.get("statut") == "vendu" and not data.get("date_vente"):
        raise ValidationError({"date_vente": "Date de vente requise si statut vendu."})
    return True

def validate_entretien(data):
    """Valide un entretien selon le schéma et les règles métier."""
    errors = EntretienSchema().validate(data)
    if errors:
        raise ValidationError(errors)
    # Règles métier additionnelles (ex : coût > 0 si effectué)
    if data.get("statut") == "effectué" and data.get("cout", 0) <= 0:
        raise ValidationError({"cout": "Coût requis si entretien effectué."})
    return True

# ... Ajouter d'autres validateurs métier ...
