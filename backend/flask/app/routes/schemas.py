"""
Schémas globaux partagés pour toutes les routes Dihya (Flask).
Inclut pagination, réponse standard, erreurs, sécurité, RGPD, extensibilité, production-ready.
"""

from marshmallow import Schema, fields

class PaginationSchema(Schema):
    page = fields.Int(required=True, metadata={"description": "Numéro de page"})
    per_page = fields.Int(required=True, metadata={"description": "Nombre d'éléments par page"})
    total = fields.Int(required=True, metadata={"description": "Total d'éléments"})

class StandardResponseSchema(Schema):
    code = fields.Int(required=True, metadata={"description": "Code HTTP ou interne"})
    message = fields.Str(required=True, metadata={"description": "Message de statut ou d'erreur"})
    data = fields.Raw(required=False, metadata={"description": "Payload de la réponse"})

class ErrorSchema(Schema):
    code = fields.Int(required=True)
    message = fields.Str(required=True)
    details = fields.Raw(required=False)
