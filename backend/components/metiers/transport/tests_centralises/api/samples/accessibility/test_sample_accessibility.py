import unittest
from transport.api.samples.accessibility.sample_accessibility import (
    sample_accessibility_check,
)


class TestSampleAccessibility(unittest.TestCase):
    def test_accessibility_compliance(self):
        # Teste la conformité accessibilité sur un cas valide
        data = {"label": "Test", "lang": "fr"}
        result = sample_accessibility_check(data)
        self.assertTrue(result["accessible"])
        self.assertEqual(result["lang"], "fr")

    def test_accessibility_missing_label(self):
        # Teste le cas d'une ressource sans label
        data = {"lang": "fr"}
        result = sample_accessibility_check(data)
        self.assertFalse(result["accessible"])
        self.assertEqual(result["reason"], "missing_label")

    def test_accessibility_default_lang(self):
        # Teste la langue par défaut
        data = {"label": "Test"}
        result = sample_accessibility_check(data)
        self.assertEqual(result["lang"], "fr")
