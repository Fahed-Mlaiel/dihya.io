# Exemple ultra avancé d’intégration API Python
from ...api.api_helper import api_nodejs_hello


def run_api_sample():
    print("--- API Python Sample ---")
    print(api_nodejs_hello())


if __name__ == "__main__":
    run_api_sample()
