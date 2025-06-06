"""
Internationalisation et traduction pour Environnement.
"""

def translate(text, lang="fr"):
    """
    Traduit un texte dans la langue cible (par défaut : français).
    """
    translations = {
        "fr": f"[FR] {text}",
        "en": f"[EN] {text}",
        "de": f"[DE] {text}"
    }
    return translations.get(lang, text)

# Alias pour compatibilité industrie/tests
def i18n(text, lang="fr"):
    return translate(text, lang)
