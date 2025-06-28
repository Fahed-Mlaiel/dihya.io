# Exemple avancé d’intégration Compliance Python
from ...compliance.compliance_helper import compliance_nodejs_hello


def run_compliance_sample():
    print("--- Compliance Python Sample ---")
    print(compliance_nodejs_hello())


if __name__ == "__main__":
    run_compliance_sample()
