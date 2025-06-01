import pytest
from ..ai import *
from ..plugins import Example3DPlugin, register_plugin

def test_ai_plugin_import():
    """Test d’import IA et fallback IA via plugin."""
    plugin = Example3DPlugin()
    register_plugin('example', plugin)
    data = {'foo': 'bar'}
    result = plugin.process(data)
    assert result['example'] == 'ok'
