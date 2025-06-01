"""
Internationalisation pour le module Science (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'domaine': 'Domaine',
        'sujet': 'Sujet',
    },
    'en': {
        'domaine': 'Domain',
        'sujet': 'Subject',
    }
}
def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
