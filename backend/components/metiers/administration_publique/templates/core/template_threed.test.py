# template_threed.test.py – Tests unitaires Python pour template métier core
import unittest
from backend.components.metiers.threed.templates.core.template_threed import render_3d_template_ultra, validate_3d_template_ultra

class TestTemplateThreedCore(unittest.TestCase):
    def test_render_ultra(self):
        data = {'id': 1, 'name': 'Cube', 'meta': {'type': 'test'}, 'format': 'obj', 'i18n': {'fr': 'Cube', 'en': 'Cube'}}
        out = render_3d_template_ultra(data, {'audit': 'ok', 'accessibility': 'ok', 'rgpd': 'ok'})
        self.assertIn('Cube', out)
        self.assertIn('RGPD: ok', out)
    def test_validate_ultra(self):
        self.assertTrue(validate_3d_template_ultra({'id': 1, 'name': 'Cube', 'rgpd': 'ok'}))
        self.assertFalse(validate_3d_template_ultra({'id': 1}))

if __name__ == '__main__':
    unittest.main()
