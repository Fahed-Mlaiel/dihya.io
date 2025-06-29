"""
Internationalisation et traduction pour Automobile.
"""


def translate(text, lang="fr"):
    """
    Traduit un texte dans la langue cible (par défaut : français).
    """
    translations = {
        "fr": f"[FR] {text}",
        "en": f"[EN] {text}",
        "de": f"[DE] {text}",
    }
    return translations.get(lang, text)


i18n = translate
