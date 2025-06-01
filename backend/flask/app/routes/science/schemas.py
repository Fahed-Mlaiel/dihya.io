"""
Schemas pour le module Science (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate
class ScienceBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    domaine = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    sujet = fields.Str()
    date_recherche = fields.DateTime()
    actif = fields.Bool(default=True)
class ScienceCreateSchema(ScienceBaseSchema):
    pass
class ScienceUpdateSchema(ScienceBaseSchema):
    pass
