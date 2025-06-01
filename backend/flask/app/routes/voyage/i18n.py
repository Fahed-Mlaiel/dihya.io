"""
Internationalisation (i18n) pour le module Voyage.
Support multilingue, extensible, production-ready.
"""

TRANSLATIONS = {
    "fr": {
        "voyage_created": "Voyage créé avec succès.",
        "voyage_updated": "Voyage mis à jour.",
        "voyage_deleted": "Voyage supprimé.",
        "voyage_found": "Voyage trouvé."
    },
    "en": {
        "voyage_created": "Trip created successfully.",
        "voyage_updated": "Trip updated.",
        "voyage_deleted": "Trip deleted.",
        "voyage_found": "Trip found."
    }
}

def translate(key, lang="fr"):
    return TRANSLATIONS.get(lang, TRANSLATIONS["fr"]).get(key, key)
