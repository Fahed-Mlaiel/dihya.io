# plugin_manager.py – Gestionnaire de plugins ultra avancé, clé en main, conforme au cahier des charges
class PluginManager:
    def __init__(self):
        self.plugins = {}

    def register(self, name, plugin):
        """Enregistre un plugin sous un nom donné."""
        self.plugins[name] = plugin

    def unregister(self, name):
        """Désenregistre le plugin associé au nom donné, le cas échéant."""
        if name in self.plugins:
            del self.plugins[name]

    def get(self, name):
        """Récupère le plugin associé au nom donné, le cas échéant."""
        return self.plugins.get(name)

    def list_plugins(self):
        """Renvoie la liste des noms de tous les plugins enregistrés."""
        return list(self.plugins.keys())

    def execute(self, name, *args, **kwargs):
        """Exécute la méthode 'run' du plugin nommé, avec les arguments fournis."""
        plugin = self.get(name)
        if plugin and hasattr(plugin, 'run'):
            return plugin.run(*args, **kwargs)
        raise ValueError(f"Plugin '{name}' not found or invalid.")
