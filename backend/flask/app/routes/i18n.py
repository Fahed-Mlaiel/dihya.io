"""
Internationalisation globale (i18n) pour toutes les routes Dihya (Flask).
Support multilingue, extensible, production-ready.
"""

TRANSLATIONS = {
    "fr": {
        "success": "Succès.",
        "error": "Erreur.",
        "not_found": "Ressource non trouvée.",
        "unauthorized": "Non autorisé.",
        "forbidden": "Accès refusé."
    },
    "en": {
        "success": "Success.",
        "error": "Error.",
        "not_found": "Resource not found.",
        "unauthorized": "Unauthorized.",
        "forbidden": "Access denied."
    }
}

def translate(key, lang="fr"):
    return TRANSLATIONS.get(lang, TRANSLATIONS["fr"]).get(key, key)
