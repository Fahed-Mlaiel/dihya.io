"""
Internationalisation pour le module Restauration (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'nom': 'Nom',
        'type': 'Type',
        'adresse': 'Adresse',
    },
    'en': {
        'nom': 'Name',
        'type': 'Type',
        'adresse': 'Address',
    }
}
def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
