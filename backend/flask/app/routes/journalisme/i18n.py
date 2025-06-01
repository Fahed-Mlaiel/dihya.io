"""
Internationalisation pour le module Journalisme (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'titre': 'Titre',
        'contenu': 'Contenu',
        'auteur': 'Auteur',
    },
    'en': {
        'titre': 'Title',
        'contenu': 'Content',
        'auteur': 'Author',
    }
}

def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
