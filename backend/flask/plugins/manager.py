"""
Gestionnaire de plugins dynamiques pour Dihya Coding Backend
"""
import importlib
import os

PLUGINS_PATH = os.path.join(os.path.dirname(__file__), '.')

PLUGINS = {}

def load_plugins():
    # Chargement dynamique des plugins (exemple)
    for fname in os.listdir(PLUGINS_PATH):
        if fname.endswith('.py') and fname not in ['__init__.py', 'manager.py']:
            name = fname[:-3]
            mod = importlib.import_module(f'plugins.{name}')
            PLUGINS[name] = mod

def run_plugin_hook(plugin_name, user, payload):
    plugin = PLUGINS.get(plugin_name)
    if not plugin:
        return {'error': 'Plugin not found'}
    return plugin.run(user, payload)
