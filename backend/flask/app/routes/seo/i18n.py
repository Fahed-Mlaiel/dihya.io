"""
Internationalisation pour le module SEO (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'url': 'URL',
        'titre': 'Titre',
        'description': 'Description',
        'score': 'Score',
    },
    'en': {
        'url': 'URL',
        'titre': 'Title',
        'description': 'Description',
        'score': 'Score',
    }
}
def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
