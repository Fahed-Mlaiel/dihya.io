"""
Exemple de plugin Sécurité : RGPD, i18n, audit, fallback IA, etc.
"""
from .base import SecuritePluginBase

class ExampleSecuritePlugin(SecuritePluginBase):
    name = "example"
    description = "Plugin d'exemple pour Sécurité."
    version = "1.0.0"
    author = "Dihya Team"

    def process(self, data):
        # Traitement RGPD, i18n, fallback IA, etc.
        data['example'] = 'ok'
        return data
