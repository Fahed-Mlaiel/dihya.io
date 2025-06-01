class CultureAuditLogger:
    def log(self, user, action, obj_type, obj_id, details=None, language=None):
        pass
culture_audit_logger = CultureAuditLogger()
