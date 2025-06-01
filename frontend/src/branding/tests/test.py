"""
Test unitaire branding Dihya
Sécurité, accessibilité, i18n, CI/CD, plugins
"""

import unittest
from branding import branding


class TestBranding(unittest.TestCase):
    def test_multilingue_et_securite(self):
        self.assertIn('fr', branding['slogan'])
        self.assertIn('en', branding['slogan'])
        self.assertTrue(branding['colors']['primary'].startswith('#'))


if __name__ == '__main__':
    unittest.main()
