"""
Schemas pour le module SEO (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate
class SEOBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    url = fields.Url(required=True)
    titre = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    description = fields.Str()
    score = fields.Float()
    date_audit = fields.DateTime()
    actif = fields.Bool(default=True)
class SEOCreateSchema(SEOBaseSchema):
    pass
class SEOUpdateSchema(SEOBaseSchema):
    pass
