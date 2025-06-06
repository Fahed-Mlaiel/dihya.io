# __init__.test.py – Test d’intégration du point d’entrée Python helpers services
import unittest
import importlib

class TestInitHelpersServices(unittest.TestCase):
    def test_imports(self):
        mod = importlib.import_module('__init__')
        self.assertTrue(hasattr(mod, '__file__'))

if __name__ == '__main__':
    unittest.main()
