"""
Schemas pour le module Marketing (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate

class MarketingBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    campagne = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    canal = fields.Str()
    budget = fields.Float()
    date_lancement = fields.DateTime()
    actif = fields.Bool(default=True)

class MarketingCreateSchema(MarketingBaseSchema):
    pass

class MarketingUpdateSchema(MarketingBaseSchema):
    pass
