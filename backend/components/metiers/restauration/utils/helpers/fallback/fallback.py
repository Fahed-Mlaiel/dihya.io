# fallback.py
# Fallback helper Python pour RestauratioN – exemple clé en main


def fallback_helper(fn, default_value):
    """
    Fallback minimal : retourne une valeur par défaut si la fonction échoue
    """
    try:
        return fn()
    except Exception:
        return default_value
