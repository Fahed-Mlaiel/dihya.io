# Fixture de services environnement pour les tests environnement
services = [
    {
        'service': 'Audit RGPD',
        'description': 'Audit de conformité RGPD pour les environnements environnement',
        'type': 'conformité',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['base', 'rgpd'],
            'i18n': ['fr', 'en', 'de']
        }
    },
    {
        'service': 'Surveillance Ressources',
        'description': 'Surveillance des ressources et activités environnementales',
        'type': 'monitoring',
        'statut': 'actif',
        'audit': {
            'rgpd': True,
            'plugins': ['environnement', 'monitoring'],
            'i18n': ['fr', 'en']
        }
    }
]
