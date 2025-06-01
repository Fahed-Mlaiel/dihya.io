"""
Internationalisation pour le module Immobilier (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'titre': 'Titre',
        'description': 'Description',
        'prix': 'Prix',
        'adresse': 'Adresse',
    },
    'en': {
        'titre': 'Title',
        'description': 'Description',
        'prix': 'Price',
        'adresse': 'Address',
    }
}

def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
