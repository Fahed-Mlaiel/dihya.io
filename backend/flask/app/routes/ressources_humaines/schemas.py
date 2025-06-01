"""
Schemas pour le module Ressources Humaines (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate
class RessourcesHumainesBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    nom = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    poste = fields.Str()
    date_embauche = fields.DateTime()
    actif = fields.Bool(default=True)
class RessourcesHumainesCreateSchema(RessourcesHumainesBaseSchema):
    pass
class RessourcesHumainesUpdateSchema(RessourcesHumainesBaseSchema):
    pass
