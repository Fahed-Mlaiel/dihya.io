"""
Schemas avancés pour le module education (validation, sérialisation, RGPD, multitenancy, sécurité).
"""
from marshmallow import Schema, fields, validate

class EducationBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    nom = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    niveau = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    pays = fields.Str(validate=validate.Length(max=56))
    tenant_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class EducationCreateSchema(EducationBaseSchema):
    pass

class EducationUpdateSchema(Schema):
    nom = fields.Str(validate=validate.Length(min=1, max=100))
    niveau = fields.Str(validate=validate.Length(min=1, max=50))
    pays = fields.Str(validate=validate.Length(max=56))

class EducationRGPDExportSchema(Schema):
    id = fields.Int()
    nom = fields.Str()
    niveau = fields.Str()
    pays = fields.Str()
    tenant_id = fields.Int()
    export_date = fields.DateTime()
