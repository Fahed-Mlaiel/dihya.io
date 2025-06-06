# js_core.py
# Fonctions utilitaires JS (équivalent Python, clé en main, ultra avancé)

def is_plain_object(value):
    """
    Vérifie si une valeur est un dictionnaire pur (équivalent plain object JS)
    :param value: objet à tester
    :return: bool
    """
    return isinstance(value, dict)
