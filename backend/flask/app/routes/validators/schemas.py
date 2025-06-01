"""
Schémas de validation (Pydantic/Marshmallow ready).
Sécurité, RGPD, extensibilité, production-ready.
"""

from marshmallow import Schema, fields

class EmailSchema(Schema):
    email = fields.Email(required=True, description="Adresse email valide")

class PhoneSchema(Schema):
    phone = fields.String(required=True, description="Numéro de téléphone international")

class ConsentSchema(Schema):
    consent = fields.Boolean(required=True, description="Consentement RGPD explicite")
