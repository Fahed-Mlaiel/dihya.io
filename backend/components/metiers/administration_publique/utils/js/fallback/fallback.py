# fallback.py
# Mécanismes de secours JS (équivalent Python, clé en main, ultra avancé)

def fallback_value(value, default=None):
    """
    Retourne la valeur si elle n'est pas None, sinon retourne la valeur par défaut.
    :param value: valeur à tester
    :param default: valeur de secours
    :return: value ou default
    """
    return value if value is not None else default
