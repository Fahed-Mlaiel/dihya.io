# sample_access.py
# Exemple d’intégration avancée pour la gestion des accès

from helpers import generate_mfa_token, provision_user

user = {'id': 'u123', 'name': 'Alice'}
provisioned = provision_user(user)
print('Provisioned:', provisioned)

mfa_token = generate_mfa_token(user['id'])
print('MFA Token:', mfa_token)
