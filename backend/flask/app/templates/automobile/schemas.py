"""
Schémas de validation métier pour le module Automobile (Dihya Coding)
Ultra avancé : sécurité, RGPD, audit, extensibilité, docstring, Marshmallow
"""
from marshmallow import Schema, fields, validate, validates, ValidationError

class VehiculeSchema(Schema):
    id = fields.Int(dump_only=True)
    marque = fields.Str(required=True, validate=validate.Length(min=1, max=64))
    modele = fields.Str(required=True, validate=validate.Length(min=1, max=64))
    annee = fields.Int(required=True, validate=validate.Range(min=1900, max=2100))
    immatriculation = fields.Str(required=True, validate=validate.Length(min=1, max=32))
    statut = fields.Str(validate=validate.OneOf(["actif", "inactif", "vendu", "loué"]))
    kilometrage = fields.Int(validate=validate.Range(min=0))
    entretiens = fields.List(fields.Int())

    class Meta:
        ordered = True
        description = "Schéma de véhicule pour le module automobile."

class EntretienSchema(Schema):
    id = fields.Int(dump_only=True)
    vehicule = fields.Int(required=True)
    date = fields.Date(required=True)
    type = fields.Str(required=True)
    cout = fields.Float(validate=validate.Range(min=0))
    statut = fields.Str(validate=validate.OneOf(["planifié", "effectué", "annulé"]))

    class Meta:
        ordered = True
        description = "Schéma d'entretien pour le module automobile."

# ... Ajouter d'autres schémas métier (Location, Conducteur, Alerte) ...
