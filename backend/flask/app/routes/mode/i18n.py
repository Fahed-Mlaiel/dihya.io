"""
Internationalisation pour le module Mode (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'nom': 'Nom',
        'style': 'Style',
        'saison': 'Saison',
    },
    'en': {
        'nom': 'Name',
        'style': 'Style',
        'saison': 'Season',
    }
}
def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
