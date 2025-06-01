"""
Internationalisation (i18n) pour le module Transport.
Support multilingue, extensible, production-ready.
"""

TRANSLATIONS = {
    "fr": {
        "transport_created": "Transport créé avec succès.",
        "transport_updated": "Transport mis à jour.",
        "transport_deleted": "Transport supprimé.",
        "transport_found": "Transport trouvé."
    },
    "en": {
        "transport_created": "Transport created successfully.",
        "transport_updated": "Transport updated.",
        "transport_deleted": "Transport deleted.",
        "transport_found": "Transport found."
    }
}

def translate(key, lang="fr"):
    return TRANSLATIONS.get(lang, TRANSLATIONS["fr"]).get(key, key)
