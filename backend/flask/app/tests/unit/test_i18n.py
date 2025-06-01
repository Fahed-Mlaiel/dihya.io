"""
Test unitaire de l'internationalisation (Dihya Flask)
Couvre : détection de langue, fallback, conformité multilingue
"""
import unittest
from backend.flask.app.utils.i18n import detect_language, translate

class TestI18nUtils(unittest.TestCase):
    def test_detect_language(self):
        self.assertEqual(detect_language("[fr] Bonjour"), "fr")
        self.assertEqual(detect_language("[en] Hello"), "en")
        self.assertEqual(detect_language("[ar] مرحبا"), "ar")
        self.assertEqual(detect_language("[tzr] Azul"), "tzr")
        self.assertEqual(detect_language("Texte sans balise"), "fr")

    def test_translate(self):
        self.assertIn("[en] Bonjour", translate("Bonjour", "en"))
        self.assertIn("[ar] Hello", translate("Hello", "ar"))

if __name__ == "__main__":
    unittest.main()
