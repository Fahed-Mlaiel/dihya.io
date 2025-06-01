"""
Internationalisation pour le module Securite (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'type': 'Type',
        'niveau': 'Niveau',
        'description': 'Description',
    },
    'en': {
        'type': 'Type',
        'niveau': 'Level',
        'description': 'Description',
    }
}
def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
