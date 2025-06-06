# __init__.test.py – Test d’import du point d’entrée Python core/plugins
from . import AdvancedPlugin

def test_import_AdvancedPlugin():
    assert AdvancedPlugin is not None
    plugin = AdvancedPlugin()
    plugin.activate({'user': 'test'})
    assert plugin.activated
