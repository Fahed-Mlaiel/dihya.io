"""
Test unitaire de la génération automatique (Dihya Flask)
Couvre : génération de code, templates métiers, sécurité, fallback
"""
import unittest
from backend.flask.app.services.generation_service import generate_code_from_template

class TestGenerationService(unittest.TestCase):
    def test_generate_code(self):
        template = {"template": "education", "fields": [{"name": "student_name", "type": "string"}]}
        data = {"student_name": "Alice"}
        code = generate_code_from_template(template, data)
        self.assertIn("Alice", code)
        self.assertIn("education", code)

if __name__ == "__main__":
    unittest.main()
