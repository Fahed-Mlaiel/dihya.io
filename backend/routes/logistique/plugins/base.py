"""
Base class pour plugins Logistique, conforme sécurité, i18n, RGPD, audit, multitenancy, etc.
"""
from typing import Dict
from ..audit import logistique_audit_logger

class LogistiquePluginBase:
    name: str
    description: str
    version: str
    author: str
    enabled: bool = True

    def activate(self):
        logistique_audit_logger.log_plugin(self.name, 'activate')
        self.enabled = True

    def deactivate(self):
        logistique_audit_logger.log_plugin(self.name, 'deactivate')
        self.enabled = False

    def process(self, data: Dict) -> Dict:
        return data
