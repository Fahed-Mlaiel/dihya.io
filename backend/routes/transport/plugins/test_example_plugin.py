import pytest
from .example_plugin import ExampleTransportPlugin

def test_example_plugin_process():
    plugin = ExampleTransportPlugin()
    data = {'foo': 'bar'}
    result = plugin.process(data)
    assert result['example'] == 'ok'
