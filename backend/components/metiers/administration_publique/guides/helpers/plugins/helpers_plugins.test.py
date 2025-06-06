# helpers_plugins.test.py – Tests unitaires et edge cases Python
from .helpers_plugins import check_plugin, audit_plugin

def test_check_plugin():
    assert check_plugin({'enabled': True, 'version': '1.0.0'}) is True
    assert check_plugin({'enabled': False, 'version': None}) is False

def test_audit_plugin():
    result = audit_plugin({'enabled': True, 'version': '1.0.0'})
    assert isinstance(result, dict)
    assert 'score' in result
    assert 'compliant' in result
