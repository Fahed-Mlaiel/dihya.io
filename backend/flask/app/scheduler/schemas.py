"""
Schémas de données pour le module Scheduler (Flask).
Sécurité, RGPD, extensibilité, production-ready.
"""

from marshmallow import Schema, fields

class ScheduleJobSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, description="Nom du job planifié")
    cron = fields.Str(required=True, description="Expression CRON")
    status = fields.Str(required=True, description="Statut du job")
    last_run = fields.DateTime(dump_only=True)
    next_run = fields.DateTime(dump_only=True)
