"""
Schemas avancés pour le module beaute (validation, sérialisation, RGPD, multitenancy, sécurité).
"""
from marshmallow import Schema, fields, validate

class BeauteBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    nom = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    categorie = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    description = fields.Str(validate=validate.Length(max=500))
    tenant_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class BeauteCreateSchema(BeauteBaseSchema):
    pass

class BeauteUpdateSchema(Schema):
    nom = fields.Str(validate=validate.Length(min=1, max=100))
    categorie = fields.Str(validate=validate.Length(min=1, max=50))
    description = fields.Str(validate=validate.Length(max=500))

class BeauteRGPDExportSchema(Schema):
    id = fields.Int()
    nom = fields.Str()
    categorie = fields.Str()
    description = fields.Str()
    tenant_id = fields.Int()
    export_date = fields.DateTime()
