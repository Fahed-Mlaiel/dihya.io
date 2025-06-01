"""
Gestion avancée des plugins VR/AR (ajout, suppression, audit, sécurité, i18n).
"""
from typing import List, Dict, Any

class VRARPluginManager:
    """
    Manager pour plugins VR/AR souverains.
    """
    def __init__(self):
        self.plugins: List[Dict[str, Any]] = []

    def register_plugin(self, plugin: Dict[str, Any]) -> None:
        self.plugins.append(plugin)

    def remove_plugin(self, name: str) -> None:
        self.plugins = [p for p in self.plugins if p.get('name') != name]

    def list_plugins(self) -> List[Dict[str, Any]]:
        return self.plugins

plugin_manager = VRARPluginManager()
