# Fixture de services environnement pour les tests gamer
services = [
    {
        'service': 'Audit RGPD',
        'description': 'Audit de conformité RGPD pour les environnements gamer',
        'type': 'conformité',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['base', 'rgpd'],
            'i18n': ['fr', 'en', 'de']
        }
    },
    {
        'service': 'Surveillance Sessions',
        'description': 'Surveillance des sessions et activités gaming',
        'type': 'monitoring',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['gamer', 'monitoring'],
            'i18n': ['fr', 'en']
        }
    }
]
