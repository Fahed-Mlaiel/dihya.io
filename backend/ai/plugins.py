"""
Dihya Backend AI – Plugins ultra avancés pour IA backend
Extensible dynamiquement via API/CLI, sécurisé, multilingue, RGPD-ready.
"""
from typing import List, Dict, Callable

class AIPluginBase:
    """
    Base class pour tous les plugins IA backend.
    """
    name: str
    description: str
    version: str
    author: str
    enabled: bool = True

    def activate(self):
        self.enabled = True

    def deactivate(self):
        self.enabled = False

    def process(self, data: Dict) -> Dict:
        """Override pour traitement métier."""
        return data

class PluginManager:
    """
    Gestionnaire de plugins IA backend, extensible à chaud.
    """
    def __init__(self):
        self.plugins: List[AIPluginBase] = []

    def register(self, plugin: AIPluginBase):
        self.plugins.append(plugin)

    def process_all(self, data: Dict) -> Dict:
        for plugin in self.plugins:
            if plugin.enabled:
                data = plugin.process(data)
        return data

plugin_manager = PluginManager()
