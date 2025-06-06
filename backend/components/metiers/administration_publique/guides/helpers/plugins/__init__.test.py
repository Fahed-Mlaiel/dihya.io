# __init__.test.py – Test d'import du point d'entrée Python plugins (guides/helpers/plugins)
def test_import_plugins_init():
    import importlib
    plugins = importlib.import_module('backend.components.metiers.threed.guides.helpers.plugins')
    assert plugins.check_plugin
    assert plugins.audit_plugin
