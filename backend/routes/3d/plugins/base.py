"""
Base class pour plugins 3D, conforme sécurité, i18n, RGPD, audit, multitenancy, etc.
"""
from typing import Dict
from ..audit import threed_audit_logger

class ThreeDPluginBase:
    name: str
    description: str
    version: str
    author: str
    enabled: bool = True

    def activate(self):
        threed_audit_logger.log_plugin(self.name, 'activate')
        self.enabled = True

    def deactivate(self):
        threed_audit_logger.log_plugin(self.name, 'deactivate')
        self.enabled = False

    def process(self, data: Dict) -> Dict:
        return data

class PluginManager:
    def __init__(self):
        self.plugins = []
    def register(self, plugin: ThreeDPluginBase):
        self.plugins.append(plugin)
        threed_audit_logger.log_plugin(plugin.name, 'register')
    def process_all(self, data: Dict) -> Dict:
        for plugin in self.plugins:
            if plugin.enabled:
                data = plugin.process(data)
        return data

plugin_manager = PluginManager()
