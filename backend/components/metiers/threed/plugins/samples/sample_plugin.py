"""
sample_plugin.py
Exemple de plugin (sample) pour le module core plugins threed (Python).
Sert de référence pour l'intégration, la documentation et les tests.
"""

class SamplePlugin:
    def __init__(self, options=None):
        self.options = options or {}
        self.config = None

    def init(self, config):
        """Initialise le sample plugin avec des paramètres de test."""
        self.config = config
        # Logique d'initialisation de sample
        return True

    def run(self, data):
        """Exécute la fonctionnalité principale du sample plugin."""
        # Traitement métier de sample
        return {"processed": True, "data": data, "config": self.config}
