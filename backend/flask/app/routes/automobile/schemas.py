"""
Schemas avancés pour le module automobile (validation, sérialisation, RGPD, multitenancy, sécurité).
"""
from marshmallow import Schema, fields, validate

class AutomobileBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    marque = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    modele = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    annee = fields.Int(required=True, validate=validate.Range(min=1886))
    proprietaire_id = fields.Int(required=True)
    vin = fields.Str(required=True, validate=validate.Length(equal=17))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class AutomobileCreateSchema(AutomobileBaseSchema):
    pass

class AutomobileUpdateSchema(Schema):
    marque = fields.Str(validate=validate.Length(min=1, max=100))
    modele = fields.Str(validate=validate.Length(min=1, max=100))
    annee = fields.Int(validate=validate.Range(min=1886))
    vin = fields.Str(validate=validate.Length(equal=17))

class AutomobileRGPDExportSchema(Schema):
    id = fields.Int()
    marque = fields.Str()
    modele = fields.Str()
    annee = fields.Int()
    vin = fields.Str()
    proprietaire_id = fields.Int()
    export_date = fields.DateTime()
