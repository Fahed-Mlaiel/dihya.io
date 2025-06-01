"""
Configuration pour la traduction dynamique multilingue Dihya Coding.

Ce module centralise les paramètres de l’API de traduction utilisée pour la traduction à la volée
de toutes les langues et dialectes, sans création manuelle de fichiers par langue.

Bonnes pratiques :
- Utiliser une API open source (ex : LibreTranslate) pour la souveraineté et l’éthique.
- Prévoir un fallback local ou une langue par défaut en cas d’échec de l’API.
- Ne jamais stocker de clés API sensibles en clair dans ce fichier (utiliser des variables d’environnement).
- Documenter chaque paramètre pour faciliter la maintenance.

Exemple d’utilisation :
    from backend.flask.app.utils.i18n_dynamic_config import TRANSLATE_API_URL, DEFAULT_SOURCE_LANG, DEFAULT_TARGET_LANG
"""

import os

# URL de l’API de traduction (par défaut LibreTranslate public, à héberger pour la souveraineté)
TRANSLATE_API_URL = os.getenv("DIHYA_TRANSLATE_API_URL", "https://libretranslate.de/translate")

# Langue source par défaut (ex : "fr" pour français)
DEFAULT_SOURCE_LANG = os.getenv("DIHYA_DEFAULT_SOURCE_LANG", "fr")

# Langue cible par défaut (ex : "en" pour anglais)
DEFAULT_TARGET_LANG = os.getenv("DIHYA_DEFAULT_TARGET_LANG", "en")

# Timeout pour les requêtes de traduction (en secondes)
TRANSLATE_API_TIMEOUT = int(os.getenv("DIHYA_TRANSLATE_API_TIMEOUT", "5"))