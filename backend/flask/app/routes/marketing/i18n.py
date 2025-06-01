"""
Internationalisation pour le module Marketing (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'campagne': 'Campagne',
        'canal': 'Canal',
        'budget': 'Budget',
    },
    'en': {
        'campagne': 'Campaign',
        'canal': 'Channel',
        'budget': 'Budget',
    }
}

def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
