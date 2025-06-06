# api.py – Stub pour tests/samples (clé en main)
class ApiService:
    """Service API ultra basique (stub)."""
    def __init__(self, options=None):
        self.options = options or {}
        self.audit = []
    def handle(self, action, data):
        self.audit.append(action)
        return {"status": "OK", "data": data}
    def getAuditTrail(self):
        return self.audit
