"""
Internationalisation (i18n) pour le module VR/AR.
Support multilingue, extensible, production-ready.
"""

TRANSLATIONS = {
    "fr": {
        "vr_ar_created": "Asset VR/AR créé avec succès.",
        "vr_ar_updated": "Asset VR/AR mis à jour.",
        "vr_ar_deleted": "Asset VR/AR supprimé.",
        "vr_ar_found": "Asset VR/AR trouvé."
    },
    "en": {
        "vr_ar_created": "VR/AR asset created successfully.",
        "vr_ar_updated": "VR/AR asset updated.",
        "vr_ar_deleted": "VR/AR asset deleted.",
        "vr_ar_found": "VR/AR asset found."
    }
}

def translate(key, lang="fr"):
    return TRANSLATIONS.get(lang, TRANSLATIONS["fr"]).get(key, key)
