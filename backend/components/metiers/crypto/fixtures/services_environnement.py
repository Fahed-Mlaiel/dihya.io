# Fixture de services environnement pour les tests crypto
services = [
    {
        'service': 'Audit RGPD',
        'description': 'Audit de conformité RGPD pour les environnements crypto',
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
        'description': 'Surveillance des transactions et wallets crypto',
        'type': 'monitoring',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['crypto', 'monitoring'],
            'i18n': ['fr', 'en']
        }
    }
]
