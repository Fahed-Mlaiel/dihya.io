# Exemple d’intégration API Python (interopérabilité Node.js)
from ...nodejs.api.api_helper import api_nodejs_hello


def run_api_sample():
    print("--- API Node.js Sample (Python) ---")
    print(api_nodejs_hello())
