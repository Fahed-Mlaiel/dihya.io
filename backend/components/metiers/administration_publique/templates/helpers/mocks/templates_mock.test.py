# templates_mock.test.py – Tests unitaires Python pour mocks templates Threed
import unittest
from backend.components.metiers.threed.templates.helpers.templates_mock import mock_rapport_audit, mock_email_notification, mock_accessibilite_audit, mock_service_export

class TestTemplatesMock(unittest.TestCase):
    def test_mock_rapport_audit(self):
        self.assertIsInstance(mock_rapport_audit(), dict)
    def test_mock_email_notification(self):
        self.assertIsInstance(mock_email_notification(), dict)
    def test_mock_accessibilite_audit(self):
        self.assertIsInstance(mock_accessibilite_audit(), dict)
    def test_mock_service_export(self):
        self.assertIsInstance(mock_service_export(), dict)

if __name__ == '__main__':
    unittest.main()
