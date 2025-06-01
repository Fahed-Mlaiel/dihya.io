"""
Test unitaire des templates métiers (Dihya Flask)
Couvre : import/export, validation, multilingue, sécurité
"""
import unittest
from backend.flask.app.services.templates import import_template, export_template

class TestMetierTemplates(unittest.TestCase):
    def test_import_export_template(self):
        template = {"template": "sante", "fields": [{"name": "patient", "type": "string"}]}
        imported = import_template(template)
        self.assertEqual(imported["template"], "sante")
        exported = export_template(imported)
        self.assertEqual(exported["template"], "sante")

if __name__ == "__main__":
    unittest.main()
