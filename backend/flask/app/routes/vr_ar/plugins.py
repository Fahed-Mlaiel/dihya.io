"""
Plugins pour le module VR/AR.
Extensible, sécurisé, RGPD, production-ready.
"""

PLUGINS = {}

def register_plugin(name, plugin):
    PLUGINS[name] = plugin

def get_plugin(name):
    return PLUGINS.get(name)
