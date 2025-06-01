"""
Schemas avancés pour le module banque_finance (validation, sérialisation, RGPD, multitenancy, sécurité).
"""
from marshmallow import Schema, fields, validate

class BanqueBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    nom = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    code_bic = fields.Str(required=True, validate=validate.Length(equal=8))
    pays = fields.Str(required=True, validate=validate.Length(min=2, max=56))
    tenant_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class BanqueCreateSchema(BanqueBaseSchema):
    pass

class BanqueUpdateSchema(Schema):
    nom = fields.Str(validate=validate.Length(min=1, max=100))
    code_bic = fields.Str(validate=validate.Length(equal=8))
    pays = fields.Str(validate=validate.Length(min=2, max=56))

class BanqueRGPDExportSchema(Schema):
    id = fields.Int()
    nom = fields.Str()
    code_bic = fields.Str()
    pays = fields.Str()
    tenant_id = fields.Int()
    export_date = fields.DateTime()
