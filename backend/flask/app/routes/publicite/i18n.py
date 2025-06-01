"""
Internationalisation pour le module Publicité (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'titre': 'Titre',
        'canal': 'Canal',
        'budget': 'Budget',
    },
    'en': {
        'titre': 'Title',
        'canal': 'Channel',
        'budget': 'Budget',
    }
}
def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
