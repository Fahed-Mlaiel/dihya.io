"""
Internationalisation pour le module Environnement (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'nom': 'Nom',
        'description': 'Description',
    },
    'en': {
        'nom': 'Name',
        'description': 'Description',
    }
}

def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
