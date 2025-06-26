# Exemple avancé d’intégration Onboarding Python
from ...onboarding.onboarding_helper import onboarding_nodejs_hello


def run_onboarding_sample():
    print("--- Onboarding Python Sample ---")
    print(onboarding_nodejs_hello())


if __name__ == "__main__":
    run_onboarding_sample()
