"""
Base class pour plugins Journalisme, conforme sécurité, i18n, RGPD, audit, multitenancy, etc.
"""
from typing import Dict
from ..audit import journalisme_audit_logger

class JournalismePluginBase:
    name: str
    description: str
    version: str
    author: str
    enabled: bool = True

    def activate(self):
        journalisme_audit_logger.log_plugin(self.name, 'activate')
        self.enabled = True

    def deactivate(self):
        journalisme_audit_logger.log_plugin(self.name, 'deactivate')
        self.enabled = False

    def process(self, data: Dict) -> Dict:
        return data
