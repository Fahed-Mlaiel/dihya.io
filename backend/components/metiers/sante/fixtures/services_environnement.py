# Fixture de services environnement pour les tests santé
services = [
    {
        'service': 'Audit RGPD',
        'description': 'Audit de conformité RGPD pour les environnements santé',
        'type': 'conformité',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['base', 'rgpd'],
            'i18n': ['fr', 'en', 'de']
        }
    },
    {
        'service': 'Surveillance Dispositifs',
        'description': 'Surveillance des dispositifs médicaux connectés',
        'type': 'monitoring',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['medtech', 'monitoring'],
            'i18n': ['fr', 'en']
        }
    }
]
