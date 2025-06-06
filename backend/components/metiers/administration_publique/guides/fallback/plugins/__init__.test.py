# __init__.test.py – Test d'import du point d'entrée Python plugins (guides/fallback/plugins)
def test_import_plugins_init():
    import importlib
    plugins = importlib.import_module('backend.components.metiers.threed.guides.fallback.plugins')
    assert plugins.fallback_plugins is not None
