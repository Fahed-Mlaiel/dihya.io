"""
Exemple de plugin Tourisme : RGPD, i18n, audit, fallback IA, etc.
"""
from .base import TourismePluginBase

class ExampleTourismePlugin(TourismePluginBase):
    name = "example"
    description = "Plugin d'exemple pour Tourisme."
    version = "1.0.0"
    author = "Dihya Team"

    def process(self, data):
        # Traitement RGPD, i18n, fallback IA, etc.
        data['example'] = 'ok'
        return data
