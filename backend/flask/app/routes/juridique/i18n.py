"""
Internationalisation pour le module Juridique (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'titre': 'Titre',
        'reference': 'Référence',
        'date_publication': 'Date de publication',
    },
    'en': {
        'titre': 'Title',
        'reference': 'Reference',
        'date_publication': 'Publication Date',
    }
}

def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
