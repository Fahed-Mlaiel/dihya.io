"""
Internationalisation (i18n) pour le module validators.
Support multilingue, extensible, production-ready.
"""

TRANSLATIONS = {
    "fr": {
        "email_valid": "Email valide.",
        "phone_valid": "Téléphone valide.",
        "consent_valid": "Consentement RGPD valide.",
        "accessibility_valid": "Accessibilité validée."
    },
    "en": {
        "email_valid": "Valid email.",
        "phone_valid": "Valid phone.",
        "consent_valid": "Valid RGPD consent.",
        "accessibility_valid": "Accessibility validated."
    }
}

def translate(key, lang="fr"):
    return TRANSLATIONS.get(lang, TRANSLATIONS["fr"]).get(key, key)
