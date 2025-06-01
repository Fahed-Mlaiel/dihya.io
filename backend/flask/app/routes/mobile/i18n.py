"""
Internationalisation pour le module Mobile (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'nom': 'Nom',
        'os': 'OS',
        'version': 'Version',
    },
    'en': {
        'nom': 'Name',
        'os': 'OS',
        'version': 'Version',
    }
}
def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
