"""
Internationalisation pour le module Industrie (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'secteur': 'Secteur',
        'description': 'Description',
        'chiffre_affaires': 'Chiffre d\'affaires',
    },
    'en': {
        'secteur': 'Sector',
        'description': 'Description',
        'chiffre_affaires': 'Turnover',
    }
}

def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
