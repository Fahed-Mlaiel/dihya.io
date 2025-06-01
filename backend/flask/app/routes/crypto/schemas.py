"""
Schemas avancés pour le module crypto (validation, sérialisation, RGPD, multitenancy, sécurité).
"""
from marshmallow import Schema, fields, validate

class CryptoBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    nom = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    symbole = fields.Str(required=True, validate=validate.Length(min=1, max=10))
    pays = fields.Str(validate=validate.Length(max=56))
    tenant_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class CryptoCreateSchema(CryptoBaseSchema):
    pass

class CryptoUpdateSchema(Schema):
    nom = fields.Str(validate=validate.Length(min=1, max=100))
    symbole = fields.Str(validate=validate.Length(min=1, max=10))
    pays = fields.Str(validate=validate.Length(max=56))

class CryptoRGPDExportSchema(Schema):
    id = fields.Int()
    nom = fields.Str()
    symbole = fields.Str()
    pays = fields.Str()
    tenant_id = fields.Int()
    export_date = fields.DateTime()
