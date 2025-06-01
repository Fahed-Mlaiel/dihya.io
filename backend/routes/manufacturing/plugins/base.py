"""
Base class pour plugins Manufacturing, conforme sécurité, i18n, RGPD, audit, multitenancy, etc.
"""
from typing import Dict
from ..audit import manufacturing_audit_logger

class ManufacturingPluginBase:
    name: str
    description: str
    version: str
    author: str
    enabled: bool = True

    def activate(self):
        manufacturing_audit_logger.log_plugin(self.name, 'activate')
        self.enabled = True

    def deactivate(self):
        manufacturing_audit_logger.log_plugin(self.name, 'deactivate')
        self.enabled = False

    def process(self, data: Dict) -> Dict:
        return data
