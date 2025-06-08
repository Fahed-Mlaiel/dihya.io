# sample_rgpd.py
# Exemple d’intégration avancée pour la conformité RGPD

from helpers_rgpd import anonymize_data, check_consent

user = {'id': 'u123', 'name': 'Alice', 'consent': True}
print('Consent:', check_consent(user))
print('Anonymized:', anonymize_data(user))
