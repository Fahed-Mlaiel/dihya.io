# sample_onboarding.py
# Exemple d’intégration avancée pour l’onboarding

from helpers_onboarding import start_onboarding, complete_onboarding

user = {'id': 'u123', 'name': 'Alice'}
user = start_onboarding(user)
print('Started:', user)
user = complete_onboarding(user)
print('Completed:', user)
