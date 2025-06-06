# service_threed.test.py – Tests unitaires Python pour service principal 3D
import unittest
import pytest
from service_threed import get_3d_model, list_3d_models, audit_model, secure_access
from .service_threed import ServiceThreed

class TestServiceThreed(unittest.TestCase):
    def test_get_3d_model(self):
        self.assertEqual(get_3d_model(1)['id'], 1)
        with self.assertRaises(ValueError):
            get_3d_model(None)
    def test_list_3d_models(self):
        self.assertEqual(len(list_3d_models()), 3)
    def test_audit_model(self):
        self.assertTrue(audit_model({'id': 1})['success'])
        with self.assertRaises(ValueError):
            audit_model({})
    def test_secure_access(self):
        self.assertTrue(secure_access({'role': 'admin'}, 'write'))
        self.assertTrue(secure_access({'role': 'user'}, 'read'))
        with self.assertRaises(PermissionError):
            secure_access({'role': 'user'}, 'write')

    def test_service_threed_init(self):
        service = ServiceThreed(options={"mode": "test"})
        assert service.options == {"mode": "test"}
        assert service.get_audit_trail() == []

    def test_service_threed_config_and_audit(self):
        service = ServiceThreed()
        assert service.init({"version": 1}) is True
        assert service.config == {"version": 1}
        assert service.get_audit_trail()[0]["action"] == 'init'

    def test_service_threed_process_valid(self):
        service = ServiceThreed()
        service.init({"version": 2})
        result = service.process("OP", {"foo": "bar"})
        assert result == {"success": True, "operation": "OP", "data": {"foo": "bar"}, "config": {"version": 2}}
        assert len(service.get_audit_trail()) == 2
        assert service.get_audit_trail()[1]["action"] == 'process'

    def test_service_threed_process_invalid(self):
        service = ServiceThreed()
        with pytest.raises(ValueError):
            service.process(None, {})
        assert service.get_audit_trail()[0]["action"] == 'error'

if __name__ == '__main__':
    unittest.main()
