# fallback.py
# Fallback i18n Python pour Threed – exemple clé en main


def i18n_fallback(key, translations, default_value="N/A"):
    """
    Retourne une traduction par défaut si la clé n'est pas trouvée
    """
    return translations.get(key, default_value)
