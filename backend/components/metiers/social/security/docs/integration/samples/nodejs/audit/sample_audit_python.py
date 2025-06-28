# Exemple d’intégration Audit Python (interopérabilité Node.js)
from ...nodejs.audit.audit_helper import audit_nodejs_hello


def run_audit_sample():
    print("--- Audit Node.js Sample (Python) ---")
    print(audit_nodejs_hello())
