# Fixture de services environnement pour les tests construction
services = [
    {
        'service': 'Audit RGPD',
        'description': 'Audit de conformité RGPD pour les environnements construction',
        'type': 'conformité',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['base', 'rgpd'],
            'i18n': ['fr', 'en', 'de']
        }
    },
    {
        'service': 'Surveillance Chantiers',
        'description': 'Surveillance des chantiers et équipements construction',
        'type': 'monitoring',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['construction', 'monitoring'],
            'i18n': ['fr', 'en']
        }
    }
]
