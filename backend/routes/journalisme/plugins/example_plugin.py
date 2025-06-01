"""
Exemple de plugin Journalisme : RGPD, i18n, audit, fallback IA, etc.
"""
from .base import JournalismePluginBase

class ExampleJournalismePlugin(JournalismePluginBase):
    name = "example"
    description = "Plugin d'exemple pour Journalisme."
    version = "1.0.0"
    author = "Dihya Team"

    def process(self, data):
        # Traitement RGPD, i18n, fallback IA, etc.
        data['example'] = 'ok'
        return data
