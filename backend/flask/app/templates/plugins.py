# Kompatibilitäts-Alias für plugin_hook

def plugin_hook(event):
    """
    Stub-Decorator für Pluginsystem, ruft das Ziel direkt auf.
    """
    def decorator(f):
        return f
    return decorator
