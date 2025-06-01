"""
Schemas pour le module Mode (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate
class ModeBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    nom = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    style = fields.Str()
    saison = fields.Str()
    date_lancement = fields.DateTime()
    actif = fields.Bool(default=True)
class ModeCreateSchema(ModeBaseSchema):
    pass
class ModeUpdateSchema(ModeBaseSchema):
    pass
