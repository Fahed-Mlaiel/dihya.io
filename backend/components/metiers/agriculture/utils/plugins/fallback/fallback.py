# fallback.py
# Fallback plugin Python pour Agriculture – exemple clé en main


def plugin_fallback(name):
    """
    Fallback minimal : plugin de secours qui log l'appel
    """
    return f"[PLUGIN-FALLBACK] Appel du plugin: {name}"
