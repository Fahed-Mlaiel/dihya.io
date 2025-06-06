# __init__.test.py – Test d’intégration du point d’entrée Python core templates
import unittest
import importlib

class TestInitCoreTemplates(unittest.TestCase):
    def test_imports(self):
        mod = importlib.import_module('core.__init__', package=__package__)
        self.assertTrue(hasattr(mod, '__file__'))

if __name__ == '__main__':
    unittest.main()
