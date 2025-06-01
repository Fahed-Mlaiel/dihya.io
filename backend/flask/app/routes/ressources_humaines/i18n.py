"""
Internationalisation pour le module Ressources Humaines (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'nom': 'Nom',
        'poste': 'Poste',
    },
    'en': {
        'nom': 'Name',
        'poste': 'Position',
    }
}
def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
