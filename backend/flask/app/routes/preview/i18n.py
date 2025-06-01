"""
Internationalisation pour le module Preview (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'nom': 'Nom',
        'url': 'URL',
        'type': 'Type',
    },
    'en': {
        'nom': 'Name',
        'url': 'URL',
        'type': 'Type',
    }
}
def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
