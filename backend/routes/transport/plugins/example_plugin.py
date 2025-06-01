"""
Exemple de plugin Transport : RGPD, i18n, audit, fallback IA, etc.
"""
from .base import TransportPluginBase

class ExampleTransportPlugin(TransportPluginBase):
    name = "example"
    description = "Plugin d'exemple pour Transport."
    version = "1.0.0"
    author = "Dihya Team"

    def process(self, data):
        # Traitement RGPD, i18n, fallback IA, etc.
        data['example'] = 'ok'
        return data
