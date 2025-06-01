"""
Exemple de plugin Voice : RGPD, i18n, audit, fallback IA, etc.
"""
from .base import VoicePluginBase

class ExampleVoicePlugin(VoicePluginBase):
    name = "example"
    description = "Plugin d'exemple pour Voice."
    version = "1.0.0"
    author = "Dihya Team"

    def process(self, data):
        # Traitement RGPD, i18n, fallback IA, etc.
        data['example'] = 'ok'
        return data
