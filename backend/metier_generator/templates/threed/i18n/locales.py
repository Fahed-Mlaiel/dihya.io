"""
Gestion avancée des locales
"""


def get_locale(lang):
    import json
    import os

    with open(os.path.join(os.path.dirname(__file__), f"{lang}.json")) as f:
        return json.load(f)
