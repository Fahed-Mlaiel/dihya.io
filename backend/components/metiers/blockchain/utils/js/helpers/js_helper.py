# js_helper.py
# Fonctions utilitaires JS (équivalent Python, clé en main, ultra avancé)


def to_camel_case(s):
    """
    Convertit une chaîne snake_case en camelCase (équivalent JS)
    :param s: str
    :return: str
    """
    parts = s.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])
