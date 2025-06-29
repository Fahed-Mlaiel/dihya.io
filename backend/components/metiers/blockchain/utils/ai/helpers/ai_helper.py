# ai_helper.py
# Helper IA Python pour Blockchain – exemple clé en main
import unicodedata


def normalize_text(text):
    """
    Nettoie et normalise un texte pour l'IA (suppression espaces, accents, etc.)
    """
    if not text:
        return ""
    text = unicodedata.normalize("NFD", text)
    text = "".join([c for c in text if not unicodedata.combining(c)])
    text = " ".join(text.split())
    return text.strip()
