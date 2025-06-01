"""
Internationalisation (i18n) pour le module Voice.
Support multilingue, extensible, production-ready.
"""

TRANSLATIONS = {
    "fr": {
        "voice_created": "Ressource vocale créée avec succès.",
        "voice_updated": "Ressource vocale mise à jour.",
        "voice_deleted": "Ressource vocale supprimée.",
        "voice_found": "Ressource vocale trouvée."
    },
    "en": {
        "voice_created": "Voice resource created successfully.",
        "voice_updated": "Voice resource updated.",
        "voice_deleted": "Voice resource deleted.",
        "voice_found": "Voice resource found."
    }
}

def translate(key, lang="fr"):
    return TRANSLATIONS.get(lang, TRANSLATIONS["fr"]).get(key, key)
