# plugins_helper.py
# Helper plugins Python pour Transport – exemple clé en main
import re


def is_valid_plugin_name(name):
    """
    Valide le nom d'un plugin (alphanumérique, tirets, underscores)
    """
    return bool(re.match(r"^[a-zA-Z0-9_-]+$", name))
