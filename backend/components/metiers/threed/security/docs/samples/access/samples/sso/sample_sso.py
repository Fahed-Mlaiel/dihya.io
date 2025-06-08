# sample_sso.py
# Exemple d’intégration avancée SSO (Single Sign-On)

from helpers.sso_helper import initiate_sso_login

sso = initiate_sso_login('google', 'https://app.dihya.io/callback')
print('SSO Login URL:', sso['url'])
print('Provider:', sso['provider'])
print('Initiated At:', sso['initiatedAt'])
