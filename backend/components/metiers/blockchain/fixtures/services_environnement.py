# Fixture de services environnement pour les tests blockchain
services = [
    {
        'service': 'Audit RGPD',
        'description': 'Audit de conformité RGPD pour les environnements blockchain',
        'type': 'conformité',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['base', 'rgpd'],
            'i18n': ['fr', 'en', 'de']
        }
    },
    {
        'service': 'Surveillance Smart Contracts',
        'description': 'Surveillance des smart contracts et transactions blockchain',
        'type': 'monitoring',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['blockchain', 'monitoring'],
            'i18n': ['fr', 'en']
        }
    }
]
