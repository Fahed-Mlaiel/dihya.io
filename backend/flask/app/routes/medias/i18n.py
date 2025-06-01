"""
Internationalisation pour le module Medias (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'titre': 'Titre',
        'url': 'URL',
        'type': 'Type',
    },
    'en': {
        'titre': 'Title',
        'url': 'URL',
        'type': 'Type',
    }
}
def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
