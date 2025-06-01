class EcommerceAuditLogger:
    def log(self, user, action, obj_type, obj_id, details=None, language=None):
        pass
ecommerce_audit_logger = EcommerceAuditLogger()
