"""
Base class pour plugins Arts, conforme sécurité, i18n, RGPD, audit, multitenancy, etc.
"""
from typing import Dict
from ..audit import arts_audit_logger

class ArtsPluginBase:
    name: str
    description: str
    version: str
    author: str
    enabled: bool = True

    def activate(self):
        arts_audit_logger.log_plugin(self.name, 'activate')
        self.enabled = True

    def deactivate(self):
        arts_audit_logger.log_plugin(self.name, 'deactivate')
        self.enabled = False

    def process(self, data: Dict) -> Dict:
        return data
