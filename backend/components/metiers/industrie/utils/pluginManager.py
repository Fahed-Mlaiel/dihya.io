"""
Gestion dynamique et avancée des plugins pour Environnement.
Permet d'enregistrer, d'exécuter et de lister les plugins métier.
"""
class PluginManager:
    def __init__(self):
        self.plugins = []
    def register(self, plugin):
        if plugin not in self.plugins:
            self.plugins.append(plugin)
    def run_all(self, data):
        return [plugin.run(data) for plugin in self.plugins]
    def get_plugins(self):
        return [plugin.__class__.__name__ for plugin in self.plugins]
