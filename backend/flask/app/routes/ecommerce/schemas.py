"""
Schemas avancés pour le module ecommerce (validation, sérialisation, RGPD, multitenancy, sécurité).
"""
from marshmallow import Schema, fields, validate

class EcommerceBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    nom = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    categorie = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    pays = fields.Str(validate=validate.Length(max=56))
    tenant_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class EcommerceCreateSchema(EcommerceBaseSchema):
    pass

class EcommerceUpdateSchema(Schema):
    nom = fields.Str(validate=validate.Length(min=1, max=100))
    categorie = fields.Str(validate=validate.Length(min=1, max=50))
    pays = fields.Str(validate=validate.Length(max=56))

class EcommerceRGPDExportSchema(Schema):
    id = fields.Int()
    nom = fields.Str()
    categorie = fields.Str()
    pays = fields.Str()
    tenant_id = fields.Int()
    export_date = fields.DateTime()
