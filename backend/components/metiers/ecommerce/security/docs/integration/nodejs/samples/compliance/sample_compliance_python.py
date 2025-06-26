# Exemple avancé d’intégration Compliance Python (Node.js)
from ...compliance.compliance_helper import compliance_nodejs_hello


def run_compliance_sample():
    print("--- Compliance Node.js Sample (Python) ---")
    print(compliance_nodejs_hello())


if __name__ == "__main__":
    run_compliance_sample()
