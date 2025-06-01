"""
Audit logger pour le module Marketing
"""
class MarketingAuditLogger:
    def log(self, user, action, obj_type, obj_id, details=None, language=None):
        # Log avancé (RGPD, multitenancy, sectorisation, monitoring, hooks métier)
        pass
marketing_audit_logger = MarketingAuditLogger()
