# Exemple avancé d’intégration Audit Python (Node.js)
from ...audit.audit_helper import audit_nodejs_hello


def run_audit_sample():
    print("--- Audit Node.js Sample (Python) ---")
    print(audit_nodejs_hello())


if __name__ == "__main__":
    run_audit_sample()
