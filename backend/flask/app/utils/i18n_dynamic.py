"""
Module de traduction dynamique multilingue pour Dihya Coding.

Permet de traduire à la volée n'importe quel texte dans toutes les langues et dialectes supportés
par l'API de traduction (ex : LibreTranslate), sans créer de fichiers de langue manuels.

Bonnes pratiques :
- Utiliser une API open source pour la souveraineté et l’éthique (ex : LibreTranslate).
- Utiliser un cache mémoire pour limiter les appels API et accélérer les réponses.
- Prévoir un fallback sur la langue source en cas d’échec de l’API.
- Ne jamais transmettre de données sensibles à l’API de traduction.
- Documenter chaque fonction pour faciliter la maintenance.

Exemple d’utilisation :
    from backend.flask.app.utils.i18n_dynamic import translate_dynamic
    msg = translate_dynamic("Bienvenue sur Dihya Coding !", "ar")
"""

import requests
from functools import lru_cache
from backend.flask.app.utils.i18n_dynamic_config import (
    TRANSLATE_API_URL,
    DEFAULT_SOURCE_LANG,
    TRANSLATE_API_TIMEOUT,
)

@lru_cache(maxsize=2048)
def translate_dynamic(text, target_lang, source_lang=DEFAULT_SOURCE_LANG):
    """
    Traduit dynamiquement un texte dans la langue cible via l’API de traduction.
    Utilise un cache mémoire pour limiter les appels API.

    :param text: Texte à traduire (str)
    :param target_lang: Code langue cible (str, ex : "en", "ar", "kab", "es", etc.)
    :param source_lang: Code langue source (str, défaut : français)
    :return: Texte traduit (str)
    """
    if not text or not target_lang or target_lang == source_lang:
        return text

    payload = {
        "q": text,
        "source": source_lang,
        "target": target_lang,
        "format": "text"
    }
    try:
        resp = requests.post(TRANSLATE_API_URL, data=payload, timeout=TRANSLATE_API_TIMEOUT)
        if resp.status_code == 200:
            translated = resp.json().get("translatedText")
            if translated:
                return translated
    except Exception as e:
        # Logger l’erreur si besoin (optionnel)
        pass
    # Fallback : retourne le texte original si la traduction échoue
    return text
