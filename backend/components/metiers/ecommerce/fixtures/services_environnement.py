# Fixture de services environnement pour les tests ecommerce
services = [
    {
        'service': 'Audit RGPD',
        'description': 'Audit de conformité RGPD pour les environnements ecommerce',
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
        'description': 'Surveillance des transactions et activités ecommerce',
        'type': 'monitoring',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['ecommerce', 'monitoring'],
            'i18n': ['fr', 'en']
        }
    }
]
