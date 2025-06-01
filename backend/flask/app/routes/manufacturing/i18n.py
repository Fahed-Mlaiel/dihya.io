"""
Internationalisation pour le module Manufacturing (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'produit': 'Produit',
        'quantite': 'Quantité',
        'usine': 'Usine',
    },
    'en': {
        'produit': 'Product',
        'quantite': 'Quantity',
        'usine': 'Factory',
    }
}

def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
