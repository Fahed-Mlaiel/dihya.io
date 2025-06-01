import pytest
from .example_plugin import ExampleAutomobilePlugin

def test_example_plugin_process():
    plugin = ExampleAutomobilePlugin()
    data = {'foo': 'bar'}
    result = plugin.process(data)
    assert result['example'] == 'ok'
