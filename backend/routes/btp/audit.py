class BtpAuditLogger:
    def log(self, user, action, obj_type, obj_id, details=None, language=None):
        pass
btp_audit_logger = BtpAuditLogger()
