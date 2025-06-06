# Fixture de services environnement pour les tests banque_finance
services = [
    {
        'service': 'Audit RGPD',
        'description': 'Audit de conformité RGPD pour les environnements bancaires et financiers',
        'type': 'conformité',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['base', 'rgpd'],
            'i18n': ['fr', 'en', 'de']
        }
    },
    {
        'service': 'Surveillance Transactions',
        'description': 'Surveillance des transactions et opérations financières',
        'type': 'monitoring',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['finance', 'monitoring'],
            'i18n': ['fr', 'en']
        }
    }
]
