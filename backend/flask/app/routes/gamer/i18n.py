"""
Internationalisation pour le module Gamer (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'pseudo': 'Pseudo',
        'email': 'Email',
        'score': 'Score',
    },
    'en': {
        'pseudo': 'Username',
        'email': 'Email',
        'score': 'Score',
    }
}

def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
