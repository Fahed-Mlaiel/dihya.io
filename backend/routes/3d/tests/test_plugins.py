import pytest
from ..plugins.example_plugin import Example3DPlugin

def test_example_plugin_process():
    plugin = Example3DPlugin()
    data = {'foo': 'bar'}
    result = plugin.process(data)
    assert result['example'] == 'ok'
