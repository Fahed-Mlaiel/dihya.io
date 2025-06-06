# Fixture de services environnement pour les tests BTP
services = [
    {
        'service': 'Audit RGPD',
        'description': 'Audit de conformité RGPD pour les environnements BTP',
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
        'description': 'Surveillance des chantiers et équipements BTP',
        'type': 'monitoring',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['btp', 'monitoring'],
            'i18n': ['fr', 'en']
        }
    }
]
