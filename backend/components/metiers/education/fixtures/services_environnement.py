# Fixture de services environnement pour les tests education
services = [
    {
        'service': 'Audit RGPD',
        'description': 'Audit de conformité RGPD pour les environnements education',
        'type': 'conformité',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['base', 'rgpd'],
            'i18n': ['fr', 'en', 'de']
        }
    },
    {
        'service': 'Surveillance Examens',
        'description': 'Surveillance des examens et activités pédagogiques',
        'type': 'monitoring',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['education', 'monitoring'],
            'i18n': ['fr', 'en']
        }
    }
]
