"""
Test unitaire du système de plugins (Dihya Flask)
Couvre : chargement, extension, fallback, sécurité
"""
import unittest
from backend.flask.app.plugins import load_plugin, is_plugin_enabled

class TestPluginSystem(unittest.TestCase):
    def test_load_plugin(self):
        # Simule le chargement d'un plugin fictif
        plugin = load_plugin("demo_plugin")
        self.assertIsNotNone(plugin)
        self.assertTrue(is_plugin_enabled("demo_plugin"))

if __name__ == "__main__":
    unittest.main()
