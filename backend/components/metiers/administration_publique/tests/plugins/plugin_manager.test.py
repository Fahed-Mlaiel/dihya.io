# plugin_manager.test.py – Tests unitaires avancés pour PluginManager (Python)
import pytest
from .plugin_manager import PluginManager

class DummyPlugin:
    def run(self, x):
        return x * 2

def test_register_and_get_plugin():
    pm = PluginManager()
    plugin = DummyPlugin()
    pm.register('dummy', plugin)
    assert pm.get('dummy') is plugin

def test_list_plugins():
    pm = PluginManager()
    pm.register('a', DummyPlugin())
    pm.register('b', DummyPlugin())
    assert set(pm.list_plugins()) == {'a', 'b'}

def test_execute_plugin():
    pm = PluginManager()
    plugin = DummyPlugin()
    pm.register('dummy', plugin)
    assert pm.execute('dummy', 3) == 6

def test_unregister_plugin():
    pm = PluginManager()
    plugin = DummyPlugin()
    pm.register('dummy', plugin)
    pm.unregister('dummy')
    assert pm.get('dummy') is None

def test_execute_invalid_plugin():
    pm = PluginManager()
    with pytest.raises(ValueError):
        pm.execute('notfound', 1)
