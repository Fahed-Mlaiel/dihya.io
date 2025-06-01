"""
Internationalisation (i18n) pour le module utils.
Support multilingue, extensible, production-ready.
"""

TRANSLATIONS = {
    "fr": {
        "uuid_generated": "UUID généré avec succès.",
        "input_sanitized": "Entrée utilisateur nettoyée.",
        "event_logged": "Événement utilitaire journalisé."
    },
    "en": {
        "uuid_generated": "UUID generated successfully.",
        "input_sanitized": "User input sanitized.",
        "event_logged": "Utility event logged."
    }
}

def translate(key, lang="fr"):
    return TRANSLATIONS.get(lang, TRANSLATIONS["fr"]).get(key, key)
