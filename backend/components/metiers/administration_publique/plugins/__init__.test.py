from . import AdvancedPlugin

def test_import_AdvancedPlugin():
    assert AdvancedPlugin is not None
    plugin = AdvancedPlugin()
    plugin.activate({'user': 'test'})
    assert plugin.activated
