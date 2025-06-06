# Fixture de services environnement pour les tests transport
services = [
    {
        'service': 'Audit RGPD',
        'description': 'Audit de conformité RGPD pour les environnements de transport',
        'type': 'conformité',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['base', 'rgpd'],
            'i18n': ['fr', 'en', 'de']
        }
    },
    {
        'service': 'Surveillance Flotte',
        'description': 'Surveillance des véhicules et équipements de transport',
        'type': 'monitoring',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['fleet', 'monitoring'],
            'i18n': ['fr', 'en']
        }
    }
]
