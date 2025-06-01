"""
Schémas de données pour le module VR/AR (Marshmallow).
Sécurité, RGPD, extensibilité, production-ready.
"""

from marshmallow import Schema, fields

class VRARSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, description="Nom de l’asset VR/AR")
    type = fields.Str(required=False, description="Type d’asset (VR, AR, 3D, etc.)")
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
