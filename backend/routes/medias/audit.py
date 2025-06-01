"""
Audit logger pour le module Medias
"""
class MediasAuditLogger:
    def log(self, user, action, obj_type, obj_id, details=None, language=None):
        # Log avancé (RGPD, multitenancy, sectorisation, monitoring, hooks métier)
        pass
medias_audit_logger = MediasAuditLogger()
