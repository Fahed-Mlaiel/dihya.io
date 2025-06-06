# advanced_plugin.test.py – Test Python plugin avancé
from .advanced_plugin import AdvancedPlugin
import pytest

def test_advanced_plugin_workflow():
    plugin = AdvancedPlugin()
    with pytest.raises(Exception):
        plugin.run({})
    plugin.activate({'user': 'admin'})
    assert plugin.activated is True
    res = plugin.run({'foo': 'bar'})
    assert res['foo'] == 'bar'
    assert res['plugin'] == 'advanced'
    assert res['status'] == 'ok'
    assert len(plugin.get_audit_trail()) == 2
