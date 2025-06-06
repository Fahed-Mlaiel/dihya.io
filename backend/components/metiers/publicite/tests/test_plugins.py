from ..plugins import plugin_manager

def test_plugin_manager():
    result = plugin_manager.run_all("test")
    assert len(result) > 0
    assert "Traitement environnemental" in result[0]
