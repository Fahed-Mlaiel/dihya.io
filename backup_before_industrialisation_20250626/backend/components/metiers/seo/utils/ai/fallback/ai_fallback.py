"""
ai_fallback.py – Fallback AI open source pour Seo (seo)
"""


def ai_fallback(text, lang="fr"):
    """
    Simule un fallback AI open source pour la traduction ou l'analyse
    """
    if not text:
        return "[AI-Fallback] Texte manquant"
    return f"[AI-Fallback][{lang.upper()}] {text}"
