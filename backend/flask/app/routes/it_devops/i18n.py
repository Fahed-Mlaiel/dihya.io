"""
Internationalisation pour le module IT DevOps (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'projet': 'Projet',
        'pipeline': 'Pipeline',
        'status': 'Statut',
        'date_deploiement': 'Date de déploiement',
    },
    'en': {
        'projet': 'Project',
        'pipeline': 'Pipeline',
        'status': 'Status',
        'date_deploiement': 'Deployment Date',
    }
}

def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
