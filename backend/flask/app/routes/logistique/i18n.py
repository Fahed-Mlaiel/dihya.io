"""
Internationalisation pour le module Logistique (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'reference': 'Référence',
        'type': 'Type',
        'statut': 'Statut',
        'date_envoi': 'Date d\'envoi',
    },
    'en': {
        'reference': 'Reference',
        'type': 'Type',
        'statut': 'Status',
        'date_envoi': 'Send Date',
    }
}

def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
