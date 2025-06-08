# sample_compliance.py
# Exemple d’intégration avancée pour la conformité

from helpers_compliance import check_compliance, generate_compliance_report

data = {'entity': 'ACME Corp', 'standards': ['ISO27001', 'SOC2']}
print('ISO27001:', check_compliance('ISO27001', data))
print(generate_compliance_report(data))
