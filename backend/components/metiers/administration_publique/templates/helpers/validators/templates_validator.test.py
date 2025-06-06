# templates_validator.test.py – Tests unitaires Python pour validateurs templates Threed
import unittest
from backend.components.metiers.threed.templates.helpers.templates_validator import is_valid_template_file, validate_template_content

class TestTemplatesValidator(unittest.TestCase):
    def test_is_valid_template_file(self):
        self.assertTrue(callable(is_valid_template_file))
    def test_validate_template_content(self):
        self.assertTrue(callable(validate_template_content))

if __name__ == '__main__':
    unittest.main()
