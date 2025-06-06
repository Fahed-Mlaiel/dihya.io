# plugins.test.py – Test d’intégration avancé Plugins (fusionné, import direct PluginManager)
from . import PluginManager

class DummyPlugin:
    def run(self, x):
        return x + 1

def test_plugin_manager_integration():
    pm = PluginManager()
    plugin = DummyPlugin()
    pm.register('dummy', plugin)
    assert pm.get('dummy') is plugin
    assert pm.execute('dummy', 2) == 3
    pm.unregister('dummy')
    assert pm.get('dummy') is None
