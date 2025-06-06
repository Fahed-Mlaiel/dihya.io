# services_helper.test.py – Tests unitaires Python pour helpers services Threed
import unittest
from services_helper import get_service_status, simulate_heavy_load, audit_service, simulate_extreme_load, check_access

class TestServicesHelper(unittest.TestCase):
    def test_get_service_status(self):
        status = get_service_status()
        self.assertEqual(status['status'], 'ok')
    def test_simulate_heavy_load(self):
        self.assertEqual(len(simulate_heavy_load()), 10000)
    def test_audit_service(self):
        self.assertIn('Audit avancé', audit_service('test'))
    def test_simulate_extreme_load(self):
        self.assertEqual(len(simulate_extreme_load()), 100000)
    def test_check_access(self):
        self.assertTrue(check_access({'role': 'admin'}, 'write'))
        self.assertTrue(check_access({'role': 'user'}, 'read'))
        self.assertFalse(check_access({'role': 'user'}, 'write'))

if __name__ == '__main__':
    unittest.main()
