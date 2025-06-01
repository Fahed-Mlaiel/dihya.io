"""
Internationalisation (i18n) pour le module AI.
Support multilingue, extensible, production-ready.
"""

TRANSLATIONS = {
    "fr": {
        "ai_created": "Modèle IA créé avec succès.",
        "ai_updated": "Modèle IA mis à jour.",
        "ai_deleted": "Modèle IA supprimé.",
        "ai_found": "Modèle IA trouvé."
    },
    "en": {
        "ai_created": "AI model created successfully.",
        "ai_updated": "AI model updated.",
        "ai_deleted": "AI model deleted.",
        "ai_found": "AI model found."
    }
}

def translate(key, lang="fr"):
    return TRANSLATIONS.get(lang, TRANSLATIONS["fr"]).get(key, key)
