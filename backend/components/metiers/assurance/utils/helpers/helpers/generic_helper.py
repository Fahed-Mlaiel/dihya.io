# generic_helper.py
# Helper générique Python pour Assurance – exemple clé en main


def capitalize_first(s):
    """
    Capitalise la première lettre d'une chaîne
    """
    if not s:
        return ""
    return s[0].upper() + s[1:]
