"""
Test ultra avancé pour le blueprint plugin (Python)
"""
from blueprints.plugins.generators.plugin import create_plugin

def test_create_plugin():
    plugin = create_plugin(metier="Inventaire", config={"version": 1}, hooks={"onStart": lambda: True})
    assert plugin["metier"] == "Inventaire"
    assert plugin["enabled"] is True
    assert plugin["config"]["version"] == 1
    assert callable(plugin["activate"])
    assert plugin["activate"]() == "Plugin Inventaire activé"
    assert plugin["deactivate"]() == "Plugin Inventaire désactivé"
