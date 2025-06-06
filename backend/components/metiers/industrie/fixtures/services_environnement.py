# Fixture de services environnement pour les tests industrie
services = [
    {
        'service': 'Audit RGPD',
        'description': 'Audit de conformité RGPD pour les environnements industriels',
        'type': 'conformité',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['base', 'rgpd'],
            'i18n': ['fr', 'en', 'de']
        }
    },
    {
        'service': 'Surveillance IoT',
        'description': 'Surveillance des équipements connectés',
        'type': 'monitoring',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['iot', 'monitoring'],
            'i18n': ['fr', 'en']
        }
    }
]
