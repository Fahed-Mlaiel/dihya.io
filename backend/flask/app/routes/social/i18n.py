"""
Internationalisation pour le module Social (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'nom': 'Nom',
        'type': 'Type',
        'description': 'Description',
    },
    'en': {
        'nom': 'Name',
        'type': 'Type',
        'description': 'Description',
    }
}
def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
