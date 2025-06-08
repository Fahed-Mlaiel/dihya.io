# Exemple avancé d’intégration Onboarding Python (Node.js)
from ...onboarding.onboarding_helper import onboarding_nodejs_hello

def run_onboarding_sample():
    print('--- Onboarding Node.js Sample (Python) ---')
    print(onboarding_nodejs_hello())

if __name__ == "__main__":
    run_onboarding_sample()
