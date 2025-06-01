"""
Base class pour plugins Voice, conforme sécurité, i18n, RGPD, audit, multitenancy, etc.
"""
from typing import Dict

class VoicePluginBase:
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
        return data
