# Validateurs BTP

def validate_chantier(chantier):
    return all([
        isinstance(chantier.get('id'), int),
        isinstance(chantier.get('nom'), str),
        chantier.get('etat') in ['en_cours', 'termine', 'en_pause'],
        isinstance(chantier.get('responsable'), str)
    ])

def validate_rgpd(chantier, action):
    if action == "export":
        return chantier.get('etat') in ['en_cours', 'termine']
    if action == "delete":
        return chantier.get('etat') != 'en_pause'
    return False

def validate_accessibilite(chantier):
    return chantier.get('etat') == 'en_cours'

# Validation multilingue
ERRORS = {
    'fr': {
        'invalid': "Données invalides pour le chantier.",
        'not_found': "Chantier introuvable."
    },
    'en': {
        'invalid': "Invalid chantier data.",
        'not_found': "Chantier not found."
    }
}

def get_error(lang, key):
    return ERRORS.get(lang, ERRORS['fr']).get(key, 'Erreur inconnue')
