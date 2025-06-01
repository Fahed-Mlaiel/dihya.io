import pytest
from .example_plugin import ExampleModePlugin

def test_example_plugin_process():
    plugin = ExampleModePlugin()
    data = {'foo': 'bar'}
    result = plugin.process(data)
    assert result['example'] == 'ok'
