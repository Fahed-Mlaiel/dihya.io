"""
Test unitaire core.py (Dihya Flask)
Couvre : helpers, ServiceResponse, get_logger
"""
import unittest
from backend.flask.app.core.core import ServiceResponse, get_logger

class CoreModuleTest(unittest.TestCase):
    def test_service_response(self):
        resp = ServiceResponse(success=True, data={"foo": "bar"})
        self.assertTrue(resp.success)
        self.assertEqual(resp.data["foo"], "bar")
    def test_get_logger(self):
        logger = get_logger("test")
        self.assertTrue(hasattr(logger, "info"))
if __name__ == "__main__":
    unittest.main()

# Datei umbenannt: test_core_module.py (bitte Dateinamen im Dateisystem anpassen)
