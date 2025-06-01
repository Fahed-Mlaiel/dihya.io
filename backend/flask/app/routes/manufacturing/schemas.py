"""
Schemas pour le module Manufacturing (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate

class ManufacturingBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    produit = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    quantite = fields.Int()
    usine = fields.Str()
    date_fabrication = fields.DateTime()
    actif = fields.Bool(default=True)

class ManufacturingCreateSchema(ManufacturingBaseSchema):
    pass

class ManufacturingUpdateSchema(ManufacturingBaseSchema):
    pass
