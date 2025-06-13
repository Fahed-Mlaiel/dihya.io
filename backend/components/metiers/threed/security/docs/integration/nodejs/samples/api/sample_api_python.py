# Exemple ultra avancé d’intégration API Python (Node.js)
from ...api.api_helper import api_nodejs_hello


def run_api_sample():
    print("--- API Node.js Sample (Python) ---")
    print(api_nodejs_hello())


if __name__ == "__main__":
    run_api_sample()
