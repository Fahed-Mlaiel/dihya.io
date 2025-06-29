"""
pluginManager.py – Gestionnaire de plugins pour Energie (Python)
"""


class PluginManager:
    def __init__(self):
        self.plugins = []

    def register(self, plugin):
        self.plugins.append(plugin)

    def run_all(self, *args, **kwargs):
        results = []
        for plugin in self.plugins:
            results.append(plugin(*args, **kwargs))
        return results


pluginManager = PluginManager()

# Fichier déplacé dans samples/pluginManager.py
