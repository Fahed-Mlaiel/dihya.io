# Exemple avancé d’intégration RBAC Python
from ...rbac.rbac_helper import rbac_nodejs_hello


def run_rbac_sample():
    print("--- RBAC Python Sample ---")
    print(rbac_nodejs_hello())


if __name__ == "__main__":
    run_rbac_sample()
