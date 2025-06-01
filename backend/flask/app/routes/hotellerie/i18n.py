"""
Internationalisation pour le module Hotellerie (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'nom': 'Nom',
        'adresse': 'Adresse',
        'etoiles': 'Étoiles',
    },
    'en': {
        'nom': 'Name',
        'adresse': 'Address',
        'etoiles': 'Stars',
    }
}

def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
