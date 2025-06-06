# Fixture de services environnement pour les tests energie
services = [
    {
        'service': 'Audit RGPD',
        'description': 'Audit de conformité RGPD pour les environnements energie',
        'type': 'conformité',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['base', 'rgpd'],
            'i18n': ['fr', 'en', 'de']
        }
    },
    {
        'service': 'Surveillance Réseaux',
        'description': 'Surveillance des réseaux et équipements énergie',
        'type': 'monitoring',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['energie', 'monitoring'],
            'i18n': ['fr', 'en']
        }
    }
]
