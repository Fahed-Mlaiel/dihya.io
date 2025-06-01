"""
Internationalisation pour le module Recherche (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'sujet': 'Sujet',
        'description': 'Description',
    },
    'en': {
        'sujet': 'Subject',
        'description': 'Description',
    }
}
def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
